#!/usr/bin/env python3

"""
Very simple script to copy a file

Use like so:

python copy_file original_file_name, new_file_name
"""

import sys

source, dest = sys.argv[1:3]

# binary mode important here.
infile = open(source, 'rb')  # read binary mode
outfile = open(dest, 'wb')   # write binary mode

outfile.write(infile.read())
infile.close()
outfile.close()

# # or as a one-liner:
# open(dest, 'wb').write(open(source, 'rb').read())
