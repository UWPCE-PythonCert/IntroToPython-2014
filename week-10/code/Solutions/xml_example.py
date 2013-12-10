#!/usr/bin/env python

"""
Example of how to save data as xml, using the element tree module

This version stores all the data as attributes

"""

import xml.etree.ElementTree as ET
from indent_etree import indent # for prettier output

outfilename = "add_book_data.xml"

# get the data from the py file
from add_book_data_flat import AddressBook

# build a tree structure
root = ET.Element("address_book")

# add the elements:
for person in AddressBook:
    p = ET.SubElement(root, "person")
    # This method stores everything in attributes
    for key,value in person.items():
        p.set(key, value)
    
# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

indent(tree.getroot()) # to make it more pretty
tree.write(outfilename)   

### See if we can re-load it

tree = ET.parse(outfilename)
book = tree.getroot()
# re-build the original list:
AddressBook2 = []
for person in book.getchildren():
    #print person.attrib
    AddressBook2.append(person.attrib)

if AddressBook2 == AddressBook:
    print "xml version is the same as the original"

