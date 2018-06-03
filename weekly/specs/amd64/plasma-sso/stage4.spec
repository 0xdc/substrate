subarch: amd64
target: stage4
version_stamp: plasma-sso-@latest@
rel_type: plasma-sso
profile: default/linux/amd64/17.0/desktop/plasma/systemd
snapshot: @latest@
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/portage/sso

stage4/use:
	ipv6

stage4/packages:
	sys-auth/nss-pam-ldapd
	sys-auth/pam_krb5

stage4/root_overlay: @REPO_DIR@/overlays/sso

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
