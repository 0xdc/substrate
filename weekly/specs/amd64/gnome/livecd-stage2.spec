profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/gnome/livecd

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/sources: >=sys-kernel/gentoo-kernel-6.3.1::gentoo
boot/kernel/gentoo/packages: --usepkg=n sys-power/acpi_call
boot/kernel/gentoo/dracut_args: --xz

livecd/bootargs: systemd.wants=NetworkManager.service systemd.wants=gdm.service quiet splash
