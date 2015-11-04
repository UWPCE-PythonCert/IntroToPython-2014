"""


write a program which copies a file from a source, to a destination
(without using shutil, or the OS copy command)

advanced: make it work for any size file: i.e. don’t read the entire
contents of the file into memory at once.

Note that if you want it to do any kind of file, you need to open the
files in binary mode: open(filename, 'rb') (or 'wb' for writing.)

"""
# write a program which prints the full path to all files in the current
# directory, one per line

import os
import glob

def print_directory_files():
    print("Files in the current directory:\n")
    for line in glob.glob('*.*'):
        print(os.getcwd() + line)

print_directory_files()
