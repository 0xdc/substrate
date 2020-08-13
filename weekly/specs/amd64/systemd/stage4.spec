profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/base

stage4/packages:
	app-admin/ansible
	app-editors/vim
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-vcs/git
	net-libs/nodejs
	sys-apps/iproute2
	net-firewall/nftables
	sys-devel/bc
	sys-kernel/dracut
	sys-process/htop

stage4/root_overlay: @REPO_DIR@/root_overlays/base

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
