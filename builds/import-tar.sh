#!/bin/bash

set -e

SRCF=${1?Need tarball filename or existing image name}
base=$(basename $1)
name=${base%.tar.bz2}

if ! machinectl --quiet show-image ${name}; then
	machinectl --quiet import-tar $SRCF ${base%.tar.bz2} &
fi

tee /etc/systemd/nspawn/${name}.nspawn <<EOF
[Exec]
## Workarounds
# systemd-networkd
Capability=CAP_NET_ADMIN
EOF

wait

excluded=(
	virtual/*
	acct-*/*
	sys-devel/libtool
)

if test "$(machinectl show-image -p ReadOnly --value $name)" = "yes"; then
	machinectl read-only ${name} false
fi

if test -d /var/lib/machines/${name}/etc/portage; then
	tee -a /etc/systemd/nspawn/${name}.nspawn <<-EOF
	PrivateUsers=no
	[Files]
	BindReadOnly=/var/db/repos/gentoo
	## Allow containers to make new binpkgs and fetch distfiles
	## Needs Exec.PrivateUsers=no
	Bind=/var/cache/binpkgs
	Bind=/var/cache/distfiles
	EOF

	tee /var/lib/machines/${name}/etc/portage/make.conf <<-EOF
	COMMON_FLAGS="-O2 -pipe"
	CFLAGS="\${COMMON_FLAGS}"
	CXXFLAGS="\${COMMON_FLAGS}"
	FCFLAGS="\${COMMON_FLAGS}"
	FFLAGS="\${COMMON_FLAGS}"
	DISTDIR="/var/cache/distfiles"
	PKGDIR="/var/cache/binpkgs"
	PORT_LOGDIR="/var/log/portage/build"
	LC_MESSAGES=C

	FEATURES="\$FEATURES -news"
	FEATURES="\$FEATURES fail-clean"
	FEATURES="\$FEATURES buildpkg binpkg-multi-instance"
	EMERGE_DEFAULT_OPTS="\$EMERGE_DEFAULT_OPTS --quiet-build --usepkg=y"
	EMERGE_DEFAULT_OPTS="\$EMERGE_DEFAULT_OPTS --buildpkg-exclude '${excluded[@]}'"
	EOF

	test -d /var/lib/machines/${name}/etc/portage/repos.conf || mkdir -p /var/lib/machines/${name}/etc/portage/repos.conf
	tee /var/lib/machines/${name}/etc/portage/repos.conf/gentoo.conf <<-EOF
	[gentoo]
	location = /var/db/repos/gentoo
	auto-sync = no
	EOF
fi

systemd-nspawn --quiet -M${name} systemctl --quiet preset-all

machinectl --quiet read-only ${name} true
