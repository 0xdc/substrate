#!/usr/bin/env python

import os
import sys
import portage

p = portage.db[portage.root]["porttree"].dbapi
is_github = 'GITHUB_STEP_SUMMARY' in os.environ

if is_github: print(f"::group::{sys.argv[1]}", file=sys.stderr)

bestmatch = p.xmatch("bestmatch-visible", sys.argv[1])
print(bestmatch)

if is_github:
    with open(os.environ['GITHUB_ENV'], 'a') as env:
        print(f'NEWPKG={bestmatch}', file=env)
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
        print(f'- found version {bestmatch}', file=summary)
    print("::endgroup::", file=sys.stderr)
