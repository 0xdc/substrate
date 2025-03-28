#!/bin/bash

set -e

if test "$1" == "-s"; then
	which swift
	test "$ST_AUTH"
	test "$ST_USER"
	test "$ST_KEY"
	uploader="swift upload --skip-container-put"
	# to create and make it public: swift post -r '.r:*' $container
	shift
elif test "$1" == "-r"; then
	which rclone
	test -f ~/.config/rclone/rclone.conf
	uploader="-n1"
	shift # set container to echo
	# pipe to `rclone copyto --files-from - <src> <dst>`
else
	which openstack
	test "$OS_CLOUD" = "envvars" || (test -f /etc/openstack/clouds.yaml || test -f ~/.config/openstack/clouds.yaml )
	uploader="openstack object create"
fi

container="${1:-builds}"

pushd $(dirname $0)

f=(
	-type f

	\(
		# need to handle stage1-amd64-default
		! -name '*stage1-amd64-systemd*'
		-a
		! -name '*stage1-amd64-plasma*'
		-a
		! -name '*stage1-amd64-gnome*'
		-a
		! -name '*stage1-armv7a_hardfp*'
		-a
		! -name 'livecd-stage*'
		-a
		! -name 'latest-livecd-stage1-*'
	\)
	-a
	\(
		-name '*stage[134]-*'
		-o
		-name '*embedded-*'
		-o
		-name '*.iso*'
		-o
		-name '*.qcow2*'
		-o
		-name 'latest-livecd-stage3-*.txt'
		-o
		-name 'latest-diskimage-stage2-*.txt'
		-o
		-name 'latest-systemd-*.txt'
		-o
		-name 'systemd-*'
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
			if test -f ${i}.sha256; then
				:
			else
				if test -f $i; then
					if grep -q -m1 $i SHA256SUMS; then
						grep -m1 $i SHA256SUMS | gpg --batch --clear-sign -o ${i}.sha256
					else
						sha256sum $i | gpg --batch --clear-sign -o ${i}.sha256
					fi
				fi
			fi
			;;
		esac
	done
	popd
done

find */*/*/ */*/*.txt "${f[@]}" -o -name SHA256SUMS -o -name index.html | xargs --no-run-if-empty $uploader $container
