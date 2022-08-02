version_stamp: @latest@
profile: default/linux/arm/17.0/armv7a
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
portage_confdir: @REPO_DIR@/confdirs/vboot

stage4/packages:
	app-editors/vim
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-vcs/git
	sys-apps/busybox
	sys-devel/distcc
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/root_overlays/base

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
