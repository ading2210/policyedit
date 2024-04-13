import argparse
from pathlib import Path

from Crypto.Hash import SHA1
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

from interfaces.chrome_device_policy_pb2 import ChromeDeviceSettingsProto
from interfaces.device_management_backend_pb2 import PolicyFetchResponse
from interfaces.device_management_backend_pb2 import PolicyData

def rsa_sign(data, private_key):
  rsa_key = RSA.importKey(private_key)
  digest = SHA1.new()
  digest.update(data)
  signer = PKCS1_v1_5.new(rsa_key)
  return signer.sign(digest)

def get_public_key(private_key):
  rsa_key = RSA.importKey(private_key)
  return rsa_key.public_key().exportKey(format="DER")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  sub_parsers = parser.add_subparsers(dest="mode")

  view_command = sub_parsers.add_parser("view", help="Read the device settings without modifying anything.")
  view_command.add_argument("--device-policy", required=True, help="The path to the device policy file")

  patch_command = sub_parsers.add_parser("patch", help="Patch an existing device policy file.")
  patch_command.add_argument("--device-policy", required=True, help="The path to the device policy file")
  patch_command.add_argument("--private-key", required=True, help="The path to the private key")
  patch_command.add_argument("--public-key", required=True,  help="The path to the public key that will be generated")
  patch_command.add_argument("--new-policy", required=True,  help="The modified policy file that is generated")
  args = parser.parse_args()

  fetch_response_data = Path(args.device_policy).expanduser().read_bytes()

  #extract device settings from the serialized data
  fetch_response = PolicyFetchResponse()
  fetch_response.ParseFromString(fetch_response_data)
  policy_data = PolicyData()
  policy_data.ParseFromString(fetch_response.policy_data)
  device_settings = ChromeDeviceSettingsProto()
  device_settings.ParseFromString(policy_data.policy_value)

  if args.mode == "view":
    print(device_settings)

  else:
    private_key = Path(args.private_key).expanduser().read_bytes()
    new_policy_path = Path(args.new_policy).expanduser()
    public_key_path = Path(args.public_key).expanduser()

    #make our edits to the device settings
    device_settings.guest_mode_enabled.guest_mode_enabled = False

    #re-encode the settings and sign it
    policy_data.policy_value = device_settings.SerializeToString()
    fetch_response.policy_data = policy_data.SerializeToString()
    fetch_response.policy_data_signature = rsa_sign(fetch_response.policy_data, private_key)
    fetch_response.new_public_key = get_public_key(private_key)

    #write the new policy file and public key to a file so chrome can use them
    new_policy_data = fetch_response.SerializeToString()
    new_policy_path.write_bytes(new_policy_data)
    public_key_path.write_bytes(fetch_response.new_public_key)