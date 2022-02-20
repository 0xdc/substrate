profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/mergeusr/stage3-amd64-mergeusr-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/embedded
target: embedded

embedded/packages:
	dev-libs/openssl
	games-server/steamcmd
	sys-apps/coreutils
	sys-apps/findutils
	sys-apps/iproute2
	sys-devel/gcc

embedded/root_overlay: @REPO_DIR@/root_overlays/steamcmd
