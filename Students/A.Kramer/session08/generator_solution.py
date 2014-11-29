'''
Created on Nov 26, 2014

@author: Alekesey Kramer
'''

# Generator to add numbers to predecessors
def intsum():
    num = 0
    count = 0
    while num >= 0:
        yield num
        count += 1
        num += count


def doubler():
    num = 1
    while num >= 0:
        yield num
        num = num*2
        
def prime():
    # My code :-)
    count = 2
    while True:
        if __is_prime(count):
            yield count
            count += 1
        else:
            count += 1

# Found this code on the web at 
# https://www.daniweb.com/software-development/python/threads/70650/an-isprimen-function
# with combination from here: http://stackoverflow.com/questions/15285534/isprime-function-for-python-language
# and modified a bit to reject all the numbers lees than 2 (just in case I will use it later)
# quite useful and fast function, but limited by the have the size of int...
def __is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    # checking only odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# fibonacci
def fib():
    first = 1
    second = 1
    while True:
        yield(first)
        n = first + second
        first = second
        second = n


if __name__ == "__main__":
    print "Sum of integers"
    sum_of_ints = intsum()
    print sum_of_ints.next()
    print sum_of_ints.next()
    print sum_of_ints.next()
    print sum_of_ints.next()
    print sum_of_ints.next()
    print sum_of_ints.next()
    print
    print "Doubler"
    doub = doubler()
    print doub.next()
    print doub.next()
    print doub.next()
    print doub.next()
    print doub.next()
    print doub.next()
    print
    print "Getting Primes"
    g = prime()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print g.next()
    print
    print "Fibonacci"
    f = fib()
    print f.next()
    print f.next()
    print f.next()
    print f.next()
    print f.next()
    print f.next()
    print f.next()
    print f.next()
    print f.next()





