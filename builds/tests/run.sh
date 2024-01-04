#!/bin/bash

set -e

TESTDIR="$(dirname $0)"
HOSTNAME="${1:-builds.roflmao.space}"

which expect >/dev/null || exit 1
which virt-install >/dev/null || exit 2

trap "virsh pool-refresh default" EXIT

iso=builds/amd64/systemd/latest-livecd-stage3-amd64-systemd.iso
test -f $iso && timeout 10m expect -f "$TESTDIR"/livecd.ex $iso

iso=builds/amd64/minimal/latest-livecd-stage3-amd64-minimal.iso
if test -f $iso; then
	timeout 10m expect -f "$TESTDIR"/livecd.ex $iso --extra-args "real_init=/usr/lib/systemd/systemd"
	timeout 5m expect -f "$TESTDIR"/router.ex ${HOSTNAME}
fi

iso=builds/amd64/plasma/latest-livecd-stage3-amd64-plasma.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/livecd.ex $iso --memory 1024 --disk size=10

iso=builds/amd64/duet/latest-livecd-stage3-amd64-duet.iso
test -f $iso && timeout 15m expect -f "$TESTDIR"/duet.ex $iso --memory 2048 --disk size=30
