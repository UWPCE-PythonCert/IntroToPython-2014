#!/usr/bin/env python3

from circle import Circle

from math import isclose, pi

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
    assert isclose(c.area, 12.56637, rel_tol=1e-6)
    assert c.area == pi*4
