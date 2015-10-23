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

# Tests

# test for accuracy of first recursively generated value in fibonacci series
assert fibonacci(2) == 1
# test accuracy of two larger values for the fibonacci series
assert fibonacci(7) == 13
assert fibonacci(12) == 144
# test for accuracy of first recursively generated value in lucas series
assert lucas(2) == 3
# test accuracy of two larger values for the lucas series
assert lucas(7) == 29
assert lucas(10) == 123
# test sum_series for accuracy using large values of fibonacci and lucas series
assert sum_series(12, 0, 1) == 144
assert sum_series(10, 2, 1) == 123



