version_stamp: @latest@
profile: default/linux/arm/17.0/armv7a
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-embedded/u-boot-tools
	dev-vcs/git
	sys-apps/dtc
	sys-devel/bc
	sys-devel/distcc
	sys-fs/dosfstools

stage4/root_overlay: @REPO_DIR@/root_overlays/ella

stage4/rcadd:
	busybox-ntpd|default
	net.eth0|default
	sshd|default

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
