#!/usr/bin/python

from pprint import pprint
import urllib2
import simplejson as json

user_local_data = json.load(urllib2.urlopen('http://freegeoip.net/json/'))

user_lat = user_local_data['latitude']
user_long = user_local_data['longitude']

#print gathered lat/long
#print user_lat,user_long

#print """
#
#You can get your latitude and longitude from http://www.latlong.net/
#
#"""

#user_lat = raw_input('Please enter your Latitude: \n') 
#user_long = raw_input('Please enter your Longitude: \n')

#user_lat = '47.653098'
#user_long = '-122.353731'

lat_long_url = 'https://congress.api.sunlightfoundation.com/districts/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)

congressional_district = json.load(urllib2.urlopen(lat_long_url))


legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))


#All Legislators, irrespective of location

#House only
#legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators?chamber=house&per_page=all&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))

#All Legislators
#legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators?per_page=all&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))

#pprint(senators['results'])
#print 'Based on the latitude and longitude provided, your United States Congresspeople are: \n'


#Prints Congressman/Congresswoman + First, Last

#for i in legislators['results']:
#    pprint(i)
for i in legislators['results']:
    if i['chamber'] == 'house' and i['gender'] == 'M':
        print 'Congressman ' + i['first_name'] + ' ' + i ['last_name'] + '\n'
    elif i['chamber'] == 'senate':
        print 'Senator ' + i['first_name'] + ' ' + i ['last_name'] + '\n'


#for i in legislators['results']:
#    first = i['first_name']
#    last = i['last_name']
#    print '{} {}\n'.format(first,last)
