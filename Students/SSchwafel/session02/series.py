#!/usr/bin/python


user_number = raw_input('Which term do you want from the Fibonacci or Lucas sequence?\n')

user_number = int(user_number)

def fibonacci(n):
    """Return the nth value of the Fibonacci sequence of numbers"""

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):
    """Return the nth value of the Lucas sequence of numbers"""

    if n == 0:
        return 2

    elif n == 1:
        return 1

    elif n > 1:
        return lucas(n-1) + lucas(n-2)

#print lucas(user_number)
#print fibonacci(user_number)

def sum_series(n, optional1 = 0, optional2 = 1):

    if optional1 == 0 and optional2 == 1:
        return fibonacci(n)
    if optional1 == 2 and optional2 == 1:
        return lucas(n)

    
print sum_series(user_number,2,1)

    # This is where I am going to put my tests and asserts

if __name__ == "__main__":

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(3) == 2
    assert fibonacci(5) == 5

    print "\nAll Tests Pass!\n"
   # #
   # #
