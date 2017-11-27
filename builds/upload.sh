#!/bin/bash

pushd $(dirname $0)

openstack object create builds $(find */*/*/ */*/*.txt -type f)
