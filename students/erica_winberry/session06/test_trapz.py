
from trapezoidal import trapz
from trapezoidal import squared
import math


def test_trapz_line():
    assert math.isclose(float((trapz(squared, 1, 10))), 333.0, rel_tol=.001)


'''
About the simplest “curve” you can have is a horizontal straight line, 
in this case, at y = 5. The area under that line from 0 to 10 is a 
rectangle that is 10 wide and 5 high, so with an area of 50.

Of course in this case, it’s easiest to simply multiply the height 
times the width, but we want a function that will work for any curve.

HINT: this simple example could be a good test case!



NOTE: math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

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