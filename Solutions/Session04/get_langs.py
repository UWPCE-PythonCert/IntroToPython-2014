#!/usr/bin/env python

"""
script to determine what programming languages students came to this class with
"""

infilename = "students.txt"

# all_langs = set()  # use a set to ensure unique values

# with open(infilename) as f:  # default read text mode

#     f.readline()  # read and toss the header

#     # loop through the rest of the lines in the file
#     for line in f:
#         langs = line.split(':')[1]  # toss the names
#         # a bit of cleanup:
#         langs = langs.replace(',', ' ')
#         langs = langs.replace('and', ' ')
#         langs = langs.split()  # separate the languages
#         for lang in langs:
#             lang = lang.strip().capitalize()  # clean them up -- and make case the same
#             if lang:  # don't want empty strings
#                 all_langs.add(lang)

# # done reading the file -- no on to the rest
# for lang in all_langs:
#     print(lang)

# extra credit version: using collections.Counter:
# https://docs.python.org/3/library/collections.html#collections.Counter

from collections import Counter
all_langs = Counter()

# all_langs = {}

with open(infilename) as f:
    f.readline()  # read and toss the header

    for line in f:
        langs = line.partition(':')[2]  # get just what's after the colon
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
