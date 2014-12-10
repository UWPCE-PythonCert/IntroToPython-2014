#!/usr/bin/env python

"""
sample data for persistence/serializatiion examples

This version is nested, with more stucture 
  - can be saved with pickle, JSON, xml...
"""

AddressBook = [ {'first_name': "Chris",
                 'last_name': "Barker",
                 'address' : {'line_1':"835 NE 33rd St",
                              'line_2' : "",
                              'city' : "Seattle",
                              'state': "WA",
                              'zip': "96543"},
                 'email' : "PythonCHB@gmail.com",
                 'home_phone' : "206-555-1234",
                 'office_phone' : "123-456-7890",
                 'cell_phone' : "234-567-8901",
                 },
                
                {'first_name': "Fred",
                 'last_name': "Jones",
                 'address' : {'line_1':"123 SE 13th St",
                              'line_2' : "Apt. 43",
                              'city' : "Tacoma",
                              'state': "WA",
                              'zip': "93465"},
                 'email' : "FredJones@some_company.com",
                 'home_phone' : "510-555-1234",
                 'office_phone' : "564-466-7990",
                 'cell_phone' : "403-561-8911",
                 },
                
                {'first_name': "Nancy",
                 'last_name': "Wilson",
                 'address' : {'line_1':"8654 Walnut St",
                              'line_2' : "Suite 567",
                              'city' : "Pasadena",
                              'state': "CA",
                              'zip': "12345"},
                 'email' : "Wilson.Nancy@gmail.com",
                 'home_phone' : "423-321-9876",
                 'office_phone' : "123-765-9877",
                 'cell_phone' : "432-567-8466",
                 },
                ]

