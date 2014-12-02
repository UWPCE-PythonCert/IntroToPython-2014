#!/usr/bin/python

from pprint import pprint
import urllib2
import simplejson as json

##url = urlopen('https://www.govtrack.us/api/v2/vote?created__gt=2012-01-01T00:00:00')
url = 'https://www.govtrack.us/api/v2/bill'

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
#url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))
print type(data)

pprint(data)

#for key in data.keys():
#    print "{}  :  {}\n".format(key,data[key])
