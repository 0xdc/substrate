version_stamp: @latest@
target:stage4
profile: 0xdc:arm
repos: @REPO_DIR@/overlay
source_subpath: armv7a/systemd/stage3-armv7a_hardfp-systemd-latest

stage4/packages:
	app-editors/vim
	app-eselect/eselect-repository
	dev-vcs/git
	sys-devel/distcc
	sys-fs/dosfstools

stage4/root_overlay: @REPO_DIR@/root_overlays/ella
stage4/fsscript: @REPO_DIR@/fsscripts/livecd
