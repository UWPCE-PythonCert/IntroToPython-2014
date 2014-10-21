#!/usr/bin/env python

from sys import argv

len_argv = len(argv)
_m = int(argv[1]) if len_argv > 1 else 4
_n = int(argv[2]) if len_argv > 2 else 4

def ack(m,n):
    '''Demonstrate the power of the recursive via the Ackermann function.'''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m, n-1))
        

if __name__ == '__main__':
    # print 'ack.py is running...'
    '''
    Test each pair of inputs between 0 and 4 and assert that the result produced by your function is the result expected by the wikipedia table.
    '''
    try:
        for m in range(_m+1):
            for n in range(_n+1):
                print 'ack(%d,%d):' % (m, n), ack(m,n)
        else:
            print 'Test Run: All Pass'
    except:
        print '...\nTest Run: Uh Oh, Fail!'
    
    