profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/openstack/diskimage-stage1-amd64-openstack-latest
portage_confdir: @REPO_DIR@/confdirs/livecd

boot/kernel: gentoo
boot/kernel/gentoo/config: @REPO_DIR@/kconfig.amd64
boot/kernel/gentoo/console: ttyS0,115200

diskimage/type: console
diskimage/qcow2: roflmaOS-openstack-@latest@.qcow2
diskimage/qcow2_roottype: btrfs
diskimage/verify: yes
diskimage/volid: roflmaOS OpenStack amd64 @latest@
