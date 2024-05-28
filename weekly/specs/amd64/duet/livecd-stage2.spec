profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/duet/livecd-stage1-amd64-duet-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/plasma/duet

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/sources: >=sys-kernel/gentoo-kernel-6.3.1::gentoo
boot/kernel/gentoo/packages: --usepkg=n sys-power/acpi_call
boot/kernel/gentoo/dracut_args: --no-hostonly

livecd/bootargs: systemd.wants=NetworkManager.service systemd.wants=sddm.service splash quiet
livecd/volid: roflmaOS_duet
