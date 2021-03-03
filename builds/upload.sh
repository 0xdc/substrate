#!/bin/bash

set -e

which openstack
test "$OS_CLOUD" = "envvars" || (test -f /etc/openstack/clouds.yaml || test -f ~/.config/openstack/clouds.yaml )

pushd $(dirname $0)

for dir in */*/*/; do
	pushd $dir
	test -f SHA256SUMS || sha256sum $(find * -type f -name '*stage[134]-*' -o -name '*embedded-*') | tee SHA256SUMS
	popd
done

openstack object create builds $(find */*/*/ */*/*.txt -type f -name '*stage[34]-*' -o -name '*embedded-*' -o -name SHA256SUMS)
