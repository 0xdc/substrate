target: embedded
profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage4-amd64-users-latest
portage_confdir: @REPO_DIR@/confdirs/minimal/murmur

embedded/packages:
	net-voip/murmur
