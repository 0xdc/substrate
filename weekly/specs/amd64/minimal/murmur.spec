target: embedded
profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/mergeusr/stage3-amd64-mergeusr-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/murmur

embedded/packages:
	media-sound/murmur
