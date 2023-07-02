source_subpath: amd64/systemd/livecd-stage1-amd64-systemd-latest

boot/kernel: gentoo

livecd/cdtar: @REPO_DIR@/../builds/amd64/systemd/livecd-stage2-amd64-systemd-latest.tar.bz2
livecd/fstype: squashfs
livecd/fsscript: @REPO_DIR@/fsscripts/livecd
livecd/fsops: -comp xz -Xbcj x86
livecd/iso: roflmaOS-@latest@.iso
livecd/root_overlay: @REPO_DIR@/root_overlays/livecd
livecd/verify: yes
livecd/volid: roflmaOS amd64 @latest@
