from circle import Circle

from math import isclose, pi

def test_init():
    assert Circle(15)


def test_radius():
    c = Circle(15)
    assert c.radius == 15


def test_diameter():
    c = Circle(5)
    assert c.diameter == 10


def test_diameter2():
    c = Circle(5)
    c.radius = 4
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1


def test_area():
    c = Circle(2)
    assert c.area == pi * 4
    assert isclose(c.area, 12.56637, rel_tol=1e-6)


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.radius == 4


def test_str():
    c = Circle(4)
    assert str(c) == "Circle with radius: 4"


def test_repr():
    c = Circle(4)
    assert repr(c) == "Circle(4)"


def test_add():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1 + c2 == "Circle(6)"


def test_multiply():
    c = Circle(4)
    assert c * 3 == "Circle(12)"


def test_equal_to():
    c1 = Circle(4)
    c2 = Circle(4)
    assert c1 == c2


def test_not_equal_to():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1 != c2


def test_gt():
    c1 = Circle(4)
    c2 = Circle(2)
    assert c1 > c2


def test_lt():
    c1 = Circle(4)
    c2 = Circle(6)
    assert c1 < c2

