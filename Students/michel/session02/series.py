# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 21:10:43 2014

@author: Michel
"""

def fibonacci(n):
    """
    Computes Fibonacci series
    
    Returns Fibonacci of n
    n is a positive integer > 0
    """
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

def lucas(n):
    """
    Computes Lucas series
    
    Returns Lucas of n
    n is a positive integer > 0
    """
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
        
        
def sum_series(n, val1 = 0, val2 = 1):
    """
    Computes Fibonacci, Lucas or other series depending on val1 and val2
    
    
    n is a positve integer
    val1 and val2 are optional parameters and are positve integers
    Returns Lucas of n if val1 ==2 and val2 == 1
    Returns Fibonacci of n if no optional parameter val1 and val2 specified 
    Otherwise returns other series
    """
    if n < 0:
        return None
    elif val1 == 0 and val2 == 1:
        return fibonacci(n)
    elif val1 == 2 and val2 == 1:
        return lucas(n)
    else:
        return n
        
        
if __name__ == '__main__':
    # test all functions for n  < 0
    assert fibonacci(-1) == None
    assert lucas(-1) == None
    assert sum_series(-1) == None
    # test fibonacci and lucas functions for base cases
    assert fibonacci(0) == 1
    assert fibonacci(1) == 1
    assert lucas(0) == 2
    assert lucas(1) == 1
    # test fibonacci and lucas functions for one general case
    assert fibonacci(5) == 8
    assert lucas(5) == 11
    # test sum_series function for parameter values
    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, 0, 1) == fibonacci(5) 
    assert sum_series(5, 2, 1) == lucas(5)
    assert sum_series(5, 23, 12) == 5
    print 'All tests passed'