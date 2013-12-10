#!/usr/bin/env python

"""
Example of how to save data as json

"""

import json

outfilename = "add_book_data.json"

# get the data from the py file
from add_book_data import AddressBook

# dump it as json (it's really this simple)
json.dump(AddressBook, open(outfilename, 'wb') )
#json.dump(AddressBook, open(outfilename, 'wb'), indent=4 ) # specifying indent pretty-prints the json

### see if we can re-load it

AddressBook2 = json.load( open(outfilename, 'rb') )

if AddressBook2 == AddressBook:
    print "json version is the same as the original"

