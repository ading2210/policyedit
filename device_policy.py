import pathlib
import json
import yaml
from google.protobuf.json_format import MessageToDict

from google.protobuf.json_format import ParseDict, ParseError
from interfaces.chrome_device_policy_pb2 import ChromeDeviceSettingsProto
from interfaces.device_management_backend_pb2 import PolicyFetchResponse
from interfaces.device_management_backend_pb2 import PolicyData

import signer

# Tools for working with the device policy blobs.

base_dir = pathlib.Path(__file__).resolve().parent
schema_dir = base_dir / "schema"

class DevicePolicy:
  def __init__(self, policy_bytes):
    self.read_policy(policy_bytes)

  # Extract device settings from the serialized data.
  def read_policy(self, policy_bytes):
    self.fetch_response = PolicyFetchResponse()
    self.fetch_response.ParseFromString(policy_bytes)
    self.policy_data = PolicyData()
    self.policy_data.ParseFromString(self.fetch_response.policy_data)    
    self.device_settings = ChromeDeviceSettingsProto()
    self.device_settings.ParseFromString(self.policy_data.policy_value)

  # Convert to a format capable of being input to import_policy.
  def convert_to_policies_json(self):
    proto_map_path = schema_dir / "device_policy_proto_map.yaml"
    proto_map = yaml.safe_load(proto_map_path.read_bytes())

    # Reverse the order of the dictionary for simple requests.
    proto_map_reversed = {v: k for k, v in proto_map.items()}
    
    # Grab the settings of the policy in dictionary format.
    policy_settings = MessageToDict(self.device_settings, preserving_proto_field_name=True)

    convertedSettings = dict()
    for name in proto_map_reversed.keys():
        key = proto_map_reversed[name]
        split_name = name.split('.')
        if split_name[0] in policy_settings:
            if split_name[1] in policy_settings[split_name[0]]:
                convertedSettings[key] = policy_settings[split_name[0]][split_name[1]]

    return convertedSettings

  # Serialize the device settings and sign it.
  def serialize_policy(self, private_key):
    # Place the serialized settings in our protobuf objects.
    self.policy_data.policy_value = self.device_settings.SerializeToString()
    self.fetch_response.policy_data = self.policy_data.SerializeToString()

    # Sign with rsa and store the public key.
    new_signature = signer.rsa_sign(self.fetch_response.policy_data, private_key)
    public_key = signer.get_public_key(private_key)
    self.fetch_response.policy_data_signature = new_signature
    self.fetch_response.new_public_key = public_key
    return self.fetch_response.SerializeToString()


  def import_policy(self, policy_dict):
    proto_map_path = schema_dir / "device_policy_proto_map.yaml"
    proto_map = yaml.safe_load(proto_map_path.read_bytes())

    valid_names = list(proto_map.keys())

    # Find which names in the policy dict are device policies.
    dict_names = list(policy_dict.keys())
    imported_names = list(set(valid_names).intersection(dict_names))

    # Iterate through the policies and set the values in the device settings.
    for policy_name in imported_names:
      policy_key = proto_map[policy_name]
      
      policy_value = policy_dict[policy_name]
      try: 
        self.set_policy_item(policy_key, policy_value)
      except ParseError:
        print(f"skipped policy {policy_name} due to invalid parameters")
    
    print(self.device_settings)

  def set_policy_item(self, policy_key, policy_value):
    # See if we need to fix a non-standard mapping of values.
    policy_converted = self.fix_policy_value(policy_key, policy_value)
    
    # Construct a dict for the proto message.
    key1, key2 = policy_key.split(".")
    policy_json = {
      key1: {
        key2: policy_converted
      }
    }
    # Attempt to parse and insert it into the device settings.
    ParseDict(policy_json, self.device_settings)
  
  # Sometimes policy json values dont match with the protobuf values.
  def fix_policy_value(self, policy_key, policy_value):
    if policy_key == "DeviceLocalAccounts":
      return self.convert_local_accounts(policy_value)
    
    return policy_value
  
  # Helper function to get all the items in a dict which have a certain prefix.
  def items_from_prefix(self, target_dict, prefix):
    returned_dict = {}
    for key, value in target_dict.items():
      if not key.startswith(prefix):
        continue
      key = key.replace(prefix, "", 1)
      returned_dict[key] = value
    return returned_dict
  
  # Convert the list of local accounts so it can be imported by protobuf.
  def convert_local_accounts(self, policy_value):
    new_accounts = []
    
    for account in policy_value:
      # Setup common attributes.
      new_account = {
        "account_id": account["account_id"] + "@kiosk-apps",
        "type": account["type"]
      }
      info_prefix = None
      info_key = None

      # Get prefix and proto key from type.
      if account["type"] == "ACCOUNT_TYPE_KIOSK_APP":
        info_prefix = "kiosk_"
        info_key = "kiosk_app"
      elif account["type"] == "ACCOUNT_TYPE_WEB_KIOSK_APP":
        info_prefix = "web_kiosk_"
        info_key = "web_kiosk_app"
      
      # Apply this to the new dict.
      if info_key:
        account_info = self.items_from_prefix(account, info_prefix)
        new_account[info_key] = account_info
        new_accounts.append(new_account)
      else:
        print(f"skipping kiosk account because of unknown type: {account}")
    
    return new_accounts