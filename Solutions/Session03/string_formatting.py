#!/usr/bin/env python

"""
String formatting lab:

This version using the format() method

"""
# Rewrite: "the first 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:

# create the numbers
numbers = (32, 56, 34, 12, 48, 18)

# build the format string for the numbers:
formatter = ", ".join(["{:d}"] * len(numbers))

# put it together with the rest of the string
formatter = "the first {0:d} numbers are: {1}".format(len(numbers), formatter)

# use it:
# * unpacks a sequence into the arguments of a function -- we'll get to that!
print(formatter.format(*numbers))

# solution 2
# in class, a couple people realized that str() would make a nice string from
# a list or tuple

numbers_str = str(numbers)[1:-1]  # make a string, remove the brackets
# put it together with the rest of the string
print("the first {:d} numbers are: {}".format(len(numbers), numbers_str))

#####
# Write a format string that will take:
#        ( 2, 123.4567, 10000)
#        and produce:
#        'file_002 :   123.46, 1e+04'
#####

print("file_{:03d} : {:10.2f}, {:.3g}".format(2, 123.4567, 10000))

# could use '{:.3e}' for the last one, too -- I like '%g' --
#         it does significant figures...
