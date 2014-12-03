__author__ = 'Ari'

# first step in test, import!

from circle import Circle
import pytest
import math

def test_init():
    """
    this will fail if there is no initializer (self)
    and the class Circle(object):
    """
    Circle(3)

def test_no_radius():
    with pytest.raises(TypeError):
        c = Circle()

def test_set_radius():
    c = Circle(3)
    c.radius = 5
    assert c.radius == 5

def test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 30


