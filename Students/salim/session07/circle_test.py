#!usr/local/bin/python
from circle import Circle
from math import pi


def test_circle_class():
    c = Circle(2)
    assert isinstance(c, Circle)


def test_radius():
    c = Circle(2.0)
    assert c.radius == 2.0


def test_get_diameter():
    c = Circle(2.5)
    assert c.diameter == 5.0


def test_set_diameter():
    c = Circle(4.3)
    c.diameter = 3.0
    assert c.radius == 1.5
    assert c.diameter == 3.0


def test_area():
    c = Circle(10)
    assert c.area == pi * 10 ** 2


def test_set_area():
    c = Circle(4)
    try:
        c.area = 10
    except AttributeError as error:
        assert error.message == "can't set attribute"
    else:
        assert False


def test_from_diameter():
    c = Circle.from_diameter(10)
    assert isinstance(c, Circle)
    assert c.radius == 5.0


def test_print_circle():
    c_int = Circle(3)
    c_float = Circle(3.50)
    assert str(c_int) == 'Circle with radius: 3.00'
    assert str(c_float) == 'Circle with radius: 3.50'


def test_repr():
    c = Circle(3)
    assert repr(c) == 'Circle(3)'


def test_add():
    a = Circle(10)
    b = Circle(15)
    assert isinstance(a + b, Circle)
    assert (a + b).radius == Circle(25).radius


def test_multiply():
    a = Circle(10)
    c_mult = a * 3
    assert isinstance(c_mult, Circle)
    assert c_mult.radius == 30

    c2_mult = 4 * a
    assert isinstance(c2_mult, Circle)
    assert c2_mult.radius == 40


def test_compare_circle():
    a3 = Circle(3)
    b3 = Circle(3)
    c5 = Circle(5)
    d10 = Circle(10)
    e3f = Circle(3.0)
    assert not a3 > b3
    assert c5 > b3
    assert not c5 < b3
    assert a3 < d10
    assert a3 == b3
    assert not d10 == c5


def test_sort():
    c_list = [Circle(6), Circle(7), Circle(15), Circle(1), Circle(6.5)]
    c_list.sort()

    sorted_list = [Circle(1), Circle(6), Circle(6.5), Circle(7), Circle(15)]
    assert c_list[0].radius == sorted_list[0].radius
    assert c_list[1].radius == sorted_list[1].radius
    assert c_list[2].radius == sorted_list[2].radius
    assert c_list[3].radius == sorted_list[3].radius
    assert c_list[4].radius == sorted_list[4].radius
