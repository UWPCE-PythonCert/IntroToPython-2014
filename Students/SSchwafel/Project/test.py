#!/usr/bin/python

from __future__ import unicode_literals 
from pprint import pprint
import urllib2
import simplejson as json

url = json.load(urllib2.urlopen('https://congress.api.sunlightfoundation.com/votes?fields=voters&apikey=15f4679bdc124cd6a2c6be8666253000'))
pprint(url)
