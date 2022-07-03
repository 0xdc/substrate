profile: default/linux/amd64/17.1/no-multilib/systemd
source_subpath: amd64/mergeusr/stage4-amd64-users-latest
target: embedded
portage_confdir: @REPO_DIR@/confdirs/nginx
embedded/root_overlay: @REPO_DIR@/root_overlays/nginx

embedded/packages:
	app-editors/vim
	www-servers/nginx
