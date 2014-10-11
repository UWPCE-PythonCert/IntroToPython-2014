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

# Testing Block
if __name__ == "__main__":
    assert fibonacci(-3) is None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(17) == 1597
    assert lucas(-3) is None
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(10) == 123