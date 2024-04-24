import pathlib
import json
import yaml

from google.protobuf.json_format import ParseDict, ParseError
from interfaces.chrome_device_policy_pb2 import ChromeDeviceSettingsProto
from interfaces.device_management_backend_pb2 import PolicyFetchResponse
from interfaces.device_management_backend_pb2 import PolicyData

import signer

#tools for working with the device policy blobs

base_dir = pathlib.Path(__file__).resolve().parent
schema_dir = base_dir / "schema"

class DevicePolicy:
  def __init__(self, policy_bytes):
    self.read_policy(policy_bytes)

  #extract device settings from the serialized data
  def read_policy(self, policy_bytes):
    self.fetch_response = PolicyFetchResponse()
    self.fetch_response.ParseFromString(policy_bytes)
    self.policy_data = PolicyData()
    self.policy_data.ParseFromString(self.fetch_response.policy_data)
    print(self.policy_data)
    print(self.fetch_response)
    
    self.device_settings = ChromeDeviceSettingsProto()
    self.device_settings.ParseFromString(self.policy_data.policy_value)


  #serialize the device settings and sign it
  def serialize_policy(self, private_key):
    #place the serialized settings in our protobuf objects
    self.policy_data.policy_value = self.device_settings.SerializeToString()
    self.fetch_response.policy_data = self.policy_data.SerializeToString()

    #sign with rsa and store the public key
    new_signature = signer.rsa_sign(self.fetch_response.policy_data, private_key)
    public_key = signer.get_public_key(private_key)
    self.fetch_response.policy_data_signature = new_signature
    self.fetch_response.new_public_key = public_key
    return self.fetch_response.SerializeToString()


  def import_policy(self, policy_dict):
    proto_map_path = schema_dir / "device_policy_proto_map.yaml"
    legacy_map_path = schema_dir / "legacy_device_policy_proto_map.yaml"
    proto_map = yaml.safe_load(proto_map_path.read_bytes())
    legacy_proto_map = yaml.safe_load(legacy_map_path.read_bytes())

    #get list of device policy keys
    for key, item in legacy_proto_map.items():
      if not key or not item:
        continue
      proto_map[key] = item
    valid_names = list(proto_map.keys())

    #find which names in the policy dict are device policies
    dict_names = list(policy_dict.keys())
    imported_names = list(set(valid_names).intersection(dict_names))

    #iterate through the policies and set the values in the device settings
    message_dict = {}
    for policy_name in imported_names:
      policy_key = proto_map[policy_name]
      if type(policy_key) == list:
        print(f"skipped policy {policy_name} since multiple mappings are not supported yet")
        continue
      
      policy_value = policy_dict[policy_name]["value"]
      try: 
        self.set_policy_item(policy_key, policy_value)
      except ParseError:
        print(f"skipped policy {policy_name} due to invalid parameters")
    
    print(self.device_settings)

  def set_policy_item(self, policy_key, policy_value):
    #see if we need to fix a non-standard mapping of values
    policy_converted = self.fix_policy_value(policy_key, policy_value)
    
    #construct a dict for the proto message
    key1, key2 = policy_key.split(".")
    policy_json = {
      key1: {
        key2: policy_converted
      }
    }
    #attempt to parse and insert it into the device settings
    ParseDict(policy_json, self.device_settings)
  
  #sometimes policy json values dont match with the protobuf values
  def fix_policy_value(self, policy_key, policy_value):
    if policy_key == "device_local_accounts.account":
      return self.convert_local_accounts(policy_value)
    
    return policy_value
  
  #helper function to get all the items in a dict which have a certain prefix
  def items_from_prefix(self, target_dict, prefix):
    returned_dict = {}
    for key, value in target_dict.items():
      if not key.startswith(prefix):
        continue
      key = key.replace(prefix, "", 1)
      returned_dict[key] = value
    return returned_dict
  
  #convert the list of local accounts so it can be imported by protobuf
  def convert_local_accounts(self, policy_value):
    new_accounts = []
    
    for account in policy_value:
      #setup common attributes
      new_account = {
        "account_id": account["id"] + "@kiosk-apps",
        "type": account["type"]
      }
      info_prefix = None
      info_key = None

      #get prefix and proto key from type
      if account["type"] == 1:
        info_prefix = "kiosk_"
        info_key = "kiosk_app"
      elif account["type"] == 4:
        info_prefix = "web_kiosk_"
        info_key = "web_kiosk_app"
      
      #apply this to the new dict
      if info_key:
        account_info = self.items_from_prefix(account, info_prefix)
        new_account[info_key] = account_info
        new_accounts.append(new_account)
      else:
        print(f"skipping kiosk account because of unknown type: {account}")
    
    return new_accounts