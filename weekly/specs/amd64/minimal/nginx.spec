profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
target: embedded
portage_confdir: @REPO_DIR@/confdirs/nginx
embedded/root_overlay: @REPO_DIR@/root_overlays/nginx

embedded/packages:
	app-editors/vim
	www-servers/nginx
