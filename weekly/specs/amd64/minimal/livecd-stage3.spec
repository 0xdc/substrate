source_subpath: amd64/minimal/embedded-amd64-minimal-latest
profile: not-necessary


boot/kernel: gentoo
boot/kernel/gentoo/console: ttyS0

livecd/bootargs: dokeymap overlayfs verify
livecd/cdtar: @REPO_DIR@/../builds/amd64/minimal/@latest@/livecd-stage2-amd64-minimal-@latest@.tar.bz2
livecd/fsscript: @REPO_DIR@/fsscripts/livecd
livecd/fstype: squashfs
livecd/fsops: -comp xz -Xbcj x86
livecd/iso: roflmaOS-minimal-@latest@.iso
livecd/root_overlay: @REPO_DIR@/root_overlays/livecd
livecd/verify: yes
livecd/volid: roflmaOS minimal amd64 @latest@
