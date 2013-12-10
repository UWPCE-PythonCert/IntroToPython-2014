#!/usr/bin/env python

"""
Example of how to save data using the anydbm package

"""


import anydbm

outfilename = "add_book_data.dbm"

# get the data from the py file
# csv format really only holds flat data well.
from add_book_data_flat import AddressBook

## note that dbm files are really only good for simple key-value storage
##   so let's just do one record:
person = AddressBook[0]

# create a dbm  file writing object
db = anydbm.open(outfilename, 'n')

#write the data:
for key, value in person.items():
    db[key] = value

#close the file
db.close()    

#### see if it can be re-loaded.
#
# open an existing dbm file
db = anydbm.open(outfilename, 'r')

#read the data:
person = {}
for key, value in db.items():
    person[key] = value

#Check if they are the same
if person == AddressBook[0]:
    print "db version is the same as the original"

### Storing multiple people:
##    building up a key

# left as an exercise for the reader....

