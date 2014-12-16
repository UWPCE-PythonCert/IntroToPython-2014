#!/usr/bin/python

    

print """

This program performs Ackermann's Function, as defined by: 

A(m,n) =

    n+1 if m = 0

    A(m-1) if m > 0 and n = 0

    A(m-1, A(m, n-1)) if m > 0 and n > 0


    """

m = raw_input("Please provide a value for m: ")
n = raw_input("Please provide a value for n: ")

m = int(m)
n = int(n)

print "m = " + str(m)
print "n = " + str(n)

def is_negative(x):
"""This function checks to make sure that values are positive"""
    if x < 0:

        x = raw_input("Ackermann's function is not defined for values less than 0. Please start over with a value that is greater than 0. \n\nExiting.\n")

        exit()
    
is_negative(m)
is_negative(n)


def ackermann(x,y):
"""Performs Ackermann's function on values x = m, y = n"""
    #x = m 
    #y = n 

    #while y > -1:

    if x == 0:
    
        return y+1

    elif x > 0 and y == 0:

        return ackermann(x - 1, 1)

    elif x > 0 and y > 0:
        return ackermann(x - 1 , ackermann(x, y - 1))
        
print ackermann(m,n)


    #
    # This is where I am going to put my tests and asserts

if __name__ == "__main__":

    assert ackermann(0,0) == 1
    assert ackermann(0,1) == 2
    assert ackermann(0,2) == 3
    assert ackermann(0,3) == 4
    assert ackermann(1,0) == 2
    assert ackermann(2,0) == 3
    assert ackermann(2,4) == 11
    assert ackermann(3,4) == 125
    print "\nAll Tests Pass!\n"
   # #
   # #

