import argparse
import sys
import json
from pathlib import Path

import device_policy
import signer

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
  patch_command.add_argument("--policy-json", required=False, help="Import a policies.json file")

  args = parser.parse_args()

  if args.mode is None:
    parser.print_help()
    sys.exit(1)

  policy_bytes = Path(args.device_policy).expanduser().read_bytes()
  policy = device_policy.DevicePolicy(policy_bytes)

  if args.mode == "view":
    print(policy.device_settings)

  else:
    private_key = Path(args.private_key).expanduser().read_bytes()
    new_policy_path = Path(args.new_policy).expanduser()
    public_key_path = Path(args.public_key).expanduser()

    if args.policy_json:
      policy_json = Path(args.policy_json).expanduser().read_text()
      policy_dict = json.loads(policy_json)["chromePolicies"]
      policy.import_policy(policy_dict)
      sys.exit(1)

    new_policy_data = policy.serialize_policy(private_key)
    new_policy_path.write_bytes(new_policy_data)
    public_key_path.write_bytes(signer.get_public_key(private_key))