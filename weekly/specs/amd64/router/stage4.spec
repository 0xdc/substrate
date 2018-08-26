subarch: amd64
target: stage4
version_stamp: router-@latest@
rel_type: router
profile: default/linux/amd64/17.0/systemd
snapshot: @latest@
source_subpath: amd64/systemd/stage3-amd64-systemd-latest
portage_confdir: @REPO_DIR@/portage/router

stage4/use:
	bindist
	ipv6

stage4/packages:
	net-dialup/ppp
	net-dialup/rp-pppoe
	net-dns/dnsmasq

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
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
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
