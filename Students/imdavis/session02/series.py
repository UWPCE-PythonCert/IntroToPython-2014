#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def fibonacci(n):
    """Evaluation of the nth term of the Fibonnaci Series. 

    The Fibonnaci Series is defined as:
      0th term: 0
      1st term: 1
      nth term: sum of previous two terms in the series

    Args:
      n (int): must be >= 0

    Yields:
      nth term of the Fibonnaci Series.

    """

    if (n < 0):
        print "Arguments for the Fibonnaci series must be >= 0."
        return None
    elif (n == 0):  # zeroth term = 0
        return 0
    elif (n == 1):  # first term = 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Evaluation of the nth term of the Lucas Series. 

    The Lucas Series is defined as:
      0th term: 2
      1st term: 1
      nth term: sum of previous two terms in the series

    Args:
      n (int): must be >= 0

    Yields:
      nth term of the Lucas Series.

    """

    if (n < 0):
        print "Arguments for the Lucas series must be >= 0."
        return None
    elif (n == 0):  # zeroth term = 0
        return 2
    elif (n == 1):  # first term = 1
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


if __name__ == '__main__':
    FibanocciTestsPass = True
    LucasTestsPass = True

    try:
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55
        assert fibonacci(19) == 4181

    except AssertionError:
        FibanocciTestsPass = False
        print "All Fibonacci Tests Did Not Pass!"

    try:
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(10) == 123
        assert lucas(20) == 15127

    except AssertionError:
        LucasTestsPass = False
        print "All Lucas Tests Did Not Pass!"

    if (FibanocciTestsPass and LucasTestsPass):
        print "All Tests Pass!"

