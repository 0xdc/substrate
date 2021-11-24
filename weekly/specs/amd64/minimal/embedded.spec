profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/mergeusr/stage3-amd64-mergeusr-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/embedded

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
	sys-devel/gcc
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-kernel/dracut
