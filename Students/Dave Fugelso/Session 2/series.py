'''
Dave Fugelso - UW Python Certification 10/09/2014

The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next
integer is determined by summing the previous two. This gives us:

0, 1, 1, 2, 3, 5, 8, 13, ...
Create a new module series.py in the session02 folder in your student folder. In it, add a function 
called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series.

Ensure that your function has a well-formed docstring

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. 
The resulting series looks like this:


2, 1, 3, 4, 7, 11, 18, 29, ...
In your series.py module, add a new function lucas that returns the nth value in the lucas numbers

Ensure that your function has a well-formed docstring

Both the fibonacci series and the lucas numbers are based on an identical formula.

Add a third function called sum_series with one required parameter and two optional parameters. The required 
parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it 
with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.

Ensure that your function has a well-formed docstring

Add an if __name__ == \"__main__\": block to the end of your series.py module. Use the block to write a series of assert 
statements that demonstrate that your three functions work properly.


Use comments in this block to inform the observer what your tests do.

Add your new module to your git clone and commit frequently while working on your implementation. Include good commit 
messages that explain concisely both what you are doing and why.

When you are finished, push your changes to your fork of the class repository in GitHub. Then make a pull request and submit your assignment in Canvas.
'''

def fibonnacci (n):
    '''
    Return the Nth value in the Fibonacci series.
    Args:
        n - Nth value 
    '''
    
    # special cases at front of series
    if n == 0: return 0
    if n == 1: return 1
    
    #else let's calculate
    a, b = 0, 1
    for seq in range (2, n):
        a,b = b,a+b
    return a+b
    
def lucas (n):
    '''
    Return the Nth value in the Lucas series.
    Args:
        n - Nth value 
    '''
    
    # special cases at front of series
    if n == 0: return 2
    if n == 1: return 1
    
    #else let's calculate
    a, b = 2, 1
    for seq in range (2, n):
        a,b = b,a+b
    return a+b

'''
Second solution. Just have lucas and fibonacci start a series function with differing start arguments.
'''

def series (a, b, n):
    ''' 
    Calculate the nth number in a series based on starting at a, b.
    Args:
        a - value for element 0
        b - value for element 1
        n - the series element wanted
    '''
    
    # special cases at front of series
    if n == 0: return a
    if n == 1: return b
    
    #else let's calculate
    for seq in range (2, n):
        a,b = b,a+b
    return a+b
    
def fibonacci_2(n):
    '''
    Return the Nth value in the Fibonacci series.
    Args:
        n - Nth value 
    '''
    return series(0, 1, n)

def lucas_2(n):
    '''
    Return the Nth value in the Lucas series.
    Args:
        n - Nth value 
    '''
    return series(2, 1, n)
    
if __name__ == "__main__":
    '''
    perform unit tests for fibonacci and lucas funcitons.
    '''
    
    #Test the Fibinacci series: randomly selected 0, 1 5, 8 and 25
    assert fibonnacci (0)==0, 'Fibonnaci (0) is 0. Failed!'
    assert fibonnacci (1)==1, 'Fibonnaci (1) is 1. Failed!'
    assert fibonnacci (5)==5, 'Fibonnaci (5) is 5. Failed!'
    assert fibonnacci (8)==21, 'Fibonnaci (8) is 21. Failed!'
    assert fibonnacci (25)==75025, 'Fibonnaci (25) is 75025. Failed!'
    
    #Test lucas series: choose 0, 1, 6, 9, 26
    assert lucas(0)==2, 'Lucas(0) is 2. Failed!'
    assert lucas(1)==1, 'Lucas(1) is 1. Failed!'
    assert lucas(6)==18, 'Lucas(6) is 2. Failed!'
    assert lucas(9)==76, 'Lucas(9) is 2. Failed!'
    assert lucas(26)==271443, 'Lucas(26) is 2. Failed!'
      
    #Test the Fibinacci series: randomly selected 0, 1 5, 8 and 25
    assert fibonnacci_2 (0)==0, 'Fibonnaci 2 (0) is 0. Failed!'
    assert fibonnacci_2 (1)==1, 'Fibonnaci 2 (1) is 1. Failed!'
    assert fibonnacci_2 (5)==5, 'Fibonnaci 2 (5) is 5. Failed!'
    assert fibonnacci_2 (8)==21, 'Fibonnaci 2 (8) is 21. Failed!'
    assert fibonnacci_2 (25)==75025, 'Fibonnaci 2 (25) is 75025. Failed!'
    
    # Test the second solutions
    #Test lucas series: choose 0, 1, 6, 9, 26
    assert lucas_2(0)==2, 'Lucas 2 (0) is 2. Failed!'
    assert lucas_2(1)==1, 'Lucas 2 (1) is 1. Failed!'
    assert lucas_2(6)==18, 'Lucas 2 (6) is 2. Failed!'
    assert lucas_2(9)==76, 'Lucas 2 (9) is 2. Failed!'
    assert lucas_2(26)==271443, 'Lucas 2 (26) is 2. Failed!'
    
    