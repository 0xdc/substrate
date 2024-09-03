profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/sso
target: stage4

stage4/packages:
	sys-auth/nss-pam-ldapd
	sys-auth/pam_yubico
	sys-auth/ssh-ldap-pubkey

stage4/root_overlay: @REPO_DIR@/root_overlays/sso

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
