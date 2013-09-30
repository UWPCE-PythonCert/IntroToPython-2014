#!/usr/bin/env python

"""
some sample examples from LAB 1-c (functions)
"""

x = 5
z = 10
def test_locals(y):
    z = 6
    print locals()
        
# now run it
test_locals(2)

def square_cube(x):
    square = x*x
    cube = x**3
    return square, cube

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print "factorial of 1 is:", fact(1)
print "factorial of 2 is:", fact(2)    
print "factorial of 3 is:", fact(3)    
print "factorial of 3 is:", fact(4)    