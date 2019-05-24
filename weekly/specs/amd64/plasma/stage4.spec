profile: default/linux/amd64/17.0/desktop/plasma/systemd
source_subpath: amd64/plasma/stage3-amd64-plasma-latest
portage_confdir: @REPO_DIR@/portage/plasma

stage4/packages:
	app-emulation/virt-manager
	kde-plasma/plasma-meta
	kde-apps/dolphin
	kde-apps/konsole
	www-client/firefox

stage4/root_overlay: @REPO_DIR@/overlays/plasma

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
