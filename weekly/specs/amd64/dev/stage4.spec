profile: default/linux/amd64/17.1/no-multilib/systemd/merged-usr
source_subpath: amd64/systemd/stage4-amd64-systemd-latest
portage_confdir: @REPO_DIR@/confdirs/dev

stage4/packages:
	dev-db/postgresql
	dev-db/redis
	dev-lang/elixir
	net-libs/nodejs

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
