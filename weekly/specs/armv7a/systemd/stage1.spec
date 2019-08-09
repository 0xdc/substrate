## Uncomment if armv7a systemd stages are available
#source_subpath: armv7a/systemd/stage3-armv7a_hardfp-systemd-latest
## uncomment if openrc stages are available
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
update_seed: yes
update_seed_command: --rage-clean sys-fs/eudev virtual/udev
## end comments

common_flags: -O2 -mfpu=vfpv3-d16 -mfloat-abi=hard -mcpu=cortex-a9
profile: 0xdc:arm
portage_overlay: @REPO_DIR@/overlay
