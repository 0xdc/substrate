profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64
boot/kernel/gentoo/console: ttyS0,115200

livecd/bootargs: verify
livecd/gk_mainargs: --all-ramdisk-modules --symlink --b2sum
