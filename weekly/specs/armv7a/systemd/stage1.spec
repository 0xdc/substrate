source_subpath: armv7a/systemd/stage3-armv7a_hardfp-systemd-latest
common_flags: -O2 -mfpu=vfpv3-d16 -mfloat-abi=hard -mcpu=cortex-a9
profile: 0xdc:arm
repos: @REPO_DIR@/overlay
portage_confdir: @REPO_DIR@/confdirs/armv7a/systemd/stage1
update_seed: yes
update_seed_command: --update --oneshot dev-libs/glib sys-libs/glibc
