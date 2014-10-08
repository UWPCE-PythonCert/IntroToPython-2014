#!/usr/bin/python

import webbrowser
from urllib import quote

a = raw_input('What are you tryna learn about? ')

basic_google = 'http://www.google.com/?#q='
google_plus_query = basic_google + quote(a)
webbrowser.open(google_plus_query, autoraise=True)

