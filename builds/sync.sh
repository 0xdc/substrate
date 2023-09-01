#!/bin/bash

rsync_args=(
	--prune-empty-dirs
	--recursive
	--mkpath

	--include='*/'

	--include='*.tar.*'
	--include='latest-*.txt'
	--include='*.iso'
	--include='*.sh'
	--include='index.html'

	--exclude='*'
)

exec rsync "${rsync_args[@]}" "$@"
