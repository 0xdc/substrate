profile: default/linux/amd64/23.0/no-multilib/systemd
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/openstack

diskimage/packages:
	app-admin/sshguard
	app-admin/sysstat
	app-containers/docker-registry
	bash-completion
	btrfs-progs
	dev-db/postgresql
	dev-db/redis
	dev-build/cmake
	dev-lang/go
	dev-python/mysqlclient
	dev-python/psycopg
	dev-vcs/git
	net-analyzer/vnstat
	net-libs/nodejs
	net-mail/swaks
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
	sys-boot/grub
	vim
	virtual/mysql
	yarn
