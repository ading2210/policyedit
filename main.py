from Crypto.Hash import SHA1
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

from interfaces.chrome_device_policy_pb2 import ChromeDeviceSettingsProto

def sign(data, private_key):
  rsa_key = RSA.importKey(private_key)

  digest = SHA1.new()
  digest.update(data)
  
  signer = PKCS1_v1_5.new(rsa_key)
  return signer.sign(digest)