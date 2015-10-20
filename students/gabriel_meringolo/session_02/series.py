
def fibonacci(n):
    '''returns the nth number in the fibonacci series'''
    return sum_series(n) # calls sum series using default parameters


def lucas(n):
    '''returns the nth number in the lucas numbers'''
    return sum_series(n,2,1) # calls sum series using specific arguments



def sum_series(n, x = 0, y = 1):
    '''nth number in series, default x and y for fib series, x = 2 and y = 1 for lucas numbers'''
    ser = [x,y] # creating a list with x/y parameters
    for i in range(n): # creates range
        ser.append(ser[-2] + ser[-1]) # appends list with next number in sequence
    return (ser[n - 1]) # returns nth number in sequence

if __name__ == "__main__":
    assert lucas(10) == 76
    assert fibonacci(10) == 34
    assert sum_series(10) == 34
    assert sum_series(10, 2, 1) == 76

"""asserts are cross-checking the function generated values for n with the
   actual value for n to ensure proper operation
"""


print(lucas(8))
print(sum_series(7))
print(fibonacci(2))
