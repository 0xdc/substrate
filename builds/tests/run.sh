#!/bin/bash

set -e

TESTDIR="$(dirname $0)"
HOSTNAME="${1:-builds.roflmao.space}"

which expect >/dev/null || exit 1

i=systemd
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
test -f $iso && timeout 10m expect -f "$TESTDIR"/livecd.ex $iso

i=minimal
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
if test -f $iso; then
	timeout 10m expect -f "$TESTDIR"/livecd.ex $iso --extra-args "real_init=/usr/lib/systemd/systemd"
	timeout 5m expect -f "$TESTDIR"/router.ex ${HOSTNAME}
fi

i=plasma
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/livecd.ex $iso --memory 1024 --disk size=10

i=duet
iso=builds/amd64/$i/latest-livecd-stage3-amd64-$i.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/$i.ex $iso --memory 2048 --disk size=20
