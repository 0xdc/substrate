profile: default/linux/amd64/17.1/desktop/plasma/systemd/merged-usr
source_subpath: amd64/plasma/stage4-amd64-plasma-latest
portage_confdir: @REPO_DIR@/confdirs/dev

stage4/packages:
	app-emulation/virt-manager
	dev-db/postgresql
	dev-db/redis
	dev-debug/gdb
	dev-debug/strace
	dev-debug/valgrind
	dev-lang/elixir
	dev-lang/nasm
	net-libs/nodejs

stage4/empty:
	/var/cache/edb/dep
	/var/db/repos
