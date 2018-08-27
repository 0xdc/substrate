subarch: amd64
target: stage4
version_stamp: sso-@latest@
rel_type: sso
profile: default/linux/amd64/17.0/systemd
snapshot: @latest@
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/portage/sso
update_seed: yes
update_seed_command: --newuse --deep --update @world

stage4/use:
	bindist
	ipv6

stage4/packages:
	sys-auth/nss-pam-ldapd
	sys-auth/pam_krb5
	sys-auth/pam_yubico
	sys-auth/ssh-ldap-pubkey

stage4/root_overlay: @REPO_DIR@/overlays/sso

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
