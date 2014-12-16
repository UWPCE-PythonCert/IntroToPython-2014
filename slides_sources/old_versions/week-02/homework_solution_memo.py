#!/bin/env python

"""
Chris' Solution to The Ackermann function
"""

all_calls = {}

num_calls = 0
num_calls2 = 0


def ack(m,n):
    """
    Solution to the Ackerman function
    
    http://en.wikipedia.org/wiki/Ackermann_function

    This one directly follows the logic laid out in the definition

    """

    # I prefer to check bounds up front:
    #  this really should raise an exception,
    #  but we haven't covered that yet in class.

    global num_calls
    num_calls += 1

    if m<0 or n<0:
        return "Solution is not Defined"

    # print "ack called with:", m, n
    if (m,n) in all_calls:
        # print "already called with:", (m,n)
        return all_calls[(m,n)]
    else:
        if m == 0:
        	result = n+1
        elif n == 0 and m > 0:
        	result = ack(m-1, 1)
        else:
        	result = ack(m-1, ack(m, n-1))
        all_calls[(m,n)] = result

        return result


def ack2(m,n):
    """
    Solution to the Ackerman function
    
    http://en.wikipedia.org/wiki/Ackermann_function

    This one uses nested conditional expressions:
      Don't try this at home!

    """
    global num_calls2
    num_calls2 += 1

    if m<0 or n<0:
    	return "Solution is not Defined"
    else:
        return n+1 if m==0 else (
	         ack2(m-1, 1) if (n == 0 and m > 0) else  ( 
	     	     ack2(m-1, ack2(m, n-1) ) 
	     	 	                                      )
	     	                     )
	      
    
# tests:
print "with saving intermediate results:"
print ack(3,4)
print "total number of calls:", num_calls

print "without saving intermediate results:"
print ack2(3,4)
print "total number of calls:", num_calls2

# for m in range(-1, 4):
# 	for n in range(-1, 5):
# 		print " the result of ack", (m,n), "is", ack(m,n)
# 		print " the result of ack2", (m,n), "is", ack2(m,n)


