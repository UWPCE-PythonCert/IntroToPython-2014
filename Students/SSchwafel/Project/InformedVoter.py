#!/usr/bin/python

from __future__ import unicode_literals 
from pprint import pprint
import simplejson as json
import sys
import urllib2

#This allows printing to the console, including being able to pipe ( | ) the input
reload(sys)
sys.setdefaultencoding("utf-8")

#Making sure that there is at least one command line argument, if not, is none
if len(sys.argv) == 1:
    command_line_argument = None
else:
    command_line_argument = sys.argv[1]

#Finds out the user's IP address for lookup
user_local_data = json.load(urllib2.urlopen('http://api.ipinfodb.com/v3/ip-city/?key=a648bf3844359d401197bcaa214dd01e0f8c0c6d623ec57f3716fbcafc8262bd&format=json'))

#Set variables for detected lat/long
user_lat = user_local_data['latitude']
user_long = user_local_data['longitude']

#lat_long_url = 'https://congress.api.sunlightfoundation.com/districts/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)

#Look up legislators from API with given lat/long, then store in a var. for later use
legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))


#Remnant of abandoned functionality
def find_legislators():
    """This function returns the legislator's last name and unique bioguide id, this would be useful for further, unimplemented features"""
    for i in legislators['results']:
        print '{} {}'.format(i['last_name'], i['bioguide_id'])

def print_all_legislators():
    """This function prints all the legislators, then formats according to gender and title"""
    
    legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators?per_page=all&apikey=15f4679bdc124cd6a2c6be8666253000'))
    for i in legislators['results']:

        if i['chamber'] == 'house' and i['gender'] == 'M':
            print 'Congressman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        if i['chamber'] == 'house' and i['gender'] == 'F':
            print 'Congresswoman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        elif i['chamber'] == 'senate':
            print 'Senator {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )

def print_manual_legislators():
    """This function prints the legislators of the given lat/long, then formats according to gender and title"""
    
    print """
    
    You can get your latitude and longitude from http://www.latlong.net/
    
    """

    user_lat = raw_input('Please enter your Latitude: \n') 
    user_long = raw_input('Please enter your Longitude: \n')

    legislators = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/legislators/locate?latitude={}&longitude={}&apikey=15f4679bdc124cd6a2c6be8666253000'.format(user_lat, user_long)))
    
    for i in legislators['results']:

        if i['chamber'] == 'house' and i['gender'] == 'M':
            print 'Congressman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        if i['chamber'] == 'house' and i['gender'] == 'F':
            print 'Congresswoman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        elif i['chamber'] == 'senate':
            print 'Senator {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )

def print_detected_legislators():
    """This function prints the legislators local to the IP address of the user, then formats according to gender and title"""
    for i in legislators['results']:

        if i['chamber'] == 'house' and i['gender'] == 'M':
            print 'Congressman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        if i['chamber'] == 'house' and i['gender'] == 'F':
            print 'Congresswoman {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )
        elif i['chamber'] == 'senate':
            print 'Senator {} {} - {} \nPhone: {}\nWebsite: {}\n'.format(i['first_name'],i['last_name'],i['party'],i['phone'],i['website'] )

if command_line_argument == '--all-legislators':
    print_all_legislators()

elif command_line_argument == None:
    print 'Based on the latitude and longitude detected, your United States Congresspeople are: \n'
    print_detected_legislators()

elif command_line_argument == '--manual':
    print_manual_legislators()

