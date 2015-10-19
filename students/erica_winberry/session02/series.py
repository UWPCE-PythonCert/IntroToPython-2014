
# STEP 1
# Create a new module series.py in the session02 folder in your student folder.
#     In it, add a function called fibonacci.
#     The function should have one parameter n.
#     The function should return the nth value in the fibonacci series.
#     Ensure that your function has a well-formed docstring
# Note that the fibinacci series is naturally recusive – the value is defined by previous values:
#     fib(n) = fib(n-2) + fib(n-1)

def fibonacci(n):
    """Return the nth value in the Fibonacci series."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = fibonacci(n - 2) + fibonacci(n - 1)
        return fib

# STEP 2
# The Lucas Numbers are a related series of integers that start with the 
# values 2 and 1 rather than 0 and 1. The resulting series looks like this:
# 2, 1, 3, 4, 7, 11, 18, 29, ...
# In your series.py module, add a new function lucas that returns the nth value in the lucas numbers series.

def lucas(n):
    """Return the nth value in the Lucas series."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        luc = lucas(n - 2) + lucas(n - 1)
        return luc

# STEP 3
# Add a third function called sum_series with one required parameter and 
# two optional parameters. The required parameter will determine which 
# element in the series to print. The two optional parameters will have 
# default values of 0 and 1 and will determine the first two values for 
# the series to be produced.

# Calling this function with no optional parameters will produce numbers 
# from the fibonacci series. Calling it with the optional arguments 2 and 1 
# will produce values from the lucas numbers. Other values for the optional 
# parameters will produce other series.

def sum_series(n, p1=0, p2=1):
    """Return the nth value in a number series where the next number is determined by adding the previous 2 numbers.
       Unchanged parameters result in the Fibonacci series.
       Changing parameters to n,2,1 results in the Lucas series."""
    if n == 1:
        return p1
    elif n == 2:
        return p2
    else:
        num = sum_series(n - 2,p1,p2) + sum_series(n - 1,p1,p2)
        return num

