#!/usr/bin/python

import os

dir = os.getcwd()
print dir

infile = open('testfile.txt')
infile_data = infile.read()

outfile = open('test_outfile.txt', 'w')

outfile.write(infile_data)
infile.close()
outfile.close()

