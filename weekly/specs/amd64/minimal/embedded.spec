profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest

embedded/packages:
	app-arch/tar
	app-crypt/gnupg
	net-misc/casync[-fuse]
	net-misc/rsync
	net-wireless/wpa_supplicant
	sys-apps/systemd[cryptsetup,gnuefi,repart]
	sys-apps/shadow
	sys-apps/util-linux
	sys-fs/btrfs-progs
	sys-fs/dosfstools
