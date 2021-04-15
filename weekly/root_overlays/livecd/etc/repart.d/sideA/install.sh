#!/bin/bash

set -e

DISK=${1?Need install disk (and other systemd-repart options}

root_disk=$(egrep -o 'root=[^ ]+' /proc/cmdline)
case "$root_disk" in
root=ID=*)
	root=/dev/disk/by-id/${root_disk#root=ID=}
	;;
root=LABEL=*)
	root=/dev/disk/by-label/${root_disk#root=LABEL=}
	;;
root=PARTLABEL=*)
	root=/dev/disk/by-partlabel/${root_disk#root=PARTLABEL=}
	;;
root=PARTUUID=*)
	root=/dev/disk/by-partuuid/${root_disk#root=PARTUUID=}
	;;
root=PATH=*)
	root=/dev/disk/by-path/${root_disk#root=PATH=}
	;;
root=UUID=*)
	root=/dev/disk/by-uuid/${root_disk#root=UUID=}
	;;
root=/dev/*)
	root=${root_disk#root=}
	;;
esac

sed -i "/^CopyBlocks=/s:/dev/root:$root:" $(dirname $0)/20-root.conf
systemd-repart --definitions $(dirname $0) --factory-reset=yes "$@"

cmdline=(
	$(egrep -o 'console=[^ ]*' /proc/cmdline)
	root=gpt-auto
	systemd.volatile=overlay
)

test -d /etc/kernel || mkdir -p /etc/kernel
echo "${cmdline[@]}" > /etc/kernel/cmdline

if bootctl is-installed >/dev/null; then
	echo
	echo "Rootfs installed, ready for reboot!"
	echo "# systemctl reboot"
elif mountpoint -q /boot; then
	bootctl install
	test -d /boot/$(systemd-id128 machine-id) || mkdir -p /boot/$(systemd-id128 machine-id)

	# TODO: find and install a kernel
	#kernel-install add $(uname -r) ...
else
	echo
	echo "No bootloader or ESP found." 2>/dev/null
	exit 1
fi
