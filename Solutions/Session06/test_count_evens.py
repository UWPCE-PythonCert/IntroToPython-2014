#!/usr/bin/env python

"""
test code for count_evens.py

can be run with py.test or nose
"""

from count_evens import count_evens


def test_1():
    assert count_evens([2, 1, 2, 3, 4]) == 3


def test_2():
    assert count_evens([2, 2, 0]) == 3


def test_3():
    count_evens([1, 3, 5, -9, -3]) == 0

def test_4():
    count_evens([1, 3, 5, -9, -3, -4, -2]) == 2
