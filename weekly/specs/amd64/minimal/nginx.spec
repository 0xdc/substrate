profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/mergeusr/stage3-amd64-mergeusr-latest
target: embedded
portage_confdir: @REPO_DIR@/confdirs/nginx
embedded/root_overlay: @REPO_DIR@/root_overlays/nginx

embedded/packages:
	app-editors/vim
	www-servers/nginx
