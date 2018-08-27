subarch: armv7a_hardfp
target: stage4
version_stamp: @latest@
rel_type: ella
profile: default/linux/arm/13.0/armv7a
snapshot: @latest@
source_subpath: armv7a/hardfp/stage3-armv7a_hardfp-latest
update_seed: yes
update_seed_command: --newuse --deep --update @world

stage4/use:
	bindist
	ipv6

stage4/packages:
	app-editors/vim
	app-shells/bash-completion
	dev-embedded/u-boot-tools
	dev-vcs/git
	sys-apps/dtc
	sys-devel/bc
	sys-devel/distcc
	sys-fs/dosfstools

stage4/root_overlay: @REPO_DIR@/overlays/ella

stage4/rcadd:
	busybox-ntpd|default
	net.eth0|default
	sshd|default

stage4/unmerge:
	app-editors/nano

stage4/empty:
	/root/.ccache
	/tmp
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/gentoo/repos
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	/usr/portage
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
