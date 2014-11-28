#!/usr/bin/env python

"""
very simple script to print the full paths in the current dir
"""

import os

files = os.listdir('.')
for name in files:
    print os.path.abspath(name)

