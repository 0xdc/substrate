#!/bin/bash

set -e

if test "$1" == "-s"; then
	which swift
	test "$ST_AUTH"
	test "$ST_USER"
	test "$ST_KEY"
	uploader="swift upload"
	# to make it public: swift post -r '.r:*' $container
else
	which openstack
	test "$OS_CLOUD" = "envvars" || (test -f /etc/openstack/clouds.yaml || test -f ~/.config/openstack/clouds.yaml )
	uploader="openstack object create"
fi

pushd $(dirname $0)

f=(
	-type f

	\(
		# need to handle stage1-amd64-default
		! -name '*stage1-amd64-systemd*'
		-a
		! -name '*stage1-armv7a_hardfp*'
		-a
		! -name 'livecd-stage*'
	\)
	-a
	\(
		-name '*stage[134]-*'
		-o
		-name '*embedded-*'
		-o
		-name '*.iso*'
		-o
		-name 'latest-livecd-stage3-*.txt'
	\)
)

for dir in */*/*/; do
	pushd $dir
	test -f SHA256SUMS || {
		sha256sums=$(find * "${f[@]}" | xargs --no-run-if-empty sha256sum)

		test "${sha256sums}" && {
			cat >SHA256SUMS <<<"$sha256sums"
			#test -f SHA256SUMS.gpg || gpg --batch --detach-sign -o SHA256SUMS.gpg SHA256SUMS
		}
	}
	for i in *; do
		case "$i" in
		SHA256SUMS|*.CONTENTS.gz|*.sha256|*.gpg)
			;;
		*)
			test -f ${i}.sha256 || sha256sum $i | gpg --batch --clear-sign -o ${i}.sha256
			;;
		esac
	done
	popd
done

find */*/*/ */*/*.txt "${f[@]}" -o -name 'SHA256SUMS*' | xargs --no-run-if-empty $uploader bindist
