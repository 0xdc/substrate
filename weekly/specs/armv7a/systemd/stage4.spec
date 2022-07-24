profile: 0xdc:arm
repos: @REPO_DIR@/overlay
source_subpath: armv7a/systemd/stage3-armv7a_hardfp-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/vboot

stage4/packages:
	app-editors/vim
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-vcs/git
	sys-devel/distcc
	sys-fs/cryptsetup
	sys-fs/dosfstools
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/root_overlays/base
stage4/fsscripts: @REPO_DIR@/fsscripts/livecd

stage4/unmerge:
	app-editors/nano
