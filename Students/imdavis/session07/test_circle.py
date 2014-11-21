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
    assert repr(c) == 'Circle(6.0)'