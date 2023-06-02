profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/amd64/plasma/duet

compression_mode: lbzip2
boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64

livecd/bootargs: verify setkmap=uk fbcon=rotate:1 consoleblank=3600 systemd.wants=NetworkManager.service systemd.wants=sddm.service systemd.wants=sysstat-collect.timer systemd.wants=vnstatd.service i915.enable_fbc=1 systemd.mask=systemd-repart.service iwlwifi.power_level=5 iwlwifi.power_save=1
livecd/gk_mainargs: --symlink --b2sum
