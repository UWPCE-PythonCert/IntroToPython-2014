#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import math


from circle import Circle
#from circle_solution1 import Circle


def test_create():
    c = Circle(4)

    assert c.radius == 4


def test_change_radius():
    c = Circle(3)
    c.radius = 4

    assert c.radius == 4


def test_diameter():
    c = Circle(4)

    assert c.diameter == 8


def test_change_diameter():
    c = Circle(2)

    assert c.radius == 2
    assert c.diameter == 4

    c.diameter = 6
    assert c.radius == 3
    assert c.diameter == 6


def test_area():
    c = Circle(4)

    assert c.area == math.pi*16


def test_set_area():
    c = Circle(4)

    with pytest.raises(AttributeError):
        c.area = 44


## the extra credit: classmethod:

# def test_alternate_constructor():
#   c = Circle.from_diameter(8)

#   assert c.diameter == 8
#   assert c.radius == 4
