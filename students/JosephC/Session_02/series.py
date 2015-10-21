#Intro to Python (via the University of Washington)

#Completed by: Joseph Cardenas, 10.17.2015

#This exercise prints the Fibonacci and Lucas series of numbers, then a third function which alternates
#between the two depending on the parameter the user enters

def fibonacci(n):
    """Return the value from running a Fibonacci sequence for the value n."""
#fib(n) = fib(n-2) + fib(n-1)
    if n == 1 or n == 0:
        return n
    elif n > 1:
        return fibonacci(n-2) + fibonacci(n-1)

print( "Fibonaccci with an n=9", fibonacci(9) )
print( "Fibonaccci with an n=1", fibonacci(1) )
print( "Fibonaccci with an n=10", fibonacci(10) )
print( "The computer starts grinding when n >= 35.")

print("-----------------------")
#this uses essentially the same formula as the above
""" The function below prints the lucas series of numbers."""
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1) + lucas(n-2)

print( "Lucas with an n=9", lucas(9) )
print( "Lucas with an n=1", lucas(1) )
print( "Lucas with an n=10", lucas(10) )
print( "Like with Fibonacci, n >= 35 starts to stress (my) computer.  N=99 would likely take half the day.")



#sum_series allows the user to choose which of the above functions are used
''' Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.'''
def sum_series(n, x = 0, y = 1):
   
    if n == 0:
        return x
    elif n == 1:
        return y
    elif n > 1:
        return sum_series(n-1, x, y) + sum_series(n-2, x, y) 



#check whether my functions produce the values they should
assert fibonacci(9) == 34
assert lucas(9) == 76
assert sum_series(0, 5, 6) == 5
assert sum_series(1, 5, 6) == 6
assert sum_series(2, 5, 6) == 11
assert sum_series(3, 5, 6) == 17
assert sum_series(5) == fibonacci(5)
assert sum_series(3, 2, 1) == lucas(3)
 

