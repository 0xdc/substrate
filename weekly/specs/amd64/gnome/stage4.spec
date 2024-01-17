profile: default/linux/amd64/17.1/desktop/gnome/systemd/merged-usr
source_subpath: amd64/gnome/stage3-amd64-gnome-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/gnome/stage4

stage4/use:
	-gnome-online-accounts
	ibus

stage4/packages:
	app-admin/ansible
	app-editors/vim
	app-eselect/eselect-repository
	app-i18n/ibus-anthy
	app-i18n/imsettings
	app-shells/bash-completion
	dev-vcs/git
	gnome-base/gnome-light
	media-fonts/droid
	net-firewall/nftables
	sys-apps/iproute2
	sys-kernel/dracut
	sys-process/htop
	www-client/firefox

#stage4/root_overlay: @REPO_DIR@/root_overlays/gnome

stage4/unmerge:
	app-editors/nano
