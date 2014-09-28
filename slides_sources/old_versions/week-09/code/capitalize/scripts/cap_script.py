#!/usr/bin/env python

"""
A really simple script just to demonstrate disutils
"""

import sys, os
from capitalize import capital_mod


if __name__ == "__main__":
    try:
        infilename = sys.argv[1]
    except IndexError:
        print "you need to pass in a file to process"

    root, ext = os.path.splitext(infilename)
    outfilename = root + "_cap" + ext
    
    # do the real work:
    print "Capitalizing: %s and storing it in %s"%(infilename, outfilename)
    capital_mod.capitalize(infilename, outfilename)
    
    print "I'm done"
    