#!/usr/bin/env python

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
        c = Circle()


def test_set_radius():
    c = Circle(3)
    c.radius = 5
    assert c.radius == 5


def test_diam():
    c = Circle(3)

    assert c.diameter == 6


def test_radius_change():

    c = Circle(3)
    c.radius = 4
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10

    assert c.radius == 5
    assert c.diameter == 10


def test_set_diameter_float():
    c = Circle(4)
    c.diameter = 11

    assert c.radius == 5.5
    assert c.diameter == 11


def test_area():
    c = Circle(2)

    assert c.area == pi*4


def test_set_area():
    c = Circle(2)
    with pytest.raises(AttributeError):
        c.area = 30


def test_from_diameter():
    c = Circle.from_diameter(4)

    assert isinstance(c, Circle)
    assert c.radius == 2
    assert c.diameter == 4


def test_repr():
    c = Circle(6.0)

    assert repr(c) == 'Circle(6.0)'

