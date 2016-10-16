#!/usr/bin/env python

"""
String formatting lab:

This version using the format() method

"""

#####
# Write a format string that will take:
#        ( 2, 123.4567, 10000)
#        and produce:
#        'file_002 :   123.46, 1.00e+04'
#####

print("file_{:03d} : {:10.2f}, {:.2g}".format(2, 123.4567, 10000))

# could use '{:.2e}' for the last one, too -- I like '%g' --
#         it does significant figures...

#######################
# Rewrite: "the 3 numbers are: %i, %i, %i"%(1,2,3)
#          for an arbitrary number of numbers...

# solution 1
# the goal was to demonstrate dynamic building of format strings:


def formatter(t):
    fstring = "the {:d} numbers are: ".format(len(t))
    fstring += ", ".join(['{:d}'] * len(t))
    # * unpacks a sequence into the arguments of a function -- we'll get to that!
    return fstring.format(*t)

# call it with a couple different tuples of numbers:
formatter((2, 3, 5))

formatter((2, 3, 5, 7, 9))

# solution 2
# some of you realized that str() would make a nice string from
# a list or tuple

numbers = (34, 12, 3, 56)

numbers_str = str(numbers)[1:-1]  # make a string, remove the brackets

# put it together with the rest of the string
print("the first {:d} numbers are: {}".format(len(numbers), numbers_str))
