import sqlite3

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

#DOES NOT WORK! this code was my attempt at experimenting with reading the nssdb
def load_db(key4_path):
  con = sqlite3.connect(key4_path)
  cur = con.cursor()
  cur.execute("SELECT a100, a120, a122, a123, a124, a125, a128, a127, a128 FROM nssPrivate;")

  for row in cur:
    #print(row)
    row_int = [int.from_bytes(col, byteorder="big") for col in row]
    key_type, modulus, public_exponent, private_exponent, prime_1, prime_2, exponent_1, exponent_2, coefficient = row_int
    #print(row_int)

    if key_type != 0:
      continue #not rsa type
    
    try:
      rsa_key = RSA.construct((modulus, public_exponent, private_exponent, prime_1, prime_2, coefficient))
      print(rsa_key)
    except Exception as e:
      print(e)
      print("fail")
  
  con.close()

#load_db("data/test-user/.pki/nssdb/key4.db")