#!/bin/bash

rsync_args=(
	--prune-empty-dirs
	--recursive
	--mkpath

	--include='*/'

	--exclude="*livecd-stage2*"
	--include='*.tar.*'
	--include='latest-*.txt'
	--include='*.iso'
	--include='*.sh'
	--include='index.html'

	--exclude='*'
)

exec rsync "${rsync_args[@]}" "$@"
