#!/bin/bash

base_dir="$(pwd)"
proto_dir="$base_dir/proto"
mkdir -p $proto_dir

tag="main"
repo="src"
proto_paths=(
  "components/policy/proto/chrome_device_policy.proto"
  "components/policy/proto/policy_common_definitions.proto"
  "components/policy/proto/device_management_backend.proto"
  "third_party/private_membership/src/private_membership_rlwe.proto"
  "third_party/private_membership/src/private_membership.proto"
  "third_party/shell-encryption/src/serialization.proto"
)

download_file() {
  local path="$1"
  local filename="$(basename "$path")"
  local url="https://chromium.googlesource.com/chromium/$repo/+/refs/heads/$tag/$path?format=TEXT"
  echo "downloading $filename"
  curl "$url" | base64 -d > "$proto_dir/$filename"
}

for path in "${proto_paths[@]}"; do
  download_file "$path"
done

#download from different repository 
repo="src/out"
download_file "chromeos-Debug/gen/components/policy/proto/cloud_policy.proto"
