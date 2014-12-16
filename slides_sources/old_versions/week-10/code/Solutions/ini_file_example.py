#!/usr/bin/env python

"""
Example of how to save data as an "ini" file with ConfigParser

"""

import ConfigParser

outfilename = "addresses.ini"

# get the data from the py file
# ini format really only holds flat data well.
from add_book_data_flat import AddressBook

# save it in an ini file
data = ConfigParser.ConfigParser()

for i, person in enumerate(AddressBook):
    sec_name = 'person%i'%i
    data.add_section(sec_name)
    for key,value in person.items():
        data.set(sec_name, key, value)

data.write( open("add_book.ini",'w') )         

## see if we can re-load it
data = data = ConfigParser.ConfigParser()
data.read("add_book.ini")

#extract the data and put into a list of dicts:
AddressBook2 = []
for sec_name in data.sections():
    AddressBook2.append( dict( data.items(sec_name) ) )
print AddressBook2
    
if AddressBook2 == AddressBook:
    print "they are the same"

