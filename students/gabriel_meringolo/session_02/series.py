def fibonacci(n):
    '''returns the nth number in the fibonacci sequence'''
    fib = (0,1) # sets up fib sequence
    assert type(n) == int and n > 0, "ERROR: Argument must be IntType greater than 0."
    # assert checks for Int greater than zero, if false throws error
    for i in range(n):
        newFib = (fib[-2] + fib[-1]) # adds the last two numbers in sequence, creates next number...
        fib += (newFib,) # creates new tuple with old one and new number
    #print(fib) # for testing
    #print(fib[n - 1]) # for testing
    return (fib[n - 1]) # returns the nth number in the sequence, misusing one because seq starts at 0


def lucas(n):
    '''returns the nth number in the lucas sequence'''
    luc = (2,1) # sets up lucas sequence
    assert type(n) == int and n > 0, "ERROR: Argument must be IntType greater than 0."
    # assert checks for Int greater than zero, if false throws error
    for i in range(n):
        newLuc = (luc[-2] + luc[-1]) # adds the last two numbers in sequence, creates next number...
        luc += (newLuc,) # creates new tuple with old one and new number
    #print(luc) # for testing
    #print(luc[n - 1]) # for testing
    return (luc[n - 1]) # returns the nth number in the sequence, misusing one because seq starts at 0



def sum_series(n, x = 0, y = 1):
    '''returns nth number of fib sequence if x, y are default/ lucas numbers if x = 2, y = 1'''
    if x == 0 and y == 1:
        return fibonacci(n) # calls fib function if x, y are default
    elif x == 2 and y == 1:
        return lucas(n) # calls lucas function if x = 2 and y = 1
    else:
        return "Those are not accepted parameters." # throws error if not 0/1 or 2/1



print(fibonacci(4))
print(lucas(4))
print(sum_series(4))