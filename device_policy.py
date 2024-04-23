import pathlib
import json
import copy
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
    fetch_response = PolicyFetchResponse()
    fetch_response.ParseFromString(policy_bytes)
    policy_data = PolicyData()
    policy_data.ParseFromString(fetch_response.policy_data)
    self.device_settings = ChromeDeviceSettingsProto()
    self.device_settings.ParseFromString(policy_data.policy_value)


  #serialize the device settings and sign it
  def serialize_policy(self, private_key):
    #create new protobuf objects and place the serialized settings in them
    policy_data = PolicyData()
    fetch_response = PolicyFetchResponse()
    policy_data.policy_value = self.device_settings.SerializeToString()
    fetch_response.policy_data = policy_data.SerializeToString()

    #sign with rsa and store the public key
    new_signature = signer.rsa_sign(fetch_response.policy_data, private_key)
    public_key = signer.get_public_key(private_key)
    fetch_response.policy_data_signature = new_signature
    fetch_response.new_public_key = public_key
    return fetch_response.SerializeToString()


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
    #construct a dict for the proto message
    key1, key2 = policy_key.split(".")
    policy_json = {
      key1: {
        key2: policy_value
      }
    }
    #attempt to parse and insert it into the device settings
    ParseDict(policy_json, self.device_settings)