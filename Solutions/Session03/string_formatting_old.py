#!/usr/bin/env python

"""
String formatting lab:

This version using "old style" formatting

Still pretty hand, and while less flexible, also a bit simpler
"""
# Rewrite: "the first 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:

# create the numbers
numbers = [32, 56, 34, 12, 48, 18]

# build the format string for the numbers:
formatter = ("%i, " * len(numbers))[:-2]  # take the extra comma and space off the end

# or use join():
#formatter = ", ".join(["%i"] * len(numbers))

# put it together with the rest of the string
formatter = "the first %i numbers are: %s" % (len(numbers), formatter)

# use it:
# the format operator needs a tuple
# tuple(seq) will make a tuple out of any sequence
print(formatter % tuple(numbers))

# solution 2
# in class, a couple people realized that str() would make a nice string from
# a list or tuple

numbers_str = str(numbers)[1:-1]  # make a string, remove the brackets
# put it together with the rest of the string
print("the first %i numbers are: %s" % (len(numbers), numbers_str))

#####
# Write a format string that will take:
#        ( 2, 123.4567, 10000)
#        and produce:
#        'file_002 :   123.46, 1e+04'
#####

t = (2, 123.4567, 10000)
print("file_%03i : %10.2f, %.3g" % t)

# could use '%e' for the last one, too -- I like '%g' --
# it does significant figures...
