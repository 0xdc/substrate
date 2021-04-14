#!/bin/bash

set -e

DISK=${1?Need install disk (and other systemd-repart options}

# the genkernel initramfs has some issues with switch_root
coproc dracut -f /tmp/initramfs-$(uname -r).img

systemd-repart --empty=allow --definitions $(dirname $0) "$@"

cmdline=(
	# since we kexec, we cannot use discoverable partitions
	# cannot use encrypted root unless we discover the UUID
	root=PARTLABEL=root-x86-64

	# save the console tty
	$(egrep -o 'console=[^ ]*' /proc/cmdline)

	systemd.volatile=overlay
)

kexec_args=(
	--load
	--initrd /tmp/initramfs-$(uname -r).img

	# we need the kernel from the cdrom
	/mnt/cdrom/boot/gentoo
)

wait

# args should be separate words, but the cmdline should be one argument
kexec "${kexec_args[@]}" --command-line "${cmdline[*]}"

echo
echo "Rootfs installed, ready for kexec!"
echo "# systemctl kexec"
