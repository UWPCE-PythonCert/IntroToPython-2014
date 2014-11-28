#!/usr/bin/env python

"""
A really simple module, just to demonstrate disutils
"""

def capitalize(infilename, outfilename):
    """
    reads the contents of infilename, and writes it to outfilename, but with
    every word capitalized

    note: very primitive -- it will mess some files up!

    this is called by the capitalize script
    """
    infile = open(infilename, 'U')
    outfile = open(outfilename, 'w')

    for line in infile:
        outfile.write( " ".join( [word.capitalize() for word in line.split() ] ) )
        outfile.write("\n")
    
    return None