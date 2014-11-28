#!/usr/bin/env python

"""
Example of how to save data as xml, using the element tree module

This version uses the nested dataset, and does full-on nested XML

"""

import xml.etree.ElementTree as ET
from indent_etree import indent # for prettier output

outfilename = "add_book_data2.xml"

# get the data from the py file
from add_book_data import AddressBook

# build a tree structure
root = ET.Element("address_book")

# add the elements:
for person in AddressBook:
    p = ET.SubElement(root, "person")
    # This method stores everything as sub-elements
    for key, value in person.items():
        if type(value) == dict:
            address = ET.SubElement(p, 'address')
            for sub_key, sub_value in value.items():
                sub_el = ET.SubElement(address, sub_key)
                sub_el.text=sub_value
        else:
            el = ET.SubElement(p, key)
            el.text=value
    
# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

indent(tree.getroot()) # to make it more pretty
tree.write(outfilename)   

### See if we can re-load it

tree = ET.parse(outfilename)
book = tree.getroot()
# re-build the original list:
AddressBook2 = []
for person in list(book):
    p = {}
    for sub_el in list(person):
        if sub_el.tag == "address":
            address = {}
            for sub_sub_el in sub_el.getchildren():
                t = sub_sub_el.text
                if t is None: ## etree returns None for empty tags!    
                    address[sub_sub_el.tag] = ""
                else:
                    address[sub_sub_el.tag] = t
            p['address'] = address
        else:
            p[sub_el.tag] = sub_el.text
    AddressBook2.append(p)

if AddressBook2 == AddressBook:
    print "xml version is the same as the original"
else:
    print "xml version is not exactly the same as the original"
