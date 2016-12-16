#!/usr/bin/env python3

"""
test code for the trapezoidal rule exercise
"""
import pytest

from trapz_adapt import trapz, isclose

import math


# linear functions should require no iterations
def test_simple_line():
    ''' a simple horizontal line at y = 5'''
    def line(x):
        return 5

    assert trapz(line, 0, 10) == 50


def test_sloping_line():
    ''' a simple linear function '''
    def line(x):
        return 2 + 3*x

    # I got 159.99999999999 rather than 160
    #   hence the need for isclose()
    assert isclose(trapz(line, 2, 10), 160)
    m, B = 3, 2
    a, b = 0, 5
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))

    a, b = 5, 10
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))

    a, b = -10, 5
    assert isclose(trapz(line, a, b), 1/2*m*(b**2 - a**2) + B*(b-a))


def test_sine():
    #  a sine curve from zero to pi -- should be 2
    # with a hundred points, only correct to about 4 figures
    result = trapz(math.sin, 0, math.pi, tol=1e-4)
    assert isclose(result, 2.0, rel_tol=1e-04)
    assert not isclose(result, 2.0, rel_tol=1e-05)

    # Try again with higher tol:
    result = trapz(math.sin, 0, math.pi, tol=1e-12)
    assert isclose(result, 2.0, rel_tol=1e-12)
    assert not isclose(result, 2.0, rel_tol=1e-13)


def test_sine2():
    #  a sine curve from zero to 2pi -- should be 0.0
    # tricky for the convergence!
    # need to set an absolute tolerance when comparing to zero
    result = trapz(math.sin, 0, 2*math.pi, tol=1e-4)
    assert isclose(result, 0.0, abs_tol=1e-04)
    # actualy gets a better answer right off the bat:
    # Trapezoidal rulw works very well for periodic functions
    #   The errors cancel out.
    # assert not isclose(result, 0.0, abs_tol=1e16)

    # try again with a higher tolerance
    # using abs_tol to compare with zero
    result = trapz(math.sin, 0, 2*math.pi, tol=1e-12)
    assert isclose(result, 0.0, abs_tol=1e-12)




if __name__ == "__main__":
    test_sine2()
