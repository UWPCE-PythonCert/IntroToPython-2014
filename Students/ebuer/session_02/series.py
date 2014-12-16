import numpy as np

def fibonacci(n):
    """Return the nth value in the Fibonacci series

    Syntax:
    fibonacci(n)

    Arguments:
    n -- a positive integer

    The function calculates the specified value in the
    Fibonacci series given by the argument "n".  For example
    an n-value of 5 will return 5, the 5th value in the Fibonacci
    series.

    Note that this function has opted to use the same indexing as python
    series, which assigns a position of 0 to the first value.
    """

    if n < 0:
        return None
    elif not n:
        return 0
    elif n == 1:
        return 1
    else:
        v1 = 0
        v2 = 1
        v3 = 0
        for r in range(n):
            v3 += v2
            v1 = v2
            v2 = v3 - v1
        return v3

# print "Test Fibonacci output:"
# for m in range(20):
#     print fibonacci(m),

def lucas(n):
    """Return the nt value in the Lucas series

    Syntax:
    lucas(n)

    Arguments:
    n -- a positive integer

    The function calculates the specified value in the Lucas series 
    given an argument "n".  For example an n-value of 4 will return the 
    4th value in the Lucas series: 7.

    Note that this function has opted to use the same indexing as python
    series, which assigns a position of 0 to the first value.
    """
    if n < 0:
        return None
    elif not n:
        return 2
    elif n == 1:
        return 1
    else:
        v1 = 2
        v2 = 1
        v3 = v2 + v1
        for r in np.arange(2,n):
            v3 += v2
            v1 = v2
            v2 = v3 - v1
        return v3

# print "\nTest Lucas output:"
# for m in range(20):
#     print lucas(m),

def sum_series(n, a = 0, b = 1):
    """Return the nth value in an additive series with a and b as starting integers

    Syntax:
    sum_series(n, a, b)

    Arguments:
    n -- a positive integer
    a (optional) -- a positive integer, default value is 0
    b (optional) -- a positive integer, default value is 1

    The function is set up to act as a Fibonacci additive series unless
    the new starting values for a and b are provided when the function is
    called. For example: providing the values a = 2 and b = 1 will return 
    the nth value in the Lucas series.

    Note that this function has opted to use the same indexing as python
    series, which assigns a position of 0 to the first value.
    """
    if (a or b) < 0:
        print 'Both a and b must be positive integers.'
        return None

    if n < 0:
        return None
    elif not n:
        return a
    elif n == 1:
        return b
    else:
        v1 = a
        v2 = b
        v3 = v2 + v1
        for r in np.arange(2,n):
            v3 += v2
            v1 = v2
            v2 = v3 - v1
        return v3

# print "\nTest sum_series output:"
# for m in range(20):
#     print sum_series(m, 3, 5),

if __name__ == "__main__":
    #provide test values to fibo, lucas and sum_series
    #to make sure function argument passing is working.
    assert fibonacci(5) == 5 
    assert lucas(4) == 7
    assert sum_series(10) == 55

    print "All functions have passed initialization tests."