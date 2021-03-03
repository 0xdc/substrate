#!/usr/bin/env python

import sys
from DeComp.definitions import COMPRESS_DEFINITIONS

try:
    d = COMPRESS_DEFINITIONS.get(sys.argv[1] or "lbzip2", None)
except:
    d = None

if d:
    try:
        print(".".join(["", d[4][0]]))
    except:
        pass
else:
    print(".tar.bz2")
