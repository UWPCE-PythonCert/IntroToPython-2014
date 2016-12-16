#!/usr/bin/env python

"""
Example code for closures / currying
"""

from functools import partial


def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]
    return incr


def power(base, exponent):
    """returns based raised to the given exponent"""
    return base ** exponent

# now some specialized versions:

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
