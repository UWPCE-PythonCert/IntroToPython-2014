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
legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators?per_page=all&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))

#pprint(senators['results'])
#print 'Based on the latitude and longitude provided, your United States Congresspeople are: \n'


#Prints Congressman/Congresswoman + First, Last

def find_legislators():

    for i in legislators['results']:
        print i['last_name'] + ' ' + i['bioguide_id']
        #legislator_ids.append(i)

#find_legislators()

#votes_url = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/votes?voter_ids.{}__exists=true&apikey=15f4679bdc124cd6a2c6be8666253000')).format( __ THIS IS WHERE THE UNIQUE ID OF THE LEGISLATOR NEEDS TO BE __ )

#pprint(votes_url)

#def recent_votes():

   ##THIS IS WHERE YOU ARE GOING TO RETURN THE LAST 10 VOTES BY var = LEGISLATOR 

def print_legislators():

    #FIX THE FORMATTING BELOW!!!
    #Also, be sure to add  .encode('utf-8')

    for i in legislators['results']:
        if i['chamber'] == 'house' and i['gender'] == 'M':
            print 'Congressman ' + i['first_name'] + ' ' + i['last_name'] + ' - ' + i['party']+ '\n' + 'Phone: ' + i['phone'] + '\n' + 'Website: ' + i['website'] + '\n'
        if i['chamber'] == 'house' and i['gender'] == 'F':
            print 'Congresswoman ' + i['first_name'] + ' ' + i['last_name'] + ' - ' + i['party']+ '\n' + 'Phone: ' + i['phone'] + '\n' + 'Website: ' + i['website'] + '\n'
        elif i['chamber'] == 'senate':
            print 'Senator ' + i['first_name'] + ' ' + i ['last_name'] + ' - ' + i['party']+ '\n' + 'Phone: ' + i['phone'] + '\n' + 'Website: ' + i['website'] + '\n'

print_legislators()
