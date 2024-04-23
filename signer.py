from Crypto.Hash import SHA1
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def new_private_key():
  rsa_key = RSA.generate(2048)
  return rsa_key.export_key()

def rsa_sign(data, private_key):
  rsa_key = RSA.importKey(private_key)
  digest = SHA1.new()
  digest.update(data)
  signer = PKCS1_v1_5.new(rsa_key)
  return signer.sign(digest)

def get_public_key(private_key):
  rsa_key = RSA.importKey(private_key)
  return rsa_key.public_key().exportKey(format="DER")