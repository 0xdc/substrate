profile: 0xdc:arm/desktop/chromebook
repos: @REPO_DIR@/overlay
source_subpath: armv7a/systemd/stage4-armv7a_hardfp-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/xorg

stage4/packages:
	net-wireless/iw
	net-wireless/wpa_supplicant
	sys-kernel/linux-firmware
	x11-base/xorg-server
	x11-misc/dmenu
	x11-terms/st
	x11-wm/dwm

stage4/fsscript: @REPO_DIR@/fsscripts/livecd
