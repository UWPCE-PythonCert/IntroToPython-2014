#!/usr/bin python3

"""
Simple factorial function -- to demostrate recursion
"""


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
