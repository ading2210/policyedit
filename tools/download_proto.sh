#!/bin/bash

base_dir="$(pwd)"
proto_dir="$base_dir/proto"
mkdir -p $proto_dir

tag="main"
proto_paths=(
  "components/policy/proto/chrome_device_policy.proto"
  "components/policy/proto/policy_common_definitions.proto"
  "components/policy/proto/device_management_backend.proto"
  "third_party/private_membership/src/private_membership_rlwe.proto"
  "third_party/private_membership/src/private_membership.proto"
  "third_party/shell-encryption/src/serialization.proto"
)

for path in "${proto_paths[@]}"; do
  filename="$(basename "$path")"
  url="https://chromium.googlesource.com/chromium/src/+/refs/heads/$tag/$path?format=TEXT"
  echo "downloading $filename"
  curl "$url" | base64 -d > "$proto_dir/$filename"
  #sed -i 's/import "/import "generated\//' "$base_dir/proto/$filename"
done