profile: default/linux/amd64/17.1/desktop/plasma/systemd/merged-usr
portage_confdir: @REPO_DIR@/confdirs/plasma
source_subpath: amd64/plasma/stage3-amd64-plasma-latest

stage4/use:
	ibus

stage4/packages:
	app-admin/ansible
	app-editors/vim
	app-eselect/eselect-repository
	app-i18n/ibus-anthy
	app-i18n/imsettings
	app-shells/bash-completion
	dev-vcs/git
	kde-plasma/plasma-desktop
	kde-plasma/plasma-pa
	kde-plasma/systemsettings
	kde-apps/ark
	kde-apps/dolphin
	kde-apps/konsole
	media-fonts/droid
	net-firewall/nftables
	sys-apps/iproute2
	sys-kernel/dracut
	sys-process/htop
	www-client/firefox
	x11-misc/sddm

stage4/root_overlay: @REPO_DIR@/root_overlays/plasma

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
