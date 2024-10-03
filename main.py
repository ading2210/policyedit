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
  patch_command.add_argument("--new-key", required=True,  help="The path to the public key that will be generated")
  patch_command.add_argument("--new-policy", required=True,  help="The modified policy file that is generated")
  patch_command.add_argument("--policy-json", required=False, help="Import a policies.json file")

  args = parser.parse_args()

  if args.mode is None:
    parser.print_help()
    sys.exit(1)

  policy_bytes = Path(args.device_policy).expanduser().read_bytes()
  policy = device_policy.DevicePolicy(policy_bytes)

  if args.mode == "view":
    print(json.dumps(policy.convert_to_policies_json(), indent=2))

  if args.mode == "patch":
    private_key = signer.new_private_key()
    new_policy_path = Path(args.new_policy).expanduser()
    public_key_path = Path(args.new_key).expanduser()

    if args.policy_json:
      policy_json = Path(args.policy_json).expanduser().read_text()
      policy_dict = json.loads(policy_json)
      policy.import_policy(policy_dict)

    new_policy_data = policy.serialize_policy(private_key)
    new_policy_path.write_bytes(new_policy_data)
    public_key_path.write_bytes(signer.get_public_key(private_key))