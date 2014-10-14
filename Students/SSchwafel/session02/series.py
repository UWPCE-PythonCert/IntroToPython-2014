#!/usr/bin/python


user_number = raw_input('Which term do you want from the Fibonacci or Lucas sequence?\n\n(be sure to ask for 0 if you want the first term from the sequence)\n\n')

user_number = int(user_number)
print

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
    """This function takes one required argument and two optional ones. 

    If the optional arguments are 2,1, return nth Lucas number, otherwise, return nth Fibonacci number. If other arguments are given, return none until other series can be programmed. 
    """

    if optional1 == 0 and optional2 == 1:
        return fibonacci(n)
    elif optional1 == 2 and optional2 == 1:
        return lucas(n)
    else:
        "It looks like you want a different series"

    
#Return Lucas value of user_number
print 'This is the Lucas number corresponding to the term you gave\n'
print sum_series(user_number,2,1)
print
print 'This is the Fibonacci number corresponding to the term you gave\n'
print sum_series(user_number,0,1)
print

if __name__ == "__main__":

    #check to see if the Fibonacci numbers returned match the first 4 known values
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(3) == 2
    assert fibonacci(5) == 5

    #check to see if the Lucas numbers returned match the first few known values (and the 6th for good measure)

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(3) == 4
    assert lucas(5) == 11

    #make sure that the sum_series function performs Fibonacci as expected, and Lucas as expected when given the necessary arguments

    assert sum_series(0) == 0
    assert sum_series(0,0,1) == 0
    assert sum_series(5,0,1) == 5
    assert sum_series(1,2,1) == 1
    assert sum_series(5,2,1) == 11
    assert sum_series(0) == 0


    print "\nAll Tests Pass!\n"
