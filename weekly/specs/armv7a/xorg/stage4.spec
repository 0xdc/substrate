profile: default/linux/arm/17.0/armv7a
source_subpath: armv7a/hardfp/stage4-armv7a_hardfp-latest
portage_confdir: @REPO_DIR@/confdirs/xorg

stage4/packages:
	net-wireless/iw
	net-wireless/wpa_supplicant
	sys-kernel/linux-firmware
	x11-base/xorg-server
	x11-misc/dmenu
	x11-terms/st
	x11-wm/dwm

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
