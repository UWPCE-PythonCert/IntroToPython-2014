#!/usr/bin/env python3

"""
test code for the trapezoidal rule exercise
"""

from trapz import trapz, frange

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


def test_frange():
    '''
    tests the floating point range function
    '''
    r = frange(10, 20, 100)
    assert r[0] == 10
    assert r[-1] == 20
    assert r[1] == 10.1
    assert r[-2] == 19.9


def test_simple_line():
    ''' a simple horizontal line at y = 5'''
    def line(x):
        return 5

    assert trapz(line, 0, 10) == 50
