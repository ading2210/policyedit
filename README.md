# Chrome OS Policy Editor

This is a Python program which is able to modify the device policies on a Chrome OS device. 

## Installation:
You must have Python 3 installed, with support for virtual environments and pip.

Clone this repository, and run the following commands:
```
python3 -m venv .venv
pip3 install -r requirements.txt
```

## Usage:
```
usage: main.py [-h] --private-key PRIVATE_KEY --public-key PUBLIC_KEY --device-policy DEVICE_POLICY --new-policy NEW_POLICY

options:
  -h, --help            show this help message and exit
  --private-key PRIVATE_KEY
                        The path to the private key
  --public-key PUBLIC_KEY
                        The path to the public key that will be generated
  --device-policy DEVICE_POLICY
                        The path to the device policy file
  --new-policy NEW_POLICY
                        The modified policy file that is generated
```

### On Real Chrome OS:
1. Make sure you are in developer mode and have rootfs verification off.
2. Add `--disable-policy-key-verification` to the end of `/etc/chrome_dev.conf`.
3. Edit `/etc/lsb-release` to change the release channel to `testimage-channel`.
4. Generate a normal RSA private key.
5. Run `main.py` with the correct arguments, specifying any policy files that are in `/var/lib/devicesettings/`.
6. Copy the public key to `/var/lib/devicesettings/owner.key`.
7. Overwrite the original policy files with the patched versions.

### On Linux-ChromiumOS:
1. Locate the user data directory (this defaults to `~/.config/chromium`) or explicitly set it with `--user-data-dir`.
2. Generate a normal RSA private key using OpenSSL: `openssl genrsa -out key.pem 1024`
3. Run `main.py`, specifying the policy file at `DATA_DIR/stub_device_policy`.
4. Overwrite the original policy with the patched version.
5. Copy the public key to `DATA_DIR/stub_owner.key`.