profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

livecd/packages:
	dev-util/cmake
	dev-util/ninja
	gui-wm/sway
	sys-apps/usbutils
	sys-boot/efibootmgr
	sys-firmware/intel-microcode
	sys-fs/btrfs-progs
	sys-fs/dosfstools
	sys-kernel/linux-firmware
	x11-libs/libXtst
	x11-terms/alacritty
