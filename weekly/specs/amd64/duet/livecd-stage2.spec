profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/duet/livecd-stage1-amd64-duet-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/plasma/duet

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/sources: >=sys-kernel/gentoo-kernel-6.3.1::gentoo
boot/kernel/gentoo/packages: --usepkg=n sys-power/acpi_call
boot/kernel/gentoo/dracut_args: --xz

livecd/bootargs: fbcon=rotate:1 consoleblank=3600 systemd.wants=NetworkManager.service splash quiet
