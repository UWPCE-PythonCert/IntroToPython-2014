#!/usr/bin/env python3

"""
adaptive version of the trapezoidal rule function

Can integerate any function passed in
 -- and will selct a step size dynamically

"""

# need a function for testing approximate equality
import math
try:
    from math import isclose
except ImportError:  # only there in py3.5 -- so we'll define it here.

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


def trapz(fun, a, b, tol=1e-4, *args, **kwargs):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes teh vule to be integrated over as
               its first argument. Any arguments can be passed in at the end.

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value

    :param tol=1e-4: accuracy expected.

    any other arguments will be passed through to fun.
    """
    # compute the range

    # loop to try varying step sizes until desired accuracey is achieved

    prev_s = None
    n = 2  # start with only two steps
    while True:  # break out when desired accuracy is reached
        vals = frange(a, b, n)
        s = sum([fun(x, *args, **kwargs) for x in vals[1:-1]])
        s += (fun(a, *args, **kwargs) + fun(b, *args, **kwargs)) / 2
        s *= (b-a) / n
        if prev_s is not None:
            # check if we're close enough
            # abs_tol is for comparison to zero
            if isclose(s, prev_s, rel_tol=tol, abs_tol=tol):
                return s
        n *= 2
        prev_s = s
        # this could be a more sophisticated criterion
        if n >= 2**22:  # it's not going to work (about half the precision of a double)
            raise ValueError("Solution didn't converge")
