def y_xrange(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step
  


def intsum():
    '''
    keep adding the next integer

    0 + 1 + 2 + 3 + 4 + 5 + ...

    so the sequence is:

    0, 1, 3, 6, 10, 15 .....
    '''
    i = 0
    sum = 0
    
    while True:
        sum = i + sum
        yield sum
        i += 1


def intsum2():
    '''
    test_generator has a intsum2... dunno why
    '''
    i = 0
    sum = 0
    
    while True:
        sum = i + sum
        yield sum
        i += 1

def doubler():
    '''
    Doubler:
    Each value is double the previous value:

    1, 2, 4, 8, 16, 32,
    '''
    sum = 1
    while True:
        yield sum
        sum += sum
 
def fib():
    '''
    Fibonacci sequence:
    The fibonacci sequence as a generator:

    f(n) = f(n-1) + f(n-2)

    1, 1, 2, 3, 5, 8, 13, 21, 34...
    '''
    yield 1
    x = 0
    y = 1
    while True:
        yield x+y
        x, y = y, x+y

    
        

        
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def prime(): 
    '''
    Prime numbers:
    Generate the prime numbers (numbers only divisible by them self and 1):

    2, 3, 5, 7, 11, 13, 17, 19, 23...
    '''
    i = 2
    while True:
        while not isprime (i):
            i += 1
        yield i
        i += 1