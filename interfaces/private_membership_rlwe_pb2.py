# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: private_membership_rlwe.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import private_membership_pb2 as private__membership__pb2
from . import serialization_pb2 as serialization__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprivate_membership_rlwe.proto\x12\x17private_membership.rlwe\x1a\x18private_membership.proto\x1a\x13serialization.proto\"q\n PrivateMembershipRlweOprfRequest\x12\x15\n\rencrypted_ids\x18\x01 \x03(\x0c\x12\x36\n\x08use_case\x18\x02 \x01(\x0e\x32$.private_membership.rlwe.RlweUseCase\"\xef\x02\n!PrivateMembershipRlweOprfResponse\x12\x43\n\x14\x64oubly_encrypted_ids\x18\x01 \x03(\x0b\x32%.private_membership.DoublyEncryptedId\x12S\n\x19hashed_buckets_parameters\x18\x02 \x01(\x0b\x32\x30.private_membership.rlwe.HashedBucketsParameters\x12Y\n\x1c\x65ncrypted_buckets_parameters\x18\x03 \x01(\x0b\x32\x33.private_membership.rlwe.EncryptedBucketsParameters\x12@\n\x0frlwe_parameters\x18\x04 \x01(\x0b\x32\'.private_membership.rlwe.RlweParameters\x12\x13\n\x0bkey_version\x18\x05 \x01(\x03\"\xb6\x01\n!PrivateMembershipRlweQueryRequest\x12\x44\n\x07queries\x18\x01 \x03(\x0b\x32\x33.private_membership.rlwe.PrivateMembershipRlweQuery\x12\x36\n\x08use_case\x18\x02 \x01(\x0e\x32$.private_membership.rlwe.RlweUseCase\x12\x13\n\x0bkey_version\x18\x03 \x01(\x03\"v\n\"PrivateMembershipRlweQueryResponse\x12P\n\rpir_responses\x18\x01 \x03(\x0b\x32\x39.private_membership.rlwe.PrivateMembershipRlwePirResponse\"A\n\x0fRlwePlaintextId\x12\x18\n\x10non_sensitive_id\x18\x01 \x01(\t\x12\x14\n\x0csensitive_id\x18\x02 \x01(\t\"|\n\x17HashedBucketsParameters\x12\x1f\n\x17hashed_bucket_id_length\x18\x01 \x01(\x05\x12@\n\x1anon_sensitive_id_hash_type\x18\x02 \x01(\x0e\x32\x1c.private_membership.HashType\"\x8d\x01\n\x1a\x45ncryptedBucketsParameters\x12\"\n\x1a\x65ncrypted_bucket_id_length\x18\x01 \x01(\x05\x12K\n\x16sensitive_id_hash_type\x18\x02 \x01(\x0e\x32+.private_membership.EncryptedBucketHashType\"\x95\x01\n\x0eRlweParameters\x12\x31\n\x07modulus\x18\x01 \x03(\x0b\x32 .private_membership.rlwe.Uint128\x12\x12\n\nlog_degree\x18\x02 \x01(\x05\x12\r\n\x05log_t\x18\x03 \x01(\x05\x12\x10\n\x08variance\x18\x04 \x01(\x05\x12\x1b\n\x13levels_of_recursion\x18\x05 \x01(\x05\"!\n\x07Uint128\x12\n\n\x02lo\x18\x01 \x01(\x04\x12\n\n\x02hi\x18\x02 \x01(\x04\"\x92\x02\n\x1aPrivateMembershipRlweQuery\x12\x1c\n\x14queried_encrypted_id\x18\x01 \x01(\x0c\x12\x38\n\x0bpir_request\x18\x02 \x01(\x0b\x32#.private_membership.rlwe.PirRequest\x12\\\n\x10hashed_bucket_id\x18\x03 \x01(\x0b\x32\x42.private_membership.rlwe.PrivateMembershipRlweQuery.HashedBucketId\x1a>\n\x0eHashedBucketId\x12\x18\n\x10hashed_bucket_id\x18\x01 \x01(\x0c\x12\x12\n\nbit_length\x18\x02 \x01(\x05\"|\n PrivateMembershipRlwePirResponse\x12\x1c\n\x14queried_encrypted_id\x18\x01 \x01(\x0c\x12:\n\x0cpir_response\x18\x02 \x01(\x0b\x32$.private_membership.rlwe.PirResponse\"\xc3\x04\n\nPirRequest\x12.\n\x07request\x18\x01 \x03(\x0b\x32\x1d.rlwe.SerializedNttPolynomial\x12M\n\x0f\x63ompact_request\x18\x03 \x01(\x0b\x32\x32.private_membership.rlwe.PirRequest.CompactRequestH\x00\x12O\n\x10\x65xpanded_request\x18\x04 \x01(\x0b\x32\x33.private_membership.rlwe.PirRequest.ExpandedRequestH\x00\x12\x11\n\tprng_seed\x18\x02 \x01(\x0c\x1a\xf3\x01\n\x0f\x45xpandedRequest\x12j\n\x0b\x63iphertexts\x18\x01 \x03(\x0b\x32U.private_membership.rlwe.PirRequest.ExpandedRequest.SerializedSymmetricRlweCiphertext\x1at\n!SerializedSymmetricRlweCiphertext\x12@\n\nciphertext\x18\x01 \x01(\x0b\x32\'.rlwe.SerializedSymmetricRlweCiphertextH\x00\x88\x01\x01\x42\r\n\x0b_ciphertext\x1a\x44\n\x0e\x43ompactRequest\x12\x32\n\x0b\x63iphertexts\x18\x01 \x03(\x0b\x32\x1d.rlwe.SerializedNttPolynomialB\x16\n\x14sharded_request_type\"f\n\x0bPirResponse\x12\x39\n\x08response\x18\x01 \x03(\x0b\x32\'.rlwe.SerializedSymmetricRlweCiphertext\x12\x1c\n\x14plaintext_entry_size\x18\x02 \x01(\x05\"\xef\x01\n\x0f\x45ncryptedBucket\x12_\n\x18\x65ncrypted_id_value_pairs\x18\x01 \x03(\x0b\x32=.private_membership.rlwe.EncryptedBucket.EncryptedIdValuePair\x1a{\n\x14\x45ncryptedIdValuePair\x12\x14\n\x0c\x65ncrypted_id\x18\x01 \x01(\x0c\x12\x17\n\x0f\x65ncrypted_value\x18\x02 \x01(\x0c\x12\x34\n\x02id\x18\x03 \x01(\x0b\x32(.private_membership.rlwe.RlwePlaintextId\"\xa2\x02\n\x17RlweMembershipResponses\x12\x66\n\x14membership_responses\x18\x01 \x03(\x0b\x32H.private_membership.rlwe.RlweMembershipResponses.MembershipResponseEntry\x1a\x9e\x01\n\x17MembershipResponseEntry\x12>\n\x0cplaintext_id\x18\x01 \x01(\x0b\x32(.private_membership.rlwe.RlwePlaintextId\x12\x43\n\x13membership_response\x18\x02 \x01(\x0b\x32&.private_membership.MembershipResponse*\xaf\x04\n\x0bRlweUseCase\x12\x1b\n\x17RLWE_USE_CASE_UNDEFINED\x10\x00\x12\x11\n\rTEST_USE_CASE\x10\x01\x12\x12\n\x0eTEST_USE_CASE2\x10\x02\x12\x12\n\x0eTEST_USE_CASE3\x10\x03\x12\x12\n\x0e\x45MPTY_USE_CASE\x10\x16\x12\x15\n\x11\x43ROS_DEVICE_STATE\x10\x05\x12\x1d\n\x19\x43ROS_DEVICE_STATE_UNIFIED\x10\x17\x12#\n\x1b\x43ROS_DEVICE_SECONDARY_STATE\x10\x0c\x1a\x02\x08\x01\x12 \n\x18\x43ROS_DEVICE_STATE_BACKUP\x10\x15\x1a\x02\x08\x01\x12\x16\n\x12\x43ROS_FRESNEL_DAILY\x10\r\x12\x18\n\x14\x43ROS_FRESNEL_MONTHLY\x10\x0e\x12\x1d\n\x19\x43ROS_FRESNEL_FIRST_ACTIVE\x10\x0f\x12\x1c\n\x18\x43ROS_FRESNEL_7DAY_ACTIVE\x10\x10\x12\x1d\n\x19\x43ROS_FRESNEL_28DAY_ACTIVE\x10\x11\x12%\n!CROS_FRESNEL_CHURN_MONTHLY_COHORT\x10\x13\x12*\n&CROS_FRESNEL_CHURN_MONTHLY_OBSERVATION\x10\x14\x12\x11\n\rCROS_SIM_LOCK\x10\x12\x12\x19\n\x15\x43ROS_SIM_LOCK_DEVMODE\x10\x18\"\x04\x08\x04\x10\x04\"\x04\x08\x06\x10\x06\"\x04\x08\x07\x10\x07\"\x04\x08\x08\x10\x08\"\x04\x08\t\x10\t\"\x04\x08\n\x10\n\"\x04\x08\x0b\x10\x0b\x42(H\x03Z$github.com/google/private-membershipb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'private_membership_rlwe_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003Z$github.com/google/private-membership'
  _RLWEUSECASE.values_by_name["CROS_DEVICE_SECONDARY_STATE"]._options = None
  _RLWEUSECASE.values_by_name["CROS_DEVICE_SECONDARY_STATE"]._serialized_options = b'\010\001'
  _RLWEUSECASE.values_by_name["CROS_DEVICE_STATE_BACKUP"]._options = None
  _RLWEUSECASE.values_by_name["CROS_DEVICE_STATE_BACKUP"]._serialized_options = b'\010\001'
  _RLWEUSECASE._serialized_start=3044
  _RLWEUSECASE._serialized_end=3603
  _PRIVATEMEMBERSHIPRLWEOPRFREQUEST._serialized_start=105
  _PRIVATEMEMBERSHIPRLWEOPRFREQUEST._serialized_end=218
  _PRIVATEMEMBERSHIPRLWEOPRFRESPONSE._serialized_start=221
  _PRIVATEMEMBERSHIPRLWEOPRFRESPONSE._serialized_end=588
  _PRIVATEMEMBERSHIPRLWEQUERYREQUEST._serialized_start=591
  _PRIVATEMEMBERSHIPRLWEQUERYREQUEST._serialized_end=773
  _PRIVATEMEMBERSHIPRLWEQUERYRESPONSE._serialized_start=775
  _PRIVATEMEMBERSHIPRLWEQUERYRESPONSE._serialized_end=893
  _RLWEPLAINTEXTID._serialized_start=895
  _RLWEPLAINTEXTID._serialized_end=960
  _HASHEDBUCKETSPARAMETERS._serialized_start=962
  _HASHEDBUCKETSPARAMETERS._serialized_end=1086
  _ENCRYPTEDBUCKETSPARAMETERS._serialized_start=1089
  _ENCRYPTEDBUCKETSPARAMETERS._serialized_end=1230
  _RLWEPARAMETERS._serialized_start=1233
  _RLWEPARAMETERS._serialized_end=1382
  _UINT128._serialized_start=1384
  _UINT128._serialized_end=1417
  _PRIVATEMEMBERSHIPRLWEQUERY._serialized_start=1420
  _PRIVATEMEMBERSHIPRLWEQUERY._serialized_end=1694
  _PRIVATEMEMBERSHIPRLWEQUERY_HASHEDBUCKETID._serialized_start=1632
  _PRIVATEMEMBERSHIPRLWEQUERY_HASHEDBUCKETID._serialized_end=1694
  _PRIVATEMEMBERSHIPRLWEPIRRESPONSE._serialized_start=1696
  _PRIVATEMEMBERSHIPRLWEPIRRESPONSE._serialized_end=1820
  _PIRREQUEST._serialized_start=1823
  _PIRREQUEST._serialized_end=2402
  _PIRREQUEST_EXPANDEDREQUEST._serialized_start=2065
  _PIRREQUEST_EXPANDEDREQUEST._serialized_end=2308
  _PIRREQUEST_EXPANDEDREQUEST_SERIALIZEDSYMMETRICRLWECIPHERTEXT._serialized_start=2192
  _PIRREQUEST_EXPANDEDREQUEST_SERIALIZEDSYMMETRICRLWECIPHERTEXT._serialized_end=2308
  _PIRREQUEST_COMPACTREQUEST._serialized_start=2310
  _PIRREQUEST_COMPACTREQUEST._serialized_end=2378
  _PIRRESPONSE._serialized_start=2404
  _PIRRESPONSE._serialized_end=2506
  _ENCRYPTEDBUCKET._serialized_start=2509
  _ENCRYPTEDBUCKET._serialized_end=2748
  _ENCRYPTEDBUCKET_ENCRYPTEDIDVALUEPAIR._serialized_start=2625
  _ENCRYPTEDBUCKET_ENCRYPTEDIDVALUEPAIR._serialized_end=2748
  _RLWEMEMBERSHIPRESPONSES._serialized_start=2751
  _RLWEMEMBERSHIPRESPONSES._serialized_end=3041
  _RLWEMEMBERSHIPRESPONSES_MEMBERSHIPRESPONSEENTRY._serialized_start=2883
  _RLWEMEMBERSHIPRESPONSES_MEMBERSHIPRESPONSEENTRY._serialized_end=3041
# @@protoc_insertion_point(module_scope)