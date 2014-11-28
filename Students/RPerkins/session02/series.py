__author__ = 'Robert W. Perkins'


def fibonacci(n):
    """Return the 'n'th value in the Fibonacci series"""

# test for input in valid range
    if n < 0:
        return None

# test for n == 0
    if n == 0:
        return 0

# base case is n == 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return the 'n'th value in the Lucas number series"""

# test for input in valid range
    if n < 0:
        return None

# test for n == 0
    if n == 0:
        return 2

# base case is n == 1
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n,first=0,second=1):
    """Return the 'n'th value of a variable series"""

    """The first two numbers are passed via "first" and "second"
    and each subsequent element is the sum of the 'n-1'th and 'n-2'th element (yes, i said tooth)"""

# test for input in valid range
    if n < 0:
        return None

# test for n == 0
    if n == 0:
        return first

# base case is n == 1
    if n == 1:
        return second
    else:
        return sum_series(n-1,first,second) + sum_series(n-2,first,second)


# Testing Block
if __name__ == "__main__":

    # test fibonacci function for out of range, n == zero, base case, and 18th value in series
    assert fibonacci(-3) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(17) == 1597

    # test lucas function for out of range, n == zero, base case, and 11th value in series
    assert lucas(-3) is None
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(10) == 123

    # tests sum_series function for fibonacci behavior with no optional params
    # for out of range, n == zero, base case, and 18th value in series
    assert sum_series(-3) is None
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(17) == 1597

	# tests sum_series function for lucas behavior with lucas series params
	# for out of range, n == zero, base case, and 11th value in series
    assert sum_series(-3,2,1) is None
    assert sum_series(0,2,1) == 2
    assert sum_series(1,2,1) == 1
    assert sum_series(10,2,1) == 123

	# tests sum_series function for valid results with optional params
	# for out of range, n == zero, base case, and 11th value in series
    assert sum_series(-3,4,2) is None
    assert sum_series(0,4,2) == 4
    assert sum_series(1,4,2) == 2
    assert sum_series(10,4,2) == 246