target: systemd
profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir:
	@REPO_DIR@/confdirs/minimal/jenkins
	@REPO_DIR@/confdirs/minimal/systemd

boot/kernel: gentoo
boot/kernel/gentoo/console: ttyS0,115200
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64

embedded/packages:
	app-containers/buildah
	app-containers/podman
	dev-util/jenkins-bin
	dev-vcs/git

embedded/root_overlay: @REPO_DIR@/root_overlays/jenkins

embedded/iso: roflmaOS-jenkins-@latest@.iso
embedded/fstype: btrfs
