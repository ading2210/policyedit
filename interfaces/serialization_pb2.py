# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13serialization.proto\x12\x04rlwe\"=\n\x17SerializedNttPolynomial\x12\x0e\n\x06\x63oeffs\x18\x01 \x01(\x0c\x12\x12\n\nnum_coeffs\x18\x02 \x01(\x05\"p\n!SerializedSymmetricRlweCiphertext\x12(\n\x01\x63\x18\x01 \x03(\x0b\x32\x1d.rlwe.SerializedNttPolynomial\x12\x12\n\npower_of_s\x18\x02 \x01(\x05\x12\r\n\x05\x65rror\x18\x03 \x01(\x01\"\xa5\x01\n\x1cSerializedRelinearizationKey\x12(\n\x01\x63\x18\x01 \x03(\x0b\x32\x1d.rlwe.SerializedNttPolynomial\x12!\n\x19log_decomposition_modulus\x18\x02 \x01(\x05\x12\x11\n\tnum_parts\x18\x03 \x01(\x05\x12\x11\n\tprng_seed\x18\x04 \x01(\x0c\x12\x12\n\npower_of_s\x18\x05 \x01(\x05\"F\n\x13SerializedGaloisKey\x12/\n\x03key\x18\x01 \x01(\x0b\x32\".rlwe.SerializedRelinearizationKeyB&H\x03Z\"github.com/google/shell-encryption')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serialization_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003Z\"github.com/google/shell-encryption'
  _SERIALIZEDNTTPOLYNOMIAL._serialized_start=29
  _SERIALIZEDNTTPOLYNOMIAL._serialized_end=90
  _SERIALIZEDSYMMETRICRLWECIPHERTEXT._serialized_start=92
  _SERIALIZEDSYMMETRICRLWECIPHERTEXT._serialized_end=204
  _SERIALIZEDRELINEARIZATIONKEY._serialized_start=207
  _SERIALIZEDRELINEARIZATIONKEY._serialized_end=372
  _SERIALIZEDGALOISKEY._serialized_start=374
  _SERIALIZEDGALOISKEY._serialized_end=444
# @@protoc_insertion_point(module_scope)