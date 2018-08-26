subarch: armv7a_hardfp
target: stage4
version_stamp: @latest@
rel_type: hardfp
profile: default/linux/arm/13.0/armv7a
snapshot: @latest@
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
portage_confdir: @REPO_DIR@/portage/vboot

stage4/use:
	bindist
	ipv6

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-embedded/u-boot-tools
	dev-util/catalyst
	dev-vcs/git
	sys-apps/dtc
	sys-boot/vboot-utils
	sys-devel/bc
	sys-devel/distcc
	sys-fs/dosfstools
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/overlays/base

stage4/unmerge:
	app-editors/nano

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
