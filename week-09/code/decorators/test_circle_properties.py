#!/usr/bin/env python

import math

import pytest

"""
code that tests the circle class defined in circle.py

designed to be run with py.test

(but most will run with nose, too)

"""

from circle_properties import Circle
#from circle_properties_solution import Circle


def test_basic():
    c = Circle(4)
    print "the radius:", c.radius    
    print "the diameter:", c.diameter
    print "the area:", c.area
    print "the repr():", repr(c)
    print "the str():", str(c)
    assert c.radius == 4
    assert c.diameter == 8
    assert round(c.area, 5) == 50.26548


def test_change_r():
    """
    testing changing the radius
    """    
    c = Circle(4)

    #"setting the radius to 2:"
    c.radius = 2
    assert c.radius == 2
    assert c.diameter == 4
    assert round(c.area, 5) == 12.56637

def test_change_d():
    """
    testing changing the diameter
    """    
    c = Circle(4)

    c.diameter = 4
    assert c.radius == 2
    assert c.diameter == 4
    assert round(c.area, 5) == 12.56637

## testing properties errors
## These require pytest

def test_delete():
    # trying to delete the diameter
    c = Circle(4)
    with pytest.raises(AttributeError):
        del c.diameter

def test_set_area():
    # trying to set the area
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 12

def test_add_circles():
    """
    testing the addition of two circle objects
    """    
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = c1 + c2 
    assert c3.radius == 6 
    assert c3.diameter == 12 

def test_repr():
    c = Circle(5)
    assert repr(c) == 'Circle(5.000000)'

def test_str():
    c = Circle(5)
    print str(c)
    assert str(c) == 'Circle Object with radius: 5.000000'

def test_from_diameter():
    c = Circle.from_diameter(6.0)
    assert c.radius == 3.0

def test_circumference():
    c = Circle.circumference(3.0)
    assert c == math.pi * 3.0 * 2
