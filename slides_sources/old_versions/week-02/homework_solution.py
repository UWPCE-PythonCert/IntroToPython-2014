#!/bin/env python

"""
Chris' Solution to The Ackermann function
"""

def ack(m,n):
    """
    Solution to the Ackerman function
    
    http://en.wikipedia.org/wiki/Ackermann_function

    This one simply follows the logic laid out in the definition

    """

    if m<0 or n<0:
    	return "Solution is not Defined"
    
    if m == 0:
    	return n+1
    elif n == 0 and m > 0:
    	return ack(m-1, 1)
    else:
    	return ack(m-1, ack(m, n-1))


def ack2(m,n):
    """
    Solution to the Ackerman function
    
    http://en.wikipedia.org/wiki/Ackermann_function

    This one uses nested conditional expressions:
      Don't try this at home!

    """

    if m<0 or n<0:
    	return "Solution is not Defined"
    else:
        return n+1 if m==0 else (
	         ack2(m-1, 1) if (n == 0 and m > 0) else  ( 
	     	     ack2(m-1, ack2(m, n-1) ) 
	     	 	                                      )
	     	                     )
	      
    

# tests:
print ack(2,3)

for m in range(-1, 4):
	for n in range(-1, 5):
		print " the result of ack", (m,n), "is", ack(m,n)
		print " the result of ack2", (m,n), "is", ack2(m,n)


