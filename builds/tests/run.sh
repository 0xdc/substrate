#!/bin/bash

set -e

TESTDIR="$(dirname $0)"

which expect >/dev/null || exit 1

for i in systemd minimal; do
	iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
	test -f $iso && timeout 10m expect -f "$TESTDIR"/livecd.ex $iso
done

test -f $iso && timeout 5m expect -f "$TESTDIR"/router.ex

i=plasma
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/livecd.ex $iso --memory 1024 --disk size=10

i=duet
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/$i.ex $iso --memory 1024 --disk size=10
