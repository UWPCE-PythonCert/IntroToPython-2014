#!/usr/bin/env python3

"""
trapezoidal rule function

Can integerate any function passed in
"""


def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C


def frange(a, b, n):
    """
    kind of like a floating point range function

    :param a: the start point
    :param b: the end point
    :param n: the number of intervals you want.

    :returns: a sequence of floating point nubers, evenly spaced between
    a and b

    result[0] == a
    result[-1] == b
    len(result) == n+1

    n specifies the number of intervals, so you get a nice delta. i.e.
    frange(1,10,100) == [1.0, 1.1, 1.2, ..., 9.8, 9.9, 10.0]

    """
    delta = (float(b) - a) / n
    return [a + i*delta for i in range(n+1)]


def trapz(fun, a, b, *args, **kwargs):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """
    # compute the range
    n = 100  # hard code that for now
    vals = frange(a, b, n)

    s = sum([fun(x, *args, **kwargs) for x in vals[1:-1]])
    s += (fun(a, *args, **kwargs) + fun(b, *args, **kwargs)) / 2
    s *= (b-a) / n

    return s


# "currying" version of quadratic:
def curry_quadratic(A, B, C):
    """
    "curry" the quadratic function to "lock in" particular arguments
    """
    return lambda x: quadratic(x, A=A, B=B, C=C)

# using functools.partial
import functools
quad_partial_123 = functools.partial(quadratic, A=1, B=2, C=3)

