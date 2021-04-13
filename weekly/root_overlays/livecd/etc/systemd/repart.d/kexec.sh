#!/bin/bash

set -e

DISK=${1?Need install disk (and other systemd-repart options}

# the genkernel initramfs has some issues with switch_root
coproc dracut -f /tmp/initramfs-$(uname -r).img

systemd-repart --empty=allow --definitions $(dirname $0) "$@"

cmdline=(
	rw
	quiet

	# since we kexec, we cannot use discoverable partitions
	# cannot use encrypted root unless we discover the UUID
	root=LABEL=root-x86-64

	# save the console tty
	$(egrep -o 'console=[^ ]*' /proc/cmdline)
)

kexec_args=(
	--load
	--initrd /tmp/initramfs-$(uname -r).img

	/mnt/cdrom/boot/gentoo
)

wait

# args should be separate words, but the cmdline should be one argument
kexec "${kexec_args[@]}" --command-line "${cmdline[*]}"
