#!/usr/bin/env python

"""
script to determine what programming languages students came to this clas iwth
"""

file_path = '../../Examples/Session01/students.txt'

all_langs = set() # use a set to ensure unique values

f = open(file_path) # default read text mode

f.readline() # read and toss the header

for line in f:
    langs = line.split(':')[1]
    langs = langs.split(',')
    for lang in langs:
        lang = lang.strip().lower()
        if lang: # don't want empty strings
            all_langs.add(lang)
for lang in all_langs:
    print lang
