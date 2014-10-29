#!/usr/bin/env python

"""
Very simple script to copy a file
"""

import sys

source, dest = sys.argv[1:3]

infile = open(source, 'rb') # read binary mode
outfile = open(dest, 'wb')  # write binary mode

outfile.write(infile.read())
infile.close()
outfile.close()

## or as a one-liner:
# open(dest, 'wb').write(open(source, 'rb').read())


