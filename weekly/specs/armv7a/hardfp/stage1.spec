subarch: armv7a_hardfp
version_stamp: @latest@
target: stage1
rel_type: hardfp
profile: default/linux/arm/17.0/armv7a
snapshot: @latest@
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
update_seed: yes
update_seed_command: --update --deep --newuse --complete-graph --rebuild-if-new-ver readline
portage_confdir: @REPO_DIR@/portage/ancient
