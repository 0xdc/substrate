profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/embedded

embedded/packages:
	app-arch/tar
	app-crypt/gnupg
	app-editors/vim
	dev-python/pychroot
	net-misc/casync
	net-misc/openssh
	net-misc/rsync
	net-wireless/wpa_supplicant
	sys-apps/arch-chroot
	sys-apps/findutils
	sys-apps/kexec-tools
	sys-apps/smartmontools
	sys-apps/util-linux
	sys-boot/efibootmgr
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-kernel/dracut
