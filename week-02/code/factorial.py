#!/usr/bin/env python

def factorial(n):
    """
    computes the factorial of n
    
    :param n: an integer to compute the factorial of
    
    :returns:  the factorial of n
    """
    # print "calling factorial, n=",n
    f = float(n)
    n = int(n)
    if n != f:
        print "factorial only works for integers:",
        return None

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# print "the factorial of 0 is:", factorial(0)
# print "the factorial of 1 is:", factorial(1)
# print "the factorial of 2 is:", factorial(2)
# print "the factorial of 3 is:", factorial(3)
# print "the factorial of 4 is:", factorial(4)

#print "the factorial of 983 is:", factorial(983)

#print "the factorial of 984 is:", factorial(984)

#print "the factorial of 4L is:", factorial(4L)

#print "the factorial of 1.5 is:", factorial(1.5)

## checking types: -- is instance
