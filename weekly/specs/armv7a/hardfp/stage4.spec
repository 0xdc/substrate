subarch: armv7a_hardfp
target: stage4
version_stamp: @latest@
rel_type: default
profile: default/linux/arm/13.0/armv7a
snapshot: @latest@
source_subpath: armv7a/default/stage3-armv7a_hardfp-latest

stage4/use:
	bindist
	ipv6

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-vcs/git

stage4/root_overlay: @REPO_DIR@/overlays/base

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
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
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
