source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest
profile: not-necessary


boot/kernel: gentoo
boot/kernel/gentoo/console: ttyS0

livecd/bootargs: dokeymap overlayfs verify
livecd/cdtar: @REPO_DIR@/../builds/amd64/systemd/@latest@/livecd-stage2-amd64-systemd-@latest@.tar.bz2
livecd/fstype: squashfs
livecd/fsops: -comp xz
livecd/iso: roflmaOS-@latest@.iso
livecd/verify: yes
livecd/volid: roflmaOS amd64 @latest@
