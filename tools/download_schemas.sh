#!/bin/bash

base_dir="$(pwd)"
schema_dir="$base_dir/schema"
mkdir -p $schema_dir

tag="main"
schema_paths=(
  "components/policy/resources/templates/device_policy_proto_map.yaml"
  "components/policy/resources/templates/legacy_device_policy_proto_map.yaml"
)

for path in "${schema_paths[@]}"; do
  filename="$(basename "$path")"
  url="https://chromium.googlesource.com/chromium/src/+/refs/heads/$tag/$path?format=TEXT"
  echo "downloading $filename"
  curl "$url" | base64 -d > "$schema_dir/$filename"
done