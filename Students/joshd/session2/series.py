def fibonacci(n):
    '''returns the nth value of the fibonacci sequence with for loop'''
    x = 0
    y = 1
    for i in range(n-2):
        # first two values already solved, therefore subtracting 2 from n
        z = x+y
        x = y
        y = z
    return z

def fib(n):
    '''returns the nth value of the fibonacci sequence recursively'''
    n -= 1
    #looking for the nth value, the first value should be 0, so subtracting to correct 0 indexing
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return ( fib(n - 1) + fib(n - 2) )

def lucas(n):
    '''returns the nth value of lucas numbers with a for loop'''
    x = 2
    y = 1
    for i in range(n-2):
        # first two values already solved, therefore subtracting 2 from n
        z = x+y
        x = y
        y = z
    return z

def L(n):
    '''returns the nth value of lucas numbers recursively'''
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return ( L(n - 1) + L(n - 2) )

def sum_series (x, first = 0, second = 1):
    if x == 1:
        return first
    if x == 2:
        return second
    else:
        return ( sum_series( x - 1, first, second) + sum_series(x - 2, first, second) )
