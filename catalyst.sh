#!/bin/bash

set -eo pipefail

if which lsns 2>/dev/null >&2; then
	if test -z "$(lsns | awk "/$$/&&/mnt/")"; then
		echo re-executing in our own mount namespace
		exec unshare -m $0 $@
	fi
fi

date=${1:-$(date --date=yesterday +%Y%m%d)}
arch=${ARCH:-$(uname -m)}

BASE_DIR="$(dirname $(readlink -f $0))"
REPO_DIR=$BASE_DIR/weekly

source "arch/$arch"
targets="${TARGETS:-${targets[*]}}"

catalyst_version=$(catalyst -V | awk 'NR==1{print$NF}')
case $catalyst_version in
3.*)
	sharedir="/usr/share/catalyst"
	;;
esac

BUILDS_DIR=$BASE_DIR/builds/$upstream
tempstage=$(mktemp)
cataconf=$(mktemp)
envscript=$(mktemp)

cat $BASE_DIR/catalyst.conf > $cataconf
tee $envscript <<<"export MAKEOPTS=\"-j$(nproc)\""
tee -a $cataconf <<<"envscript=\"${envscript}\""
tee -a $cataconf <<<"sharedir=\"${sharedir}\""
tee -a $cataconf <<<"storedir=\"$BASE_DIR\""

catalyst="catalyst -c $cataconf"

if ! tar tvvf $(dirname $0)/snapshots/portage-$date.tar.bz2 >/dev/null; then
	rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/snapshots/portage-$date.tar.bz2* $(dirname $0)/snapshots || true
	pushd $(dirname $0)/snapshots
		md5sum -c portage-$date.tar.bz2.md5sum
		chattr +i portage-$date.tar.bz2 || true
	popd
fi

for combo in $targets; do
	target=$(cut -d: -f1 <<<$combo)
	rel=${subarch:--$target}
	stage=$( cut -d: -f2 <<<$combo)

	# Skip a build if it already exists
	test -f $BUILDS_DIR/$target/$date/$stage-$upstream$rel-$date.tar.bz2 && continue

	# If a Makefile exists for the target, run the default target
	test -f $BUILDS_DIR/$target/Makefile && make -C $BUILDS_DIR/$target


	sed "s:@REPO_DIR@:$REPO_DIR:;s/@latest@/$date/" \
		$REPO_DIR/specs/$upstream/$target/$stage.spec | \
		tee $tempstage

	# add subarch and target
	tee -a $tempstage <<<"subarch: $upstream$subarch"
	tee -a $tempstage <<<"target: $stage"
	# append rel_type, version_stamp and snapshot
	tee -a $tempstage <<<"rel_type: $upstream/$target/$date"
	grep -q version_stamp: $tempstage || tee -a $tempstage <<<"version_stamp: $target-$date"
	tee -a $tempstage <<<"snapshot: $date"
	# append CHOST/CFLAGS to stage spec if set
	case "$stage" in
	stage[12])
		test -n "$chost" && tee -a $tempstage <<<"chost: $chost"
		;;
	esac
	(test -n "$cflags" && ! grep -q cflags: $tempstage) && tee -a $tempstage <<<"cflags: $cflags"

	test -d "$BASE_DIR/logs/$target" || mkdir -p "$BASE_DIR/logs/$target"
	$catalyst -f $tempstage | tee $BASE_DIR/logs/$target/$stage-$upstream$rel-$date.log

	rm -f $BUILDS_DIR/$target/$stage-$upstream$rel-latest.tar.bz2
	(cd $BUILDS_DIR/$target && ln -s $date/$stage-$upstream$rel-$date.tar.bz2 $BUILDS_DIR/$target/$stage-$upstream$rel-latest.tar.bz2)
	tee $BUILDS_DIR/$target/latest-$stage-$upstream$rel.txt <<<"$date/$stage-$upstream$rel-$date.tar.bz2"
done
