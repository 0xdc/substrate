#!/bin/bash

set -e

which openstack
test "$OS_CLOUD" = "envvars" || (test -f /etc/openstack/clouds.yaml || test -f ~/.config/openstack/clouds.yaml )

pushd $(dirname $0)

openstack object create builds $(find */*/*/ */*/*.txt -type f -name '*stage[34]-*' -o -name '*embedded-*')
