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

test -L /dev/root || ln -s "${root}" /dev/root
systemd-repart --definitions $(dirname $0) --factory-reset=yes "$@"

cmdline=(
	$(egrep -o 'console=[^ ]*' /proc/cmdline || true)
	$(egrep -o 'systemd.firstboot=[^ ]*' /proc/cmdline || true)
	i915.enable_fbc=1
	i915.enable_guc=2
	systemd.volatile=yes
	fbcon=rotate:1
	systemd.wants=NetworkManager.service
	systemd.wants=bluetooth.service
	systemd.wants=thermald.service
	systemd.wants=sddm.service
	systemd.wants=sysstat-collect.timer
	systemd.wants=vnstatd.service
)

test -d /etc/kernel || mkdir -p /etc/kernel
echo "${cmdline[@]}" > /etc/kernel/cmdline

echo

if mountpoint -q /boot; then
	bootctl is-installed >/dev/null || bootctl install
	test -d /boot/$(systemd-id128 machine-id) || mkdir -p /boot/$(systemd-id128 machine-id)

	for cdrom in /run/media/system/ISOIMAGE /mnt/cdrom; do
		test -f ${cdrom}/boot/gentoo || continue
		kernel-install add $(uname -r) ${cdrom}/boot/gentoo

		echo "Rootfs installed, ready for reboot!"
		echo "# systemctl reboot"

		exit 0
	done

	echo "No kernel found. Do not reboot." 2>/dev/null
	exit 1
else
	echo "No ESP mounted on /boot. No changes." 2>/dev/null
	exit 2
fi
