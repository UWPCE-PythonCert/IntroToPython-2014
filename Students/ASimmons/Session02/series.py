__author__ = 'Ari'

def fibonacci(n):
    """Return the nth value based on the Fibonacci sequence.
    For the purpose of this assignment I decided to start the
    sequence at 0"""
    current_num = 0
    prev_num = 1
    # first two values have already been set, thus n-2
    for i in range(0, n-2):
        temp = current_num
        current_num = prev_num
        prev_num= temp + prev_num
    return prev_num

def lucas(n):
    """Return the nth value based on the Lucas sequence"""
    current_num = 2
    prev_num = 1
    # first two values have already been set, thus n-2
    for i in range(0, n-2):
        temp = current_num
        current_num = prev_num
        prev_num = temp + prev_num
    return prev_num

def sum_series(n, current_num=0, prev_num=1):
    """Return the nth value of either the Fibonacci sequence (default) or the Lucas sequence."""
    # CURRENTLY this function doesn't work...returns nothing
    # I am not sure why, but my initial if statement
    # also is throwing syntax errors (when I inspect it
    # with the IDE
    if current_num=0 and prev_num=1:
        fibonacci(n)
    else:
        lucas(n)


