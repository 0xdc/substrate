profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest

embedded/packages:
	app-arch/tar
	app-crypt/gnupg[usb]
	app-editors/vim
	net-misc/casync[-fuse]
	net-misc/openssh[security-key]
	net-misc/rsync
	net-wireless/wpa_supplicant
	sys-apps/shadow
	sys-apps/smartmontools[-daemon]
	sys-apps/systemd[cryptsetup,gnuefi,repart]
	sys-apps/util-linux
	sys-boot/efibootmgr
	sys-devel/gcc
	sys-fs/btrfs-progs
	sys-fs/dosfstools
