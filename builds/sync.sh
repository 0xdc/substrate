#!/bin/bash

rsync_args=(
	--prune-empty-dirs
	--recursive
	--mkpath
	--links

	--include='*/'

	--exclude="*livecd-stage2*"
	--exclude="*-latest.tar.*"
	--exclude="*unbound*"
	--include='*.tar.*'
	--include='latest-*.txt'
	--include='*.iso'
	--include='*.sh'
	--include='*.tcl'
	--include='index.html'

	--exclude='*'
)

exec rsync "${rsync_args[@]}" "$@"
