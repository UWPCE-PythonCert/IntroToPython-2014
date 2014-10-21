#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Example of a recursive function with a good docstring.  

For best results to view the docstring, after importing do:
  
  >>> print ack.__doc__

Its value grows rapidly, even for small inputs. For example A(4,2) is an 
integer of 19,729 decimal digits. May hit maximum recursion limit.  See:

  sys.getrecursionlimit()
  sys.setrecursionlimit()

"""

def ack(m, n):
    """Evaluation of the Ackermann Function. 

    The Ackermann Function is defined as:
    A(m, n) =
      n+1                 if  m = 0
      A(m−1, 1)           if  m > 0  and  n = 0
      A(m−1, A(m, n−1))   if  m > 0  and  n > 0

    Args:
      m (int): must be >= 0
      n (int): must be >= 0.

    Yields:
      Evaluation of Ackermann function for A(m, n)

    """

    if (m < 0 or n < 0):
        print "Arguments for the Ackermann function must be >= 0."
        return None
    elif (m == 0):
        return n + 1
    elif (n == 0):
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':
    TestsPass = True
    
    try:
        assert ack(0, 0) == 1
        assert ack(0, 1) == 2
        assert ack(0, 2) == 3
        assert ack(0, 3) == 4
        assert ack(0, 4) == 5
        assert ack(1, 0) == 2
        assert ack(1, 1) == 3
        assert ack(1, 2) == 4
        assert ack(1, 3) == 5
        assert ack(1, 4) == 6
        assert ack(2, 0) == 3
        assert ack(2, 1) == 5
        assert ack(2, 2) == 7
        assert ack(2, 3) == 9
        assert ack(2, 4) == 11
        assert ack(3, 0) == 5
        assert ack(3, 1) == 13
        assert ack(3, 2) == 29
        assert ack(3, 3) == 61
        assert ack(3, 4) == 125
        assert ack(4, 0) == 13

    except AssertionError:
        TestsPass = False
        print "All Tests Did Not Pass!"

    if (TestsPass):
        print "All Tests Pass!"

