#Note that if you want it to do any kind of file, you need to open the
# files in binary mode: open(filename, 'rb') (or 'wb' for writing.)

# write a program which prints the full path to all files in the current
# directory, one per line

import os
import glob
from pathlib import *

def print_directory_files():
    print("Files in the current directory:\n")
    for line in glob.glob('*.*'):
        print(os.getcwd() + line)

# print_directory_files()

# OR:


def print_directory_files2():
    p = Path('.')
    for line in list(p.glob('**/*.py')):
        print(line)

# print_directory_files2()

# write a program which copies a file from a source, to a destination
# (without using shutil, or the OS copy command)


def copy_file(source, destination):
    with open(source, "rb") as file_one:
        contents = file_one.read()
    with open(destination, "wb") as file_two:
        file_two.write(contents)


# advanced: make it work for any size file: i.e. don’t read the entire
# contents of the file into memory at once.

