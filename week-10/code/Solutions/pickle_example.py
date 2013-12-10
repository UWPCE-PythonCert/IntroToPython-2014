#!/usr/bin/env python

"""
Example of how to save data in a pickle

"""

import cPickle as pickle

outfilename = "add_book_data.pickle"

# get the data from the py file
from add_book_data import AddressBook

# pickle it (it's really this simple)
pickle.dump(AddressBook, open(outfilename, 'wb') )

## see if we can re-load it

AddressBook2 = pickle.load( open(outfilename, 'rb') )

if AddressBook2 == AddressBook:
    print "pickeld/unpickled version is  the same as the original"

