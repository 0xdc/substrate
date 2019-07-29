profile: default/linux/amd64/17.0/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/base

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-util/catalyst
	dev-vcs/git
	sys-apps/iproute2
	sys-devel/distcc
	sys-kernel/dracut
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/root_overlays/base

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
