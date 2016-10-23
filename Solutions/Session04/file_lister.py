#!/usr/bin/env python

"""
file_lister

Write a program which prints the full path to all files in the current
directory, one per line.
"""

import os
import pathlib

# Two ways to do this:

# One: get file names, and convert to absolute path:

print("listing using method one")
for name in os.listdir(os.curdir):
    print(os.path.abspath(name))

# Note: os.curdir is "." on all sytems I know of...
#       so you could just do os.curdir(".")
#       Back in the days of the old MacOS -- it WAS different there.

# Two: get the current dir path, then join that with each of the filenames
curdir = os.getcwd()
print("listing using method two")
for name in os.listdir(curdir):
    print(os.path.join(curdir, name))

# Three: using pathlib:
print("listing using pathlib")
for name in pathlib.Path().glob('*'):
    print(name.absolute())
