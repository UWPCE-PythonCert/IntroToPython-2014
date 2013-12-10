#!/usr/bin/env python

"""
Example of how to save custom classes in a pickle
"""

import cPickle as pickle

outfilename = "circles.pickle"

### You can pickle a custom class, too:
# remember the Circle class?
    
import circle

# create a couple of circles:

C1 = circle.Circle(radius=2)
print C1        

C2 = circle.Circle(radius=3.4)
print C2        

# put them in a dict:
circles = {'circle1': C1,
           'circle2': C2}    

#print circles

## pickle the list 
pickle.dump(circles, open(outfilename, 'wb') )

### see if we can re-load it

## Note: the circle module needs to be available when you load the pickle
circles2 = pickle.load( open(outfilename, 'rb') )

# Haven't defined compare for the circle class:
## extra credit -- add compare method (__cmp__) to Circle class
same = True
for c1, c2 in zip(circles.values(), circles2.values()):
    if c1.radius != c2.radius:
        same = False
        break

if same:
    print "pickled/unpickled version is  the same as the original"
else:
    print "not the same"
    print circles
    print circles2