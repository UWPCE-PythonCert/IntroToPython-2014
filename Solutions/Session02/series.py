#!/usr/bin/env python

"""
series.py

solutions to the Fibonacci Series and Lucas numbers
"""


def fibonacci(n):
    """ compute the nth Fibonacci number """

    if n < 0:
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """ compute the nth Lucas number """

    if n < 0:
        return None
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """
    compute the nth value of a summation series.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    if n0 == 0 and n1 == 1, the result is the Fibbonacci series

    if n0 == 2 and n1 == 1, the result is the Lucas series
    """
    if n < 0:
        return None
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)


if __name__ == "__main__":
    # run some tests

    assert fibonacci(-1) is None
    assert fibonacci(-23) is None

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(-1) is None
    assert lucas(-23) is None

    # do these with a loop:
    tests = [(0, 2),
             (1, 1),
             (2, 3),
             (3, 4),
             (4, 7),
             (5,11),
             (6,18),
             (7, 29),
             ]
    for input, output in tests:
        assert lucas(input) == output

    # test if sum_series matched Fibonacci
    for n in range(0, 10):
        assert sum_series(n) == fibonacci(n)

    # test if sum_series matched lucas
    for n in range(0, 10):
        assert sum_series(n, 2, 1) == lucas(n)

    print "tests passed"
