#!/bin/bash

base_dir="$(pwd)"
proto_dir="$base_dir/proto"
interfaces_dir="$base_dir/interfaces"

rm -rf $interfaces_dir
mkdir -p $interfaces_dir
protoc -I $proto_dir $proto_dir/* --python_out=$interfaces_dir
#force relative import because protoc is braindead 
#https://github.com/protocolbuffers/protobuf/issues/1491
sed -i 's/^import/from \. import/' $interfaces_dir/*