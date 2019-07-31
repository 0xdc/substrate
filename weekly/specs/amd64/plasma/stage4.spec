profile: default/linux/amd64/17.0/desktop/plasma/systemd
portage_confdir: @REPO_DIR@/confdirs/plasma
source_subpath: amd64/plasma/stage3-amd64-plasma-latest

stage4/packages:
	app-emulation/virt-manager
	kde-plasma/plasma-meta
	kde-apps/dolphin
	kde-apps/konsole
	www-client/firefox

stage4/root_overlay: @REPO_DIR@/root_overlays/plasma

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
