#!/usr/bin/env python

"""
This is from CodingBat "count_evens" (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even ints in the given array.
"""


def count_evens(arr):
    return len( [i for i in arr if not i%2] )

