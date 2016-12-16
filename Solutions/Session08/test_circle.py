"""
tests for circle class
"""

import math
import pytest
from circle import Circle, Sphere

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(5)

    assert c.diameter == 10

def test_change_radius():
    c = Circle(5)
    c.radius = 2
    assert c.diameter == 4

def test_change_diameter():
    c = Circle(5)
    c.diameter = 12
    assert c.diameter == 12
    assert c.radius == 6

def test_area():
    c = Circle(4)
    assert c.area == math.pi * 4**2

    with pytest.raises(AttributeError):
        c.area = 45

def test_from_diameter():
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4

def test_str():
    c = Circle.from_diameter(8)

    assert str(c) == "A circle object with radius: 4.0"


def test_sphere():
    s = Sphere(4)

    print(s.volume())
    assert s.volume() == 268.082573106329

def test_sphere_diamter():
    s = Sphere.from_diameter(8)

    print(s.volume())
    assert s.volume() == 268.082573106329

def test_sphere_area():
    s = Sphere(4)

    with pytest.raises(NotImplementedError):
        a = s.area()

def test_add():
    c2 = Circle(2)
    c4 = Circle(4)

    c6 = c2 + c4

    assert c6.radius == 6

def test_mul():
    c2 = Circle(2)

    c6 = c2 * 3

    assert c6.radius == 6

def test_rmul():
    c2 = Circle(2)

    c6 = 3 * c2

    assert c6.radius == 6

