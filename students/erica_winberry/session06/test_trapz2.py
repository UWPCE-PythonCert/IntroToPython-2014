import math
from trapezoidal2 import trapz, line, squared, quadratic


def test_trapz_line():
    assert math.isclose(float((trapz(line, 1, 10))), 50.0, rel_tol=.1)
    assert math.isclose(float((trapz(squared, 1, 10))), 333.0, rel_tol=.001)
    assert math.isclose(float((trapz(quadratic, 1, 10, a=1, b=3, c=2))), 500.0, rel_tol=.1)


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