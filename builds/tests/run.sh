#!/bin/bash

set -e

MULT=${MULT:-1}
TESTDIR="$(dirname $0)"
HOSTNAME="${1:-builds.roflmao.space}"

which expect >/dev/null || exit 1
which virt-install >/dev/null || exit 2

{
trap "virsh pool-refresh default" EXIT

iso=builds/amd64/systemd/latest-livecd-stage3-amd64-systemd.iso
test -f $iso && timeout $((10 * $MULT))m expect -f "$TESTDIR"/livecd.tcl $iso

iso=builds/amd64/minimal/latest-livecd-stage3-amd64-minimal.iso
if test -f $iso; then
	timeout $((10 * $MULT))m expect -f "$TESTDIR"/livecd.tcl $iso
	timeout $((5 * $MULT))m expect -f "$TESTDIR"/router.tcl ${HOSTNAME}
fi

iso=builds/amd64/minimal/latest-systemd-amd64-minimal.iso
test -f $iso && timeout $(( 5 * $MULT))m expect -f "$TESTDIR"/distkernel.tcl $iso roflmaOS_systemd

iso=builds/amd64/plasma/latest-livecd-stage3-amd64-plasma.iso
test -f $iso && timeout $((15 * $MULT))m expect -f "$TESTDIR"/livecd.tcl $iso --memory 1024 --disk size=10

iso=builds/amd64/duet/latest-livecd-stage3-amd64-duet.iso
test -f $iso && timeout $((30 * $MULT))m expect -f "$TESTDIR"/duet.tcl $iso roflmaOS_duet sddm --memory 2048 --disk size=30

iso=builds/amd64/gnome/latest-livecd-stage3-amd64-gnome.iso
test -f $iso && timeout $((30 * $MULT))m expect -f "$TESTDIR"/duet.tcl $iso roflmaOS_gnome gdm --memory 2048 --disk size=30

} |& less -S +F --exit-follow-on-close
