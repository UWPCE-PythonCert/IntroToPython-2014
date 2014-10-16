#!/usr/bin/env python
"""code that tests the circle class defined in circle.py

This version adds more tests

can be run with py.test
"""
import math
import pytest  # used for the exception testing


from circle import Circle


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

## the magic methods:

def test_str():
    c = Circle(3)

    assert str(c) == 'Circle with radius: 3.000000'


def test_repr():
    c = Circle(3)

    assert repr(c) == 'Circle(3)'


def test_addition():
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2

    assert c3.radius == 5


def test_multiplication():
    c1 = Circle(2)
    c3 = c1 * 4

    assert c3.radius == 8


def test_equal():
    c1 = Circle(3)
    c2 = Circle(3.0)

    assert c1 == c2
    assert c1 <= c2
    assert c1 >= c2


def test_not_equal():
    c1 = Circle(2.9)
    c2 = Circle(3.0)

    assert c1 != c2


def test_greater():
    c1 = Circle(2)
    c2 = Circle(3)

    assert c2 > c1
    assert c2 >= c1


def test_less():
    c1 = Circle(2)
    c2 = Circle(3)

    assert c1 < c2
    assert c1 <= c2
