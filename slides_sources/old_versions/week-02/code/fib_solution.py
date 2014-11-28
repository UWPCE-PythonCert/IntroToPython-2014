#/usr/bin/env python

def fib(n):
    """
    recursive function that computes Fibonacci numbers
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    """
    non-recusive function that computes fibonacci numbers
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        minus_2 = 0
        minus_1 = 1
        for i in range(2, n+1):
            result = minus_2 + minus_1
            minus_2, minus_1 = minus_1, result
    return result


print fib(0),
print fib(1),
print fib(2),
print fib(3),
print fib(4),
print fib(5),
print fib(6),
print fib(7),


