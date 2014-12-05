#!/usr/bin/env python2.7

# This is really ugly right now. No functions, light on comments,
# but it appears to work ok.  I will clean up a bit if I have time
# this week.

import string
import sys
import random

allwords = []
strip = string.whitespace + string.punctuation + "\"'"

# read in the file and store words in file as a list
for filename in sys.argv[1:]:
    for line in open(filename):
        cleanline = line.lower().split()
        if(len(cleanline) != 0):
            for word in cleanline:
                allwords.append(word.strip(strip))

# build the trigram
trigram = {}
for i in range( len(allwords) - 3 ):
    keytuple = (allwords[i], allwords[i+1])
    if(keytuple in trigram):
        trigram[keytuple].append(allwords[i+2])
    else:
        trigram.update({ keytuple : [ allwords[i+2] ] })

# begin with a random key
random_beginning = random.choice(trigram.keys())

newtext = []
for word in random_beginning:
    newtext.append(word)
newtext.append( random.choice( trigram[random_beginning] ) )

for keys in trigram.keys():
    keytuple = (newtext[-2], newtext[-1])
    newtext.append( random.choice( trigram[keytuple] ) )

# textstring = " ".join(newtext)

for i, word in enumerate(newtext):
    if (i%20 == 0):
        print 
    elif (i%250 == 0):
        print "\n"
    else:
        print word,

# for k, v in trigram.items():
#     for word in k:
#         print word,
#     print ": ", v
