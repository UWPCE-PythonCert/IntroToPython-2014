#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def fibonacci(n):
    """Evaluation of the nth term of the Fibonnaci Series. 

    The Fibonnaci Series is defined as:
      0th term: 0
      1st term: 1
      nth term: sum of previous two terms in the series

    Args:
      n (int): nth term in series (must be >= 0)

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
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Evaluation of the nth term of the Lucas Series. 

    The Lucas Series is defined as:
      0th term: 2
      1st term: 1
      nth term: sum of previous two terms in the series

    Args:
      n (int): nth term in series (must be >= 0)

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
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, zerothTerm=0, firstTerm=1):
    """Evaluation of the nth term of a series. 

    This function will return the nth term in a series which is the sum
    of the previous two consecutive terms in the series. The user can 
    specify any zeroth and first terms to define the series, or can use 
    the default values of 0 and 1 to give the n-th term of the
    Fibonacci series.

    Args:
      n (int): nth term in series (must be >= 0)
      zerothTerm (int): zeroth term in the series (default = 0)
      firstTerm (int): first term in the series (default = 1)

    Yields:
      nth term of the series.

    """

    if (n < 0):
        print "Arguments for the series must be >= 0."
        return None
    elif (n == 0):
        return zerothTerm
    elif (n == 1):
        return firstTerm
    else:
        return sum_series(n - 1, zerothTerm, firstTerm) + sum_series(n - 2, zerothTerm, firstTerm)


if __name__ == '__main__':
    FibanocciTestsPass = True
    LucasTestsPass = True
    ArbitrarySeriesTestsPass = True

    # Some assertions to test the Fibonacci series function against known solutions
    try:
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(10) == 55
        assert fibonacci(19) == 4181

    except AssertionError:
        FibanocciTestsPass = False
        print "All Fibonacci Tests Did Not Pass!"

    # Some assertions to test the Lucas series function against known solutions
    try:
        assert lucas(0) == 2
        assert lucas(1) == 1
        assert lucas(10) == 123
        assert lucas(20) == 15127

    except AssertionError:
        LucasTestsPass = False
        print "All Lucas Tests Did Not Pass!"

    # Some assertions to test the arbitrary series function against known solutions
    try:
        assert sum_series(10) == 55
        assert sum_series(10, 0, 1) == 55
        assert sum_series(10, 2, 1) == 123
        assert sum_series(15, 3, 3) == 2961
        assert sum_series(20, 5, 2) == 34435
        assert sum_series(20, 2, 5) == 42187

    except AssertionError:
        ArbitrarySeriesTestsPass = False
        print "All aritrary series tests did not pass"

    if (FibanocciTestsPass and LucasTestsPass and ArbitrarySeriesTestsPass):
        print "All Tests Pass!"
