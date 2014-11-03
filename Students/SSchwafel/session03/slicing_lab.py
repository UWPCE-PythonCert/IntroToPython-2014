#!/usr/bin/python

user_string = raw_input("Hey, gimme a string\t ")


def switch_first_last(x):

    """Return a string with the first and last letters exchanged"""

    first =  x[0]
    last = x[-1]

    return str(last) + str(x[1:-2]) +  str(first)

#print switch_first_last(user_string)

def remove_every_other(x):

    """return a string with every other character removed"""
    return x[::2]

#print remove_every_other(user_string)

def remove_firstlastfour(x):

    """Return a string with the first and last 4 characters removed, and every other char in between
"""

    x = x[4:-4] 
    length = len(x)

    return x[0:length:2]

#print remove_firstlastfour(user_string)

def reverse_string(x):

    """return a string reversed (just with slicing)
"""

    return x[::-1]

def return_middle_last_third(x):

    divisor = len(x)/3

    first_third = x[0:divisor]

    middle_third = x[divisor:divisor+divisor]

    final_third = x[-divisor:]
    print middle_third + final_third + first_third


print return_middle_last_third(user_string)
