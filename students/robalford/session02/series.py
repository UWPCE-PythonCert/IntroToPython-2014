def fibonacci(n):
    """ Return the nth value in the Fibonacci Series. """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """ Return the nth value in the Lucas Numbers Series. """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, step_one=0, step_two=1):
    """ Return the nth value in a series of numbers beginning with step_one and step_two.
        The remaining values in the series are determined by summing the two previous values. """
    if n == 0:
        return step_one
    elif n == 1:
        return step_two
    else:
        return sum_series(n-1, step_one, step_two) + sum_series(n-2, step_one, step_two)
