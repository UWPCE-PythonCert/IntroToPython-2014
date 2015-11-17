import pytest

from math import sin
from functools import partial

from trapz import line, a_curve, another_curve, quadratic, trapz, quadratic_2, dynamic_trapz

# need a function for testing approximate equality
try:
    from math import isclose
except ImportError:  # only there in py3.5
    import math

    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        """
        Determine whether two floating point numbers are close in value.
        rel_tol
           maximum difference for being considered "close", relative to the
           magnitude of the input values
        abs_tol
           maximum difference for being considered "close", regardless of the
           magnitude of the input values
        Return True if a is close in value to b, and False otherwise.
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
        """

        if rel_tol < 0.0 or abs_tol < 0.0:
            raise ValueError('error tolerances must be non-negative')

        if a == b:  # short-circuit exact equality
            return True
        if math.isinf(a) or math.isinf(b):
            # This includes the case of two infinities of opposite sign, or
            # one infinity and one finite number. Two infinities of opposite sign
            # would otherwise have an infinite relative tolerance.
            return False
        diff = abs(b - a)
        return (((diff <= abs(rel_tol * b)) and
                 (diff <= abs(rel_tol * a))) or
                (diff <= abs_tol))


def test_is_close():
    ''' just to make sure '''
    assert isclose(4.5, 4.5)
    assert isclose(4.5, 4.499999999999999999)

    assert not isclose(4.5, 4.6)
    # of course, not comprehesive!

# used this online calculator to check solutions:
# http://nastyaccident.com/calculators/calculus/trapezoidalRule


def test_line():
    # a simple line
    assert trapz(line, 0, 10) == 50


def test_curves():
    # a simple curve
    under_curve = trapz(a_curve, 1, 6)
    assert isclose(under_curve, 7.4512822710374)
    # a simple curve with larger arbitrary start and end points
    under_curve_2 = trapz(a_curve, 22, 146)
    assert isclose(under_curve_2, 1099.8560901121)
    # another curve with arbirtrary start and end points
    under_other_curve = trapz(another_curve, 1, 1999)
    assert isclose(under_other_curve, 2662803597.7332)


def test_sine():
    # python sin function with arbitrary start and end points
    under_sin = trapz(sin, 24, 346)
    assert isclose(under_sin, 0.030750318486179)


def test_quadratic_1():
    # quadratic with kwargs
    coef = {'A': 1, 'B': 3, 'C': 2}
    quad = trapz(quadratic, 5, 10, **coef)
    assert isclose(quad, 414.16875)


def test_quadratic_2():
    # quadratic with closure
    closure_quadratic_1_3_2 = quadratic_2(1, 3, 2)
    curried_quad = trapz(closure_quadratic_1_3_2, 5, 10)
    assert isclose(curried_quad, 414.16875)


def test_quadratic_3():
    # quadratic with partial
    partial_quadratic_1_3_2 = partial(quadratic, A=1, B=3, C=2)
    partial_quad = trapz(partial_quadratic_1_3_2, 5, 10)
    assert isclose(partial_quad, 414.16875)


def test_dynamic_trapz():
    same_grid = dynamic_trapz(a_curve, 1, 6, 100)
    assert isclose(7.4512822710374, same_grid)
    big_grids = dynamic_trapz(a_curve, 1, 6, 5)
    assert isclose(big_grids, 7.2642983586919)
    small_grids = dynamic_trapz(a_curve, 1, 6, 500)
    assert isclose(small_grids, 7.4533539021642)


# Christopher's tests


# def test_sloping_line():
#     ''' a simple linear function '''
#     def line(x):
#         return 2 + 3*x
# # I got 159.99999999999 rather than 160
# #   hence the need for isclose()
#     assert isclose(trapz(line, 2, 10), 160)
#     m, B = 3, 2
#     a, b = 0, 5
#     assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))
#     a, b = 5, 10
#     assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))
#     a, b = -10, 5
#     assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))


# def test_sine():
#     #  a sine curve from zero to pi -- should be 2
#     # with a hundred points, only correct to about 4 figures
#     assert isclose(trapz(math.sin, 0, math.pi), 2.0, rel_tol=1e-04)


# def test_sine2():
#     #  a sine curve from zero to 2pi -- should be 0.0
#     # need to set an absolute tolerance when comparing to zero
#     assert isclose(trapz(math.sin, 0, 2*math.pi), 0.0, abs_tol=1e-8)


# # test the quadratic function itself
# #   this is pytest's way to test a bunch of input and output values
# #   it creates a separate test for each case.
# @pytest.mark.parametrize(("x", "y"), [(0, 1),
#                                       (1, 3),
#                                       (2, 7),
#                                       (-2, 3)
#                                       ])
# def test_quadratic_1(x, y):
#     """
#         one set of coefficients
#         """
#     assert quadratic(x, A=1, B=1, C=1) == y


# @pytest.mark.parametrize(("x", "y"), [(0, 2),
#                                       (1, 3),
#                                       (2, 0),
#                                       (-2, -12)
#                                       ])
# def test_quadratic_2(x, y):
#     """
#         different coefficients
#         """
#     assert quadratic(x, A=-2, B=3, C=2) == y


# def quad_solution(a, b, A, B, C):
#     """
#         Analytical solution to the area under a quadratic
#         used for testing
#         """
#     return A/3*(b**3 - a**3) + B/2*(b**2 - a**2) + C*(b - a)


# def test_quadratic_trapz_1():
#     """
#         simplest case -- horizontal line
#         """
#     A, B, C = 0, 0, 5
#     a, b = 0, 10
#     assert trapz(quadratic, a, b, A=A, B=B, C=C) == quad_solution(a, b, A, B, C)


# def test_quadratic_trapz_2():
#     """
#         one case: A=-1/3, B=0, C=4
#         """
#     A, B, C = -1/3, 0, 4
#     a, b = -2, 2
#     assert isclose(trapz(quadratic, a, b, A=A, B=B, C=C),
#                        quad_solution(a, b, A, B, C),
#     rel_tol=1e-3)  # not a great tolerance -- maybe should try more samples!
