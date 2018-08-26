subarch: amd64
target: stage4
version_stamp: dev-@latest@
rel_type: dev
profile: default/linux/amd64/17.0/systemd
snapshot: @latest@
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/portage/dev

stage4/use:
	ipv6

stage4/packages:
	dev-db/couchdb
	dev-db/postgresql
	dev-db/redis
	dev-lang/elixir
	dev-python/pipenv
	net-libs/nodejs

stage4/empty:
	/root/.ccache
	/tmp
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
	/usr/portage
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
