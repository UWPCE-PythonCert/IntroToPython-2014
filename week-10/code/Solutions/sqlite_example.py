#!/usr/bin/env python

"""
Example of using sqlite3 module for a relational database
"""

import sqlite3, os

db_filename = "add_book_data.sqlite" # any extension will do -- *.db and *.sqlite are common 

# get the data from the py file
from add_book_data_flat import AddressBook

# if the db already exists -- delete it:
try:
    os.remove(db_filename)
except OSError:
    print "no db file there yet"

# create a connection to an sqlite db file:
conn = sqlite3.connect(db_filename)
# NOTE: you can do an in-memory version:
#conn = sqlite3.connect(":memory:")

# establish the schema (single table in this case...):
# Create a table 
conn.execute("""CREATE TABLE addresses
             ( first_name text,
               last_name text,
               address_line_1 text,
               address_line_2 text,
               address_city text,
               address_state text,
               address_zip text,
               email text,
               home_phone text,
               office_phone text,
               cell_phone text
               )"""
          )
conn.commit()

# get the fields from the data:
fields = AddressBook[0].keys()
# order matters, so we sort to make sure they will always be in the same order
fields.sort()

# add some data:
# get a cursor:
c = conn.cursor()
for person in AddressBook:
    # Insert a row of data
    row = [ person[field] for field in fields ]
    row = "','".join(row)
    sql = "INSERT INTO addresses VALUES ('%s')"%row
    #print sql
    c.execute(sql)

# Save (commit) the changes and close the connection
conn.commit()
conn.close()


### see if we can re-load it
conn = sqlite3.connect(db_filename)

sql = "SELECT * FROM addresses"
# no need for a cursor if a single sql statement needs to be run
result = conn.execute(sql)

## put it all back in a list of dicts
AddressBook2 = []
for row in result:
    d = dict(zip(fields, row))
    AddressBook2.append(d)

if AddressBook2 == AddressBook:
    print "the version pulled from sqlite is the same as the original"
else:
    print "they don't match!"

conn.close()    

## now do it with the non-flat version -- with a proper schema

# left as an exercise for the reader



