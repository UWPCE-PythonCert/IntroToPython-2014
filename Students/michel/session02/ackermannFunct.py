# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:43:16 2014

@author: Michel
"""

def ackermann (m, n):
    """
    computes ackerman recursive function
    
    returns a positive integer value
    m and n are nonnegative integers
    """
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
        
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
        
if __name__ == '__main__':
    assert ackermann(-1,-1) == None
    assert ackermann(-1,0) == None
    assert ackermann(0,-1) == None
    assert ackermann(0,0) == 1
    assert ackermann(0,1) == 2
    assert ackermann(1,0) == 2
    assert ackermann(0,2) == 3
    assert ackermann(0,3) == 4
    assert ackermann(0,4) == 5
    assert ackermann(1,2) == 4
    assert ackermann(1,3) == 5
    assert ackermann(1,4) == 6
    assert ackermann(2,1) == 5
    assert ackermann(2,2) == 7
    assert ackermann(2,3) == 9
    assert ackermann(2,4) == 11
    assert ackermann(3,0) == 5
    assert ackermann(3,1) == 13  
    assert ackermann(3,2) == 29
    assert ackermann(3,3) == 61
    assert ackermann(3,4) == 125
    assert ackermann(4,0) == 13
    assert ackermann(4,1) == 65533
#    assert ackermann(4,2) == 61
#    assert ackermann(4,3) == 61
#    assert ackermann(4,4) == 61
    print 'All tests passed'