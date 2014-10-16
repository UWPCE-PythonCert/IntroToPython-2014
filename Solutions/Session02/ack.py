#!/usr/bin/env python
"""
Solution to the Ackerman function problem.

The Ackerman function is recusively defines as:

A(m, n) =
    n+1   if  m = 0
    A(m-1, 1)  if  m > 0 and n = 0
    A(m-1, A(m, n-1))  if m > 0 and n > 0
See http://en.wikipedia.org/wiki/Ackermann_function.
"""


def ack(m, n):
    """Compute the Ackerman function"""
    if m < 0 or n < 0:
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

if __name__ == "__main__":

    # tests from the table in wikipedia
    # you don't really need to test them all
    # they will get called as part of the recusive calls anyway...

    assert ack(0,0) == 1
    assert ack(0,4) == 5

    assert ack(1,2) == 4
    assert ack(1,4) == 6

    assert ack(2,2) == 7
    assert ack(2,4) == 11

    assert ack(3,2) == 29
    assert ack(3,4) == 125

    ## ack(4,*) exceeds the recursion limit.

    # check for neagative inputs -- should return None.
    assert ack(-1, 0) is None
    assert ack(2, -1) is None


    print "tests passed"
