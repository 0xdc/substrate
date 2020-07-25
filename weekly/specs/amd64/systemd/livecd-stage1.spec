profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

livecd/packages:
	sys-apps/memtest86+
	sys-boot/shim
	sys-boot/syslinux
	sys-firmware/intel-microcode
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-fs/squashfs-tools
