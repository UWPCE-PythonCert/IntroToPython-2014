#!/usr/bin/env python

"""
application logic code for ultra simple 
address book app...
"""

import json

class AddressBook(object):
    """
    very simple data model -- just a list of dicts
    
    each dict represents an entry in the address book
    """
    def __init__(self):
        self.book = [{},]
        self.filename = "a_book.json"

    def save_to_file(self, filename=None):
        if filename is not None :
            self.filename = filename
        json.dump(self.book, open(self.filename, 'wb'), indent=4 )

    def load_from_file(self, filename=None):
        if filename is not None :
            self.filename = filename
        self.book = json.load( open(self.filename, 'rb') )

    def close(self):
        """
        clear out the data...
        leave it with one empty dict
        """
        del self.book[:]
        self.book.append({})

if __name__ == "__main__":
    import pprint
    a_book = AddressBook()
    a_book.load_from_file()

    print "the data in the address book is:"
    pprint.pprint(a_book.book)

