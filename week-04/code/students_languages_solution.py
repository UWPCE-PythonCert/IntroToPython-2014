#!/usr/bin/env python
"""
simple script to extract a list of languages that the students have used in the past.

This script parses the text file created on the first day of class.
""" 

infile = open("../../week-01/code/students.txt")

languages = set() # use a set to store -- order doesn't matter, and we don't want duplicates

infile.readline() # skip the first line
for line in infile:
    langs = line.split(':')[1]
    langs = langs.split(',')
    for lang in langs:
        lang = lang.strip()
        lang = lang.lower() # case doesn't matter
        if lang:
            languages.add(lang)
languages = list(languages) # so we can sort it
languages.sort()

print "The programming languages previously used by students are:"
for lang in languages:
    print lang





