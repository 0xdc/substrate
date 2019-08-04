profile: default/linux/amd64/17.0/desktop/plasma/systemd
portage_confdir: @REPO_DIR@/confdirs/plasma
source_subpath: amd64/plasma/stage3-amd64-plasma-latest

stage4/packages:
	app-admin/ansible
	app-editors/vim
	app-emulation/virt-manager
	app-eselect/eselect-repository
	app-shells/bash-completion
	dev-vcs/git
	kde-plasma/plasma-meta
	kde-apps/dolphin
	kde-apps/konsole
	net-libs/nodejs
	sys-apps/iproute2
	sys-kernel/dracut
	sys-process/htop
	www-client/firefox

stage4/root_overlay: @REPO_DIR@/root_overlays/plasma

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
