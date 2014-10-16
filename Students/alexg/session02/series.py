#!/usr/bin/python

def fibonacci(x):
    """Returns the nth value of the Fibonacci Series"""
    if not x: 
        return 0
    elif x == 1: 
        return 1
    else: 
        return fibonacci(x-1)+fibonacci(x-2)

def lucas(x):
    """Returns the nth value of the Lucas Series"""
    if not x:
        return 2
    elif x == 1:
        return 1
    else:
        return lucas(x-1)+lucas(x-2)

def sum_series(n,x=0,y=1):
    """Returns the nth value of either series, or creates a new one"""
    if x==0 and y==1:
        return fibonacci(n)
    elif x==2 and y==1:
        return lucas(n)
    else:
        if not n:
            return x
        elif n==1:
            return y
        else:
            return sum_series(n-1)+sum_series(n-2)

if __name__ == "__main__":
    #Testing the 7th value of the fibonacci sequence
    assert fibonacci(6)==8

    #Testing the 7th value of the lucas sequence
    assert lucas(6)==18

    #Testing for the 2nd value of the new function
    assert sum_series(9,40,2)==34
