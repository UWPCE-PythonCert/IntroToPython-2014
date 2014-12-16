#!/usr/bin/env python

from sys import argv

def fibonacci(n=10):
    '''
    Return an array where each subsequent integer
    is the sum of the previous two, and the length
    equals the one parameter given, 'n'.  
    The first and second intergers are 0 and 1, respectively. 
    '''
    
    fibo_seq = [0,1]
    
    for i in range(2,n):
        fibo_seq.append(fibo_seq[i-2] + fibo_seq[i-1])

    return fibo_seq



def lucas(n=10):
    '''
    Return an array where each subsequent integer
    is the sum of the previous two, and the length
    equals the one parameter given, 'n'.
    The first and second intergers are 2 and 1, respectively.
    '''
    
    lucas_seq = [2,1]
    
    for i in range(2,n):
        lucas_seq.append(lucas_seq[i-2] + lucas_seq[i-1])

    return lucas_seq



def sum_series(n=10,x=0,y=1):
    '''
    Return an array where each subsequent integer
    is the sum of the previous two, and the length
    equals the one parameter given, 'n'.
    The first and second intergers are based on input.

    '''
    
    series_seq = [x,y]
    
    for i in range(2,n):
        series_seq.append(series_seq[i-2] + series_seq[i-1])

    return series_seq


if __name__ == '__main__':

    len_argv = len(argv)
    n = int(argv[1]) if len_argv > 1 else 10
    a = int(argv[2]) if len_argv > 2 else 0
    b = int(argv[3]) if len_argv > 3 else 1
    
    print '\n'
    print 'Fibonacci Series:'
    assert fibonacci(n)
    print fibonacci(n)
    
    print '\n'
    print 'Lucas Series:'
    assert lucas(n)
    print lucas(n)

    print '\n'
    print 'Custom Sum Series:'
    assert sum_series(n,a,b)
    print sum_series(n,a,b)

    print '\n'

    # try:
    # except:
    

# TODO:
# - Update docstrings for each function  
# - Add assert statements that demonstrate that your three functions work properly
# - Use comments in this block to inform the observer what your tests do
# - When you are finished, push your changes to your fork of the class repository in GitHub
# - Then make a pull request and submit your assignment in Canvas 