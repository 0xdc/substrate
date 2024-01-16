profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/openstack

stage4/packages:
	bash-completion
	btrfs-progs
	dev-db/redis
	dev-build/cmake
	dev-vcs/git
	dovecot
	ejabberd
	elixir
	fcgiwrap
	mit-krb5
	munin
	murmur
	nginx
	opendkim
	openldap
	php
	postfix
	quassel
	rclone
	rspamd
	ssh-ldap-pubkey
	vim
	virtual/mysql
	yarn

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
