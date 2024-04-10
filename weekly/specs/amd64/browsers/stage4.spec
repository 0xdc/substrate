profile: default/linux/amd64/23.0/desktop/plasma/systemd
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/confdirs/browsers

stage4/packages:
	www-client/chromium
	www-client/firefox
	www-client/google-chrome
	www-client/google-chrome-beta
	www-client/google-chrome-unstable

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
