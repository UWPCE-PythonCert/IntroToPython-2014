def fibonacci(n):
    """Return the nth value in the Fibonacci series

    Syntax:
    fibonacci(n)

    Arguments:
    n -- a positive integer

    The function calculates the specified value in the
    Fibonacci series given by the argument "n".  For example
    an n-value of 5 will return 3, the 5th value in the Fibonacci
    series.
    """

    if n < 0:
        return None
    elif not n:
        return 0
    elif n == 1:
        return 1
    else:
        v1 = 0
        v2 = 1
        v3 = 0
        for r in range(n):
            v3 += v2
            v1 = v2
            v2 = v3 - v1
        return v3

for m in range(20):
    print fibonacci(m),

