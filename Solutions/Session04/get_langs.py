#!/usr/bin/env python

"""
script to determine what programming languages students came to this class with
"""

infilename = "students.txt"

all_langs = set()  # use a set to ensure unique values

f = open(infilename)  # default read text mode

f.readline()  # read and toss the header

for line in f:
    langs = line.split(':')[1]  # toss the names
    # a bit of cleanup:
    langs = langs.replace(',', ' ')
    langs = langs.replace('and', ' ')
    langs = langs.split()  # separate the languages
    for lang in langs:
        lang = lang.strip().capitalize()  # clean them up -- and make case the same
        if lang:  # don't want empty strings
            all_langs.add(lang)
for lang in all_langs:
    print(lang)

# extra credit version: using collections.Counter:
from collections import Counter

all_langs = Counter()

f = open(infilename)  # default read text mode
f.readline()  # read and toss the header

for line in f:
    langs = line.split(':')[1]  # toss the names
    # a bit of cleanup:
    langs = langs.replace(',', ' ').replace('and', ' ')
    langs = langs.split()  # separate the languages
    for lang in langs:
        lang = lang.strip().capitalize()  # clean them up -- and make case the same
        if lang:  # don't want empty strings
            all_langs[lang] += 1

print("And now the counted version")
for lang, count in all_langs.items():
    print(lang, ":", count)
