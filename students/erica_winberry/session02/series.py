
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



# TESTING
# Add a block of code to the end of your series.py module. 
# Use the block to write a series of assert statements that demonstrate that your three functions work properly.
# Use comments in this block to inform the observer what your tests do.

if __name__ == "__main__":
# Testing fibonacci function to make sure that the first two if/elif statements are working properly:
    assert fibonacci(2) == 1 and fibonacci(1) == 0
# Testing the fibonacci function with the first few numbers in the fibonacci series:
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
# Testing lucas function to make sure that the first two if/elif statements are working properly:
    assert lucas(2) == 1 and lucas(1) == 2
# Testing the lucas function with the first few numbers in the fibonacci series:
    assert lucas(3) == 3
    assert lucas(4) == 4
    assert lucas(5) == 7
    assert lucas(6) == 11
# Testing the sum_series function to make sure it returns the correct numbers in the Fibonacci series:
    assert sum_series(3) == 1
    assert sum_series(4) == 2
    assert sum_series(5) == 3
    assert sum_series(6) == 5
# Testing the sum_series function to make sure it returns the correct numbers in the Lucas series:
    assert sum_series(3,2,1) == 3
    assert sum_series(4,2,1) == 4
    assert sum_series(5,2,1) == 7
    assert sum_series(6,2,1) == 11
# Testing the sum_series function when using other 2nd and 3rd parameters. The 3rd number in a series should always be the sum of the last two parameters:
    assert sum_series(3,4,5) == 9
    assert sum_series(3,5,6) == 11
    assert sum_series(3,6,7) == 13
    assert sum_series(3,7,8) == 15
# Deliberately making incorrect assertions - commented out. Remove the hash to test a line:
#    assert fibonacci(7) == 9
#    assert lucas(7) == 20
#    assert sum_series(7) == 10
#    assert sum_series(7,2,1) == 21
#    assert sum_series(4,4,5) == 16

# run some tests
    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
