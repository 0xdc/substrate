profile: default/linux/amd64/17.1/systemd
source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64

livecd/bootargs: docache dokeymap
livecd/fsscript: @REPO_DIR@/fsscripts/livecd
livecd/fstype: squashfs
livecd/gk_mainargs: --all-ramdisk-modules
livecd/iso: roflmaOS-@latest@.iso
livecd/root_overlay: @REPO_DIR@/root_overlays/livecd
livecd/volid: roflmaOS amd64 @latest@
