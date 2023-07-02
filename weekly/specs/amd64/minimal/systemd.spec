profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/embedded

boot/kernel: gentoo
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64
boot/kernel/gentoo/console: ttyS0

embedded/iso: roflmaOS-minimal-systemd-@latest@.iso
embedded/fstype: btrfs
embedded/fsops: -no-recovery -comp xz -Xbcj x86
embedded/fsscript: @REPO_DIR@/fsscripts/livecd
embedded/root_overlay: @REPO_DIR@/root_overlays/livecd

embedded/packages:
	app-arch/tar
	app-crypt/gnupg
	app-editors/vim
	net-misc/casync
	net-misc/openssh
	net-misc/rsync
	net-wireless/wpa_supplicant
	sys-apps/findutils
	sys-apps/kexec-tools
	sys-apps/smartmontools
	sys-apps/util-linux
	sys-boot/efibootmgr
	sys-fs/btrfs-progs
	sys-fs/dosfstools
