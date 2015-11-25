from math import isclose, pi
import circle_lab as cl


def test_init():
    c = cl.Circle(4)


def test_radius():
    c = cl.Circle(4)
    assert c.radius == 4


def test_diameter():
    c = cl.Circle(4)
    assert c.diameter == 8


def test_diameter2():
    c = cl.Circle(4)
    c.radius = 2
    assert c.diameter == 4


def test_diameter_setter():
    c = cl.Circle(4)
    c.diameter = 4
    assert c.diameter == 4
    assert c.radius == 2


def test_area():
    c = cl.Circle(2)
    assert isclose.area(c.area, 12.56673, rel_tol=1e-05)
    assert c.area == pi*4

'''
FOR REFERENCE: math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

Return True if the values a and b are close to each other and
False otherwise.

Whether or not two values are considered close is determined
according to given absolute and relative tolerances.

rel_tol is the relative tolerance – it is the maximum allowed difference
between a and b, relative to the larger absolute value of a or b. For
example, to set a tolerance of 5%, pass rel_tol=0.05. The default
tolerance is 1e-09, which assures that the two values are the same
within about 9 decimal digits. rel_tol must be greater than zero.
'''