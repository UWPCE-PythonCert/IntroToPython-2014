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
        c = Circle()  #creates a TypeError, that is intentional so we handle with  'raises'

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
    c=Circle(4)
    c.diameter = 11

    assert c.radius == 5.5
    assert c.diameter == 11

def test_area():
    c = Circle(2)

    assert c.area == pi * 4

def  test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area =30

def test_from_diameter():
    c = Circle.from_diameter(4)  # should create instance of circle class

    assert c.radius == 2
    assert c.diameter == 4
    assert isinstance(c, Circle)

# Step 6 at this point
 
def test_repr():
    c = Circle(6)

    assert repr(c) == 'Circle(6.0)'