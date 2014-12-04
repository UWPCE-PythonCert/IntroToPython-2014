#!/usr/bin/python

from pprint import pprint
import urllib2
import simplejson as json

#Bills
#url = 'https://www.govtrack.us/api/v2/bill'


#Current Members of Congress
url = 'https://www.govtrack.us/api/v2/role?current=true'

#One Particular Congressman
#url = 'https://www.govtrack.us/api/v2/person/400054'
# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))
#print data["lastname"]
#print data

objects = data['objects']
for representative in objects:
    print representative['person']['name'].encode('utf-8')
#pprint(data)

