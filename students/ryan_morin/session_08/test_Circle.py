__author__ = 'ryan.morin'

#!/usr/bin/env python3

from Circle import Circle

from math import pi

def test_init():
    C = Circle(4)

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

def test_diameter2():
    c = Circle(4)
    c.radius = 2
    assert c.diameter == 4

def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

def test_area():
    c = Circle(2)
    print(c.area)
    assert c.area == pi*4

def test_alt_constr():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

def test_add():
    c1 = Circle(4)
    c2 = Circle(10)
    assert c1 + c2 == 14

def test_multi():
    c1 = Circle(4)
    assert c1 * 10 == 40

def test_grtr():
    c1 = Circle(9)
    c2 = Circle(15)
    assert c2 > c1

def test_eql():
    c1 = Circle(18)
    c2 = Circle(8)
    assert (c1 == c2 ) is False