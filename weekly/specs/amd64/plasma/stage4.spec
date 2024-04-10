profile: default/linux/amd64/23.0/desktop/plasma/systemd
portage_confdir: @REPO_DIR@/confdirs/plasma
source_subpath: amd64/plasma/stage3-amd64-plasma-latest

stage4/use:
	ibus

stage4/packages:
	app-admin/pass-otp
	app-admin/ansible
	app-editors/vim
	app-eselect/eselect-repository
	app-i18n/ibus-anthy
	app-i18n/imsettings
	app-shells/bash-completion
	dev-vcs/git
	kde-apps/ark
	kde-apps/dolphin
	kde-apps/kmail
	kde-apps/konsole
	kde-plasma/breeze-gtk
	kde-plasma/kdeplasma-addons
	kde-plasma/kscreen
	kde-plasma/plasma-desktop
	kde-plasma/plasma-disks
	kde-plasma/plasma-pa
	kde-plasma/sddm-kcm
	kde-plasma/systemsettings
	kde-plasma/xembed-sni-proxy
	media-fonts/droid
	net-firewall/nftables
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
