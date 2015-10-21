def fib(n):
    """
    Fibonacci Series Exercise
    """
    if n < 2:
        return n
    else:    
        return fib( n-2) + fib (n-1)

# quick tests
#print (fib(1))
#print (fib(2))
#print (fib(3))
#print (fib(4))
#print (fib(5))
#print (fib(6))
assert (fib(1)) == 1
assert (fib(2)) == 1
assert (fib(3)) == 2
assert (fib(4)) == 3
assert (fib(5)) == 5
assert (fib(6)) != 5
assert (fib(6)) == 8
print ('Fibonacci number quick tests were successful')

def lucas(n):
    """ Lucas Numbers Exercise: starting with the value 2 and 1, instead of 0 and 1
    """
    if n  == 0:
        return 2
    if n == 1:
        return 1; 
    else:
        return lucas(n-2) + lucas (n-1)

# quick tests
#print (lucas(0))
#print (lucas(1))
#print (lucas(2))
#print (lucas(3))
#print (lucas(4))
#print (lucas(5))
assert (lucas(0)) == 2
assert (lucas(1)) == 1
assert (lucas(2)) == 3
assert (lucas(3)) == 4
print ('Lucas number quick tests were successful')