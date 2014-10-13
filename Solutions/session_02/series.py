#@python: 2

def fibonacci(n):
    """Return the nth value in the Fibonacci series

    Syntax:
    fibonacci(n)

    Arguments:
    n -- a positive integer

    The function calculates the specified value in the
    Fibonacci series given by the argument "n".  For example
    an n-value of 5 will return the value 3.
    """
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        v1 = 1
        v2 = 1
        for r in range(n):
            v3 = v1 + v2
            v2 = v3
            v1 = v2
        return v3