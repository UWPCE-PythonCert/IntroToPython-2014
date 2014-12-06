#!/usr/bin/python

from pprint import pprint
import urllib2
import simplejson as json

#Bills
#url = 'https://www.govtrack.us/api/v2/bill'


#List Current Members of Congress
congresspeople_url = 'https://www.govtrack.us/api/v2/role?current=true&limit=600'

#One Particular Congressman
#url = 'https://www.govtrack.us/api/v2/person/400054'
# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(congresspeople_url))

objects = data['objects']
#for representative in objects:
#    print representative['person']['name'].encode('utf-8')
#pprint(objects[0][person]['sortname'])

representatives = []

for i in objects:
    representatives.append(i['person']['sortname'].encode('utf-8'))

#representatives = sorted(representatives)
#pprint(representatives)


print """

You can get your latitude and longitude from http://www.latlong.net/

"""

#user_lat = raw_input('Please enter your Latitude: \n') 
#user_long = raw_input('Please enter your Longitude: \n')

user_lat = '47.653098'
user_long = '-122.353731'

lat_long_url = 'https://congress.api.sunlightfoundation.com/districts/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)

congressional_district = json.load(urllib2.urlopen(lat_long_url))


legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))

#pprint(senators['results'])
print 'Based on the latitude and longitude provided, your United States Congresspeople are: \n'
for i in legislators['results']:
    first = i['first_name']
    last = i['last_name']
    print '{} {}\n'.format(first,last)
