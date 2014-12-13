# @python: 2
"""
test_circle.py

"""

from circle import Circle
import pytest
from math import pi


def test_init():
    Circle(3)


def test_radius():
    c = Circle(3)
    assert c.radius == 3


def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()  #creates a TypeError, this is intentional so we handle with 'raises'


def test_set_radius():
    c= Circle(3)
    c.radius = 5
    assert c.radius == 5


def test_diam():
    c = Circle(3)
    assert c.diameter == 6


def test_radius_change():  #does diameter change when radius changes?
    c = Circle(3)
    c.radius = 4
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10

    assert c.diameter == c.radius * 2
    assert c.diameter == 10


def test_set_diam_float():
    c = Circle(4)
    c.diameter = 11

    assert c.radius == 5.5
    assert c.diameter == 11


def test_area():
    c = Circle(2)

    assert c.area == pi * 4


def  test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 30


def test_from_diameter():
    c = Circle.from_diameter(4)  # should create instance of circle class

    assert c.radius == 2
    assert c.diameter == 4
    assert isinstance(c, Circle)


# Step 6 at this point


def test_repr():
    c = Circle(6)

    assert repr(c) == 'Circle(6.0)'


def  test_str():
    c = Circle(4)
    s = 'Circle with radius: 4.00'
    cs = c.__str__()  # note, must perform bound method call with ()
    assert s == cs


def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(6)

    # note that we must compare radii since no == magic property exists
    assert c1.radius + c2.radius == c3.radius


def test_mul():
    c1 = Circle(4)
    n = 3
    c2 = c1 * n

    assert c2.radius == c1.radius * n

def test_eq():
    c1 = Circle(2)
    c2 = Circle(2)

    assert c1 == c2

def test_lt():
    c1 = Circle(4)
    c2 = Circle(2)

    assert c2 < c1

def test_gt():
    """tests that functools created greater than from existing properties"""
    c1 = Circle(4)
    c2 = Circle(2)

    assert c1 > c2

def test_csort():
    c1 = Circle(1)
    c2 = Circle(2)
    c3 = Circle(3)
    c4 = Circle(4)
    c5 = Circle(5)

    clist = [c5, c2, c3, c1, c4]
    clist.sort()
    assert clist == [c1, c2, c3, c4, c5]

# Step 8 testing: Optional Features

#reflected multiplication using __rmul__
def test_rmul():
    c1 = Circle(5)
    n = 3

    assert c1 * n == n * c1

# division is order specific, so it doesn't make sense to reflect it

#augmented assignment operator
def test_iadd():
    c1 = Circle(5)
    c2 = Circle(4)

    c1 += c2

    assert c1.radius == 9

