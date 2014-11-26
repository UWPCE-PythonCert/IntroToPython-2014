#!/usr/bin/python

import random

#opens sherlock.txt
book=open('sherlock.txt','U').read()
text=book.split()

#creates dictionary
collection={}

#converts text to dictionary
for x in range(len(text)):
        try:
            if not text[x]+' '+text[x+1] in collection:
                collection[text[x]+' '+text[x+1]]=text[x+2].split()
            else:
                collection[text[x]+' '+text[x+1]]+=text[x+2].split()
        except IndexError:
            print 'done'

#generates new text            
first = random.choice(collection.keys())
temp = first+' '+random.choice(collection[first])
temp2 = temp.split()
x=0

#iterates through dictionary and creates new text
while x!=1:
        try:
            temp2+=random.choice(collection[temp2[-2]+' '+temp2[-1]]).split()
        except KeyError:
            print ' '.join(temp2)
            x=1
