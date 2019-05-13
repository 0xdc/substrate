#!/bin/bash

set -e

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
	if test x"$HISTORICAL" = "xyes"; then
		rm -f $(dirname $0)/snapshots/portage-$date.tar.bz2*
		wget -P $(dirname $0)/snapshots https://dev.gentoo.org/~swift/snapshots/portage-$date.tar.bz2
		wget -P $(dirname $0)/snapshots https://dev.gentoo.org/~swift/snapshots/portage-$date.tar.bz2.md5sum
	else
		rsync --no-motd --progress mirror.bytemark.co.uk::gentoo/snapshots/portage-$date.tar.bz2* $(dirname $0)/snapshots || true
	fi
	pushd $(dirname $0)/snapshots
		md5sum -c portage-$date.tar.bz2.md5sum
		chattr +i portage-$date.tar.bz2 || true
	popd
fi

for combo in $targets; do
	target=$(cut -d: -f1 <<<$combo)
	rel=${subarch:--$target}
	stage=$( cut -d: -f2 <<<$combo)

	# Test that target directory exists (parents=yes)
	test -d $BUILDS_DIR/$target || mkdir -p $BUILDS_DIR/$target

	# Skip a build if it already exists
	test -f $BUILDS_DIR/$target/$date/$stage-$upstream$rel-$date.tar.bz2 && continue

	# If a Makefile exists for the target, run the default target
	test -f $BUILDS_DIR/$target/Makefile && make -C $BUILDS_DIR/$target


	sed "s:@REPO_DIR@:$REPO_DIR:;s/@latest@/$date/" \
		$REPO_DIR/specs/$upstream/$target/$stage.spec | \
		tee $tempstage

	# add subarch and target
	tee -a $tempstage <<<"subarch: $upstream$rel"
	tee -a $tempstage <<<"target: $stage"
	# append rel_type, version_stamp and snapshot
	tee -a $tempstage <<<"rel_type: $target"
	grep -q version_stamp: $tempstage || tee -a $tempstage <<<"version_stamp: $target-$date"
	tee -a $tempstage <<<"snapshot: $date"
	# append CBUILD/CFLAGS to stage spec if set
	test -n "$cbuild" && tee -a $tempstage <<<"cbuild: $cbuild"
	(test -n "$cflags" && ! grep -q cflags: $tempstage) && tee -a $tempstage <<<"cflags: $cflags"

	$catalyst -f $tempstage | tee $BASE_DIR/logs/$stage-$upstream$rel-$date.log

	# Make a directory for $date and move output into it (parents=no)
	test -d $BUILDS_DIR/$target/$date || mkdir $BUILDS_DIR/$target/$date
	mv $BASE_DIR/builds/$target/$stage-$upstream$rel-$date.tar.bz2* $BUILDS_DIR/$target/$date/
	rmdir --ignore-fail-on-non-empty $BASE_DIR/builds/$target # Cleanup, but don't care about it

	rm -f $BUILDS_DIR/$target/$stage-$upstream$rel-latest.tar.bz2
	(cd $BUILDS_DIR/$target && ln -s $date/$stage-$upstream$rel-$date.tar.bz2 $BUILDS_DIR/$target/$stage-$upstream$rel-latest.tar.bz2)
	tee $BUILDS_DIR/$target/latest-$stage-$upstream$rel.txt <<<"$date/$stage-$upstream$rel-$date.tar.bz2"
done
