target: embedded
profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/stage4-amd64-users-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/murmur

embedded/packages:
	net-voip/murmur
