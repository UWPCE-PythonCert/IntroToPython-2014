#!/usr/bin/python

def fibonacci(n):
    """Print n fibonnaci numbers"""
    n = input('How many Fibonacci numbers to print? ')
    fib=[0] # where we'll store the sequence list
    x,y,z=0,1,1
    for i in range(n-1):
        fib.append(z)
        z = x + y
        x , y = y , z
    print('Fibonacci: ', fib) # Why doesn't "return(fib)" print to std.out?

def lucas(n):
    """Print the nth value in the Lucas Number Series"""
    n= input('Which number in the Lucas Series to print? ')


