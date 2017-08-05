#!/bin/bash

set -e

date=${1:-$(date +%Y%m%d)}
arch=$(uname -m)

cleanup() {
	test -e $tempstage && rm -f $tempstage
	test -e $cataconf  && rm -f $cataconf
	rm -fr $BASE_DIR/tmp
	rm -fr $BASE_DIR/kerncache
	rm -fr $BASE_DIR/snapshot_cache
}
trap cleanup EXIT

BASE_DIR=$(dirname $0)
REPO_DIR=$BASE_DIR/weekly
BUILDS_DIR=$BASE_DIR/builds/$arch

if test x"$arch" = "xx86_64"; then
	targets="systemd:stage1 systemd:stage2 systemd:stage3 systemd:stage4 plasma:stage5"
	upstream="amd64"
elif test x"$arch" = "xarmv7l"; then
	targets="hardfp:stage1 hardfp:stage2 hardfp:stage3"
	upstream="armv7a_hardfp"
fi

tempstage=$(mktemp)
cataconf=$(mktemp)

cat $BASE_DIR/catalyst.conf > $cataconf
tee -a $cataconf <<<"storedir=\"$BASE_DIR\""
tee -a $cataconf <<<"snapshot_cache=\"$BASE_DIR/snapshot_cache\""

catalyst="catalyst -c $cataconf"

if ! test -e $(dirname $0)/snapshots/portage-$date.tar.bz2; then
	# If the system has a unit to sync the tree, skip syncing the repo
	echo -n "Checking for automatic portage tree synchroniser... "
	systemctl is-active portage-sync.timer || emaint sync -r gentoo
	$catalyst -s $date
fi

for combo in $targets; do
	target=$(cut -d: -f1 <<<$combo)
	stage=$( cut -d: -f2 <<<$combo)

	make -C $BUILDS_DIR/$target

	test -d $BUILDS_DIR/$target/$date || mkdir $BUILDS_DIR/$target/$date

	# Skip a build if it already exists
	test -f $BUILDS_DIR/$target/$date/$stage-$upstream-$target-$date.tar.bz2 && continue

	sed "s:@REPO_DIR@:$REPO_DIR:;s/@latest@/$date/" \
		$REPO_DIR/specs/$arch/$target/$stage.spec | \
		tee $tempstage

	$catalyst -f $tempstage

	mv $BASE_DIR/builds/$target/$stage-$upstream-$target-$date.tar.bz2* $BUILDS_DIR/$target/$date/

	rm -f $BUILDS_DIR/$target/$stage-$upstream-$target-latest.tar.bz2
	(cd $BUILDS_DIR/$target && ln -s $date/$stage-$upstream-$target-$date.tar.bz2 $BUILDS_DIR/$target/$stage-$upstream-$target-latest.tar.bz2)
	tee $BUILDS_DIR/$target/current-$stage-$target.txt <<<"$date/$stage-$upstream-$target-$date.tar.bz2"
done
