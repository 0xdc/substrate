#!/bin/bash

set -e

MULT=${MULT:-1}
TESTDIR="$(dirname $0)"
HOSTNAME="${1:-builds.roflmao.space}"

which expect >/dev/null || exit 1
which virt-install >/dev/null || exit 2

trap "virsh pool-refresh default" EXIT

iso=builds/amd64/systemd/latest-livecd-stage3-amd64-systemd.iso
test -f $iso && timeout $((10 * $MULT))m expect -f "$TESTDIR"/livecd.ex $iso

iso=builds/amd64/minimal/latest-livecd-stage3-amd64-minimal.iso
if test -f $iso; then
	timeout $((10 * $MULT))m expect -f "$TESTDIR"/livecd.ex $iso --extra-args "real_init=/usr/lib/systemd/systemd"
	timeout $((5 * $MULT))m expect -f "$TESTDIR"/router.ex ${HOSTNAME}
fi

iso=builds/amd64/plasma/latest-livecd-stage3-amd64-plasma.iso
test -f $iso && timeout $((15 * $MULT))m expect -f "$TESTDIR"/livecd.ex $iso --memory 1024 --disk size=10

iso=builds/amd64/duet/latest-livecd-stage3-amd64-duet.iso
test -f $iso && timeout $((15 * $MULT))m expect -f "$TESTDIR"/duet.ex $iso --memory 2048 --disk size=30

iso=builds/amd64/gnome/latest-livecd-stage3-amd64-gnome.iso
test -f $iso && timeout $((15 * $MULT))m expect -f "$TESTDIR"/gnome.ex $iso --memory 2048 --disk size=30
