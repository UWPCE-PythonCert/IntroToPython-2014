'''
Created on Nov 18, 2014

@author: Aleksey
'''

from circle import Circle
from math import pi
import pytest

def test_init():
    c = Circle(3)
    c.radius = 4
    
def test_radius():
    c = Circle(3)
    assert c.radius == 3
    
def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()
        c.radius = 4

def test_set_radius():
    c = Circle(3)
    c.radius = 5
    assert c.radius == 5

def test_diam():
    c = Circle(3)
    assert c.diameter == 6

def test_change_diameter():
    c = Circle(3)
    c.radius = 4
    assert c.diameter == 8
    
def test_change_diameter_float():
    c = Circle(4)
    c.diameter = 11
    assert c.diameter == 11
    assert c.radius == 5.5

def test_area():
    c = Circle(2)
    assert c.area == pi * c.radius**2.0

def test_set_area():
    c = Circle(4)
    with pytest.raises(AttributeError):
        c.area = 3

def test_from_diameter():
    c = Circle.from_diameter(4)
    assert isinstance(c, Circle)
    assert c.diameter == 4
    assert c.radius == 2
    
def test_repr():
    c = Circle(6)
    assert repr(c) == 'Circle(6.0)'

def test_equal():
    c = Circle(4)
    c1 = Circle(4)
    assert c == c1

def test_not_equal():
    c = Circle(4)
    c1 = Circle(8)
    assert c != c1

def test_less_than():
    c = Circle(4)
    c1 = Circle(8)
    return c < c1

def test_greater_than():
    c = Circle(4)
    c1 = Circle(8)
    return c1 > c

def test_radd():
    c = Circle(4)
    assert c.radius + 4 == 4 + c.radius
    
def test_rmul():
    c = Circle(4)
    assert c.radius * 4 == 4 * c.radius  



    