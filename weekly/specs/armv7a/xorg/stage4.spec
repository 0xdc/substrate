subarch: armv7a_hardfp
target: stage4
version_stamp: xorg-@latest@
rel_type: xorg
profile: default/linux/arm/13.0/armv7a
snapshot: @latest@
source_subpath: armv7a/default/stage4-armv7a_hardfp-latest
portage_confdir: @REPO_DIR@/portage/xorg

stage4/use:
	ipv6

stage4/packages:
	net-wireless/iw
	net-wireless/rfkill
	net-wireless/wpa_supplicant
	sys-kernel/linux-firmware
	x11-base/xorg-server
	x11-misc/dmenu
	x11-terms/st
	x11-wm/dwm

stage4/empty:
	/root/.ccache
	/tmp
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	/usr/portage
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
