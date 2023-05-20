#!/bin/bash

set -e

DISK=${1?Need install disk (and other systemd-repart options}

if mountpoint -q /mnt/cdrom; then
	cdrom=/mnt/cdrom
elif mountpoint -q /run/media/system/ISOIMAGE; then
	cdrom=/run/media/system/ISOIMAGE
fi

coproc initrd ( dracut -q -f /tmp/initramfs-$(uname -r).img )

sed -i '$aCopyBlocks='"$cdrom/image.squashfs" $(dirname $0)/30-sideB.conf
systemd-repart --empty=allow --definitions $(dirname $0) --factory-reset=yes "$@"

cmdline=(
	# save the console tty
	$(egrep -o 'console=[^ ]*' /proc/cmdline || true)

	# keep a copy of firstboot if the host system has it
	# we're going to be updating a system that has homes
	$(egrep -o 'systemd.firstboot=[^ ]*' /proc/cmdline || true)

	# since we kexec, we cannot use discoverable partitions
	# cannot use encrypted root unless we discover the UUID
	root=PARTLABEL=sideB

	systemd.volatile=overlay
	fbcon=rotate:1
)

kexec_args=(
	--load
	--initrd /tmp/initramfs-$(uname -r).img

	# we need the kernel from the cdrom
	${cdrom}/boot/gentoo
)

wait

# args should be separate words, but the cmdline should be one argument
kexec "${kexec_args[@]}" --command-line "${cmdline[*]}"

echo
echo "Rootfs installed, ready for kexec!"
echo "# systemctl kexec"
