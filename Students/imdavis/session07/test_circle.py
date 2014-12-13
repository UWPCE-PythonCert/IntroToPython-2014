#!/usr/bin/env python2.7

from circle import Circle
import pytest
from math import pi

def test_init():
    Circle(3)

def test_radius():
    c = Circle(3)
    assert c.radius == 3

# radius is a required parameter
def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()

# make sure we cannot set the area
def test_no_set_area():
    c = Circle(4.52)
    with pytest.raises(AttributeError):
        c.area = 5.67

def test_set_radius():
    c = Circle(3)
    c.radius = 5
    assert c.radius == 5

def test_diam():
    c = Circle(2.5)
    assert c.diameter == 5.0

def test_radius_chage():
    c = Circle(3) 
    c.radius = 4
    assert c.diameter == 8

def test_set_diamter():
    c = Circle(4)
    c.diameter = 11
    assert c.radius == 5.5
    assert c.diameter == 11

def test_area():
    c = Circle(2.45)
    assert c.area == pi*2.45**2

def test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 30.122 

def test_from_diameter():
    c = Circle.from_diameter(4)
    assert isinstance(c, Circle)
    assert c.radius == 2
    assert c.diameter == 4
    assert c.area == pi*2**2

def test_repr():
    c = Circle(6)
    assert repr(c) == "Circle(6.0)"

def test_str():
    c = Circle(4.32)
    assert c.__str__() == "Circle with radius 4.32"
    assert str(c) == "Circle with radius 4.32"

def test_add_circle():
    c1 = Circle(14.34)
    c2 = Circle(1.15)
    c3 = c1 + c2
    assert isinstance(c3, Circle)
    assert c3.radius == 15.49
    assert c3.diameter == 30.98
    c1 += c2
    assert c1.radius == 15.49

def test_mult_circle():
    c1 = Circle(2.34)
    c2 = Circle(5.67)
    c3 = c1 * c2
    assert isinstance(c3, Circle)
    assert c3.radius ==13.2678
    c3 = c2 * c1
    assert c3.radius ==13.2678
    c3 = c1 * 1.2
    assert isinstance(c3, Circle)
    assert c3.radius == 2.808
    c3 = 1.2 * c1
    assert c3.radius == 2.808

def test_gt():
    c1 = Circle(2.34)
    c2 = Circle(5.67)
    assert c2 > c1
    assert (c1 > c2) == False

def test_lt():
    c1 = Circle(2.34)
    c2 = Circle(5.67)
    assert c1 < c2
    assert (c2 < c1) == False

def test_eq():
    c1 = Circle(2.34)
    c2 = Circle(5.67)
    assert (c1 == c2) == False
    c2 = Circle(2.34)
    assert c1 == c2

def test_ne():
    c1 = Circle(2.34)
    c2 = Circle(5.67)
    assert c1 != c2
    assert (c1 == c2) == False
    c2 = Circle(2.34)
    assert c1 == c2

def test_nonsense_radius():
    """
    Make sure we can't create a Circle object with a negative or zero 
    radius.
    """
    with pytest.raises(ValueError):
        c = Circle(-1.234)
    with pytest.raises(ValueError):
        c = Circle(0)
    c = Circle(1.234)
    with pytest.raises(ValueError):
        c.radius = -1.234 
    with pytest.raises(ValueError):
        c.radius = 0

def test_nonsense_diameter():
    """
    Make sure we can't create a Circle object with a negative or zero 
    diameter.
    """
    with pytest.raises(ValueError):
        c = Circle.from_diameter(-2.468)
    with pytest.raises(ValueError):
        c = Circle.from_diameter(0)
    c = Circle.from_diameter(2.468)
    with pytest.raises(ValueError):
        c.diameter = -2.468
    with pytest.raises(ValueError):
        c.diameter = 0
