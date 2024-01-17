source_subpath: amd64/gnome/stage4-amd64-gnome-latest

boot/kernel: gentoo

livecd/cdtar: @REPO_DIR@/../builds/amd64/gnome/@latest@/livecd-stage2-amd64-gnome-@latest@.tar.bz2
livecd/fstype: squashfs
livecd/fsscript: @REPO_DIR@/fsscripts/livecd
livecd/fsops: -comp xz -Xbcj x86
livecd/iso: roflmaOS-gnome-@latest@.iso
livecd/root_overlay: @REPO_DIR@/root_overlays/livecd
livecd/verify: yes
livecd/volid: roflmaOS amd64 gnome @latest@
