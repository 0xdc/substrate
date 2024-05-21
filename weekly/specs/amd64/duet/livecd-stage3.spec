source_subpath: amd64/duet/livecd-stage1-amd64-duet-latest

boot/kernel: gentoo

livecd/cdtar: @REPO_DIR@/../builds/amd64/duet/@latest@/livecd-stage2-amd64-duet-@latest@.tar.bz2
livecd/fstype: squashfs
livecd/fsscript: @REPO_DIR@/fsscripts/livecd
livecd/fsops: -comp xz -Xbcj x86
livecd/iso: roflmaOS-duet-@latest@.iso
livecd/root_overlay: @REPO_DIR@/root_overlays/duet
livecd/volid: roflmaOS_duet
