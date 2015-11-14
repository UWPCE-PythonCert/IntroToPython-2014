from math import sin

from trapz import line, a_curve, another_curve, trapz

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


def test_trapz():
    # a simple line
    assert trapz(line, 0, 10) == 50
    # a simple curve
    under_curve = trapz(a_curve, 1, 6)
    assert isclose(under_curve, 7.4512822710374)
    # a simple curve with larger arbitrary start and end points
    under_curve = trapz(a_curve, 22, 146)
    assert isclose(under_curve, 1099.8560901121)
    # another curve with arbirtrary start and end points
    under_other_curve = trapz(another_curve, 1, 1999)
    assert isclose(under_other_curve, 2662803597.7332)
    # python sin function with arbitrary start and end points
    under_sin = trapz(sin, 24, 346)
    assert isclose(under_sin, 0.030750318486179)
