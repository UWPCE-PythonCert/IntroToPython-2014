#!/usr/bin/env python

"""
script to determine what programming languages students came to this
class with

This version updated to use collections.Counter, to count and maintain
a set at the same time.

"""

import collections  # lots of neat stuff in there

file_path = '../../Examples/students.txt'

# use a counter to ensure unique values and keep track of count
all_langs = collections.Counter()

f = open(file_path)  # default read text mode

f.readline()   # read and toss the header

for line in f:
    langs = line.split(':')[1]
    langs = langs.split(',')
    for lang in langs:
        lang = lang.strip().lower()
        if lang:  # don't want empty strings
            all_langs[lang] += 1
for lang, count in all_langs.items():
    print("{:25}: {:d} students".format(lang, count))
