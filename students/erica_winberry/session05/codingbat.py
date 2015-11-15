#!/usr/bin/env python

"""
Examples from: http://codingbat.com

Put here so we can write unit tests for them ourselves
"""

# Python > Warmup-1 > sleep_in


def sleep_in(weekday, vacation):
    return not (weekday is True and vacation is False)


def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False


def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


def array_front9(nums):
    # Given an array of ints, return True if one of the first 4 elements
    # in the array is a 9. The array length may be less than 4.
    if 9 in nums[:4]:
        return True
    else:
        return False


def cat_dog(string):
    if string.count("cat") == string.count("dog"):
        return True
    else:
        return False


def make_bricks(small, big, goal):
    # We want to make a row of bricks that is goal inches long.
    # We have a number of small bricks (1 inch each) and big bricks
    # (5 inches each). Return True if it is possible to make the goal
    # by choosing from the given bricks. 
    if small + (big * 5) < goal:
        return False
    elif goal % 5 > small:
        return False
    else:
        return True
