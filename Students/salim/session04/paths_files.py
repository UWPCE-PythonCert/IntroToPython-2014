#!/usr/local/bin/python

import pathlib


def copy_file(source, destination):
    # read cotents of source file
    file_to_copy = open(source, 'r').read()

    # open new file and write contents of source file
    file_to_write = open(destination, 'w')
    file_to_write.write(file_to_copy)

    # close file
    file_to_write.close()


# find file directory
file_path = pathlib.Path(__file__)
parent_path = file_path.parent

# print files in directory
for f in parent_path.iterdir():
    print f

# copy file
source = ("/Users/salimhamed/Documents/Documents/School/Python (2014)/"
          "IntroToPython/Students/salim/session04/dict_set_lab.py")
destination = ("/Users/salimhamed/Documents/Documents/School/Python (2014)/"
               "IntroToPython/Students/salim/session04/cp_dict_set_lab.py")
copy_file(source, destination)
