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
    fields = [ "phone", 
               "first_name",
               "last_name",
               "email",
              ]

    def __init__(self, filename="a_book.json"):
        self.filename = filename
        self.book = []
        self.new_record()

    def new_record(self):
        """
        and a new, empty record

        :returns index: index of the new, empty record
        """
        self.book.append(dict.fromkeys(self.fields, ""))
        return len(self.book) - 1

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

    print 
    print "the first entry is:"
    entry = a_book.book[0]
    print entry
    print "the first entry's name is:"
    print entry['first_name'], entry['last_name']



