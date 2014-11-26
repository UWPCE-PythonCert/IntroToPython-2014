#!/usr/bin/env python2.7

import pathlib
pth = pathlib.Path.cwd()
print "Current path:", pth

print "\nList of files and directories:"
for f in pth.iterdir():
    if f.is_dir():
        print "Directory:", f
    elif f.is_file():
        print "File:", f

# a dumb way to copy a file from source to destination
srcpth = '/home/ian/UWPython/class4/homework4'
destpth = '/home/ian/UWPython/class4/homework4/newdirectory/subdirectory/'
srcdir = pathlib.Path(srcpth)
destdir = pathlib.Path(destpth)
filename = 'afile.txt'

print "\nMoving file:", filename
print "  From:", srcdir
print "  To  :", destdir

f = open(srcpth+"/"+filename)
fcpy = open(destpth+"/"+filename, 'w')
for line in f:
    fcpy.write(line)
f.close()
fcpy.close()