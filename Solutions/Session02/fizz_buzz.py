#!/usr/bin/env python

"""
Fizz Buzz examples -- from most straightforward, to most compact.
"""


# basic approach:
def fizzbuzz1(n):
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print "FizzBuzz"
        elif i%3 == 0:
            print "Fizz"
        elif i%5 == 0:
            print "Buzz"
        else:
            print i


def fizzbuzz2(n):
    """
    Why evaluate i%3 and i%5 twice?
    """
    for i in range(1, n+1):
        msg = ''
        if i%3 == 0:
            msg += "Fizz"
        if i%5 == 0:
            msg += "Buzz"
        if msg:
            print msg
        else:
            print i


def fizzbuzz3(n):
    """
    use conditional expressions:
    """
    for i in range(1, n+1):
        msg = "Fizz" if i%3 == 0 else ''
        msg += "Buzz" if i%5 == 0 else ''
        print msg or i


def fizzbuzz4(n):
    """
    the one liner
    """
    for i in range(1,n+1): print ( "Fizz" * (not (i%3)) + "Buzz" * (not (i%5)) ) or i


def fizzbuzz_ruby(n):
    """
    This is a one-liner version inspired by the Ruby one-liner
    found here:

    http://www.commandercoriander.net/blog/2013/02/03/fizzbuzz-in-one-line

    This uses list comprehensions, and slicing, and is, well, pretty darn ugly!

    """
    for word in [ ("".join(["Fizz",][0:1-i%3]+["Buzz",][0:1-i%5]) or `i`) for i in range(1, n+1)]: print word

if __name__ == "__main__":
    fizzbuzz1(16)
    print
    fizzbuzz2(16)
    print
    fizzbuzz3(16)
    print
    fizzbuzz4(16)
    print
    fizzbuzz_ruby(16)


