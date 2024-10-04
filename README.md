# Chrome OS Policy Editor

This is a Python program which is able to modify the device policies on a Chrome OS system, based on [lilac](https://github.com/MercuryWorkshop/lilac).

# Installation:
You must have Python 3 installed on Linux, with support for virtual environments and pip.
You can get Python 3 on real ChromeOS by running `dev_install` as root.

Clone this repository, and run the following commands:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

# Usage Instructions

## On Real Chrome OS:
1. Make sure you are in developer mode and have rootfs verification off.
2. Add `--disable-policy-key-verification` to the end of `/etc/chrome_dev.conf`.
3. Edit `/etc/lsb-release` to change the release channel to `testimage-channel`.
4. Run `main.py` with the correct arguments (see the [arguments](#arguments) section), specifying any policy files that are in `/var/lib/devicesettings/`.
5. Copy the public key to `/var/lib/devicesettings/owner.key`.
6. Overwrite the original policy files with the patched versions.

## On Linux/ChromiumOS:
1. Locate the user data directory (this defaults to `~/.config/chromium`) or explicitly set it with `--user-data-dir=DATA_DIR`.
2. Run `main.py`, specifying the policy file at `DATA_DIR/stub_device_policy`.
3. Overwrite the original policy with the patched version.
4. Copy the public key to `DATA_DIR/stub_owner.key`.

## Arguments:

### View Mode
(Hint: Use this to generate a `policies.json` file)
```
usage: main.py view [-h] --device-policy DEVICE_POLICY

options:
  -h, --help            show this help message and exit
  --device-policy DEVICE_POLICY
                        The path to the device policy file
```

### Patch Mode
```
usage: main.py patch [-h] --device-policy DEVICE_POLICY --new-key NEW_KEY --new-policy NEW_POLICY [--policy-json POLICY_JSON]

options:
  -h, --help            show this help message and exit
  --device-policy DEVICE_POLICY
                        The path to the device policy file
  --new-key NEW_KEY     The path to the public key that will be generated
  --new-policy NEW_POLICY
                        The modified policy file that is generated
  --policy-json POLICY_JSON
                        Import a policies.json file
```

## Copyright:

This repository is licensed under the GNU GPL v3.

```
ading2210/policyedit - A program to modify Chrome OS device policies
Copyright (C) 2024 ading2210

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```