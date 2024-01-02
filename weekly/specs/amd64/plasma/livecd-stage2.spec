profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64
boot/kernel/gentoo/console: ttyS0,115200

livecd/bootargs: dokeymap verify
livecd/gk_mainargs: --all-ramdisk-modules --symlink --b2sum
