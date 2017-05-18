#!/bin/bash

set -e

date=$(date +%Y%m%d)

cleanup() {
	test -e $tempstage && rm -f $tempstage
	test -e $cataconf  && rm -f $cataconf
	rm -fr $BASE_DIR/tmp
	rm -fr $BASE_DIR/kerncache
	rm -fr $BASE_DIR/snapshot_cache
}
trap cleanup EXIT

BASE_DIR=$(dirname $0)
REPO_DIR=$BASE_DIR/releng
BUILDS_DIR=$BASE_DIR/builds

test -d $BUILDS_DIR/systemd/$date || mkdir $BUILDS_DIR/systemd/$date

tempstage=$(mktemp)
cataconf=$(mktemp)

cat $BASE_DIR/catalyst.conf > $cataconf
tee -a $cataconf <<<"storedir=\"$BASE_DIR\""
tee -a $cataconf <<<"snapshot_cache=\"$BASE_DIR/snapshot_cache\""

catalyst="catalyst -c $cataconf"

if ! test -e $(dirname $0)/snapshots/portage-$date.tar.bz2; then
	# If the system has a unit to sync the tree, skip syncing the repo
	systemctl is-active portage-sync.timer || emaint sync -r gentoo
	$catalyst -s $date
fi

for stage in stage1 stage2 stage3 stage4; do
	sed "s:@REPO_DIR@:$REPO_DIR:;s/@latest@/$date/" \
		$REPO_DIR/releases/weekly/specs/amd64/$stage-systemd.spec | \
		tee $tempstage

	$catalyst -f $tempstage

	mv $BUILDS_DIR/systemd/$stage-amd64-systemd-$date.tar.bz2* $BUILDS_DIR/systemd/$date/

	(cd $BUILDS_DIR/systemd && ln -s $date/$stage-amd64-systemd-$date.tar.bz2 $BUILDS_DIR/systemd/$stage-amd64-systemd-latest.tar.bz2)
	tee $BUILDS_DIR/systemd/current-$stage-systemd.txt <<<"$date/$stage-amd64-systemd-$date.tar.bz2"
done
