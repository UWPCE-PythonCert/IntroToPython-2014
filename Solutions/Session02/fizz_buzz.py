#!/usr/bin/env python

"""
Fizz Buzz examples -- from most straightforward, to most compact.
"""


# basic approach:
def fizzbuzz1(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)


def fizzbuzz2(n):
    """
    Why evaluate i%3 and i%5 twice?
    """
    for i in range(1, n + 1):
        msg = ''
        if i % 3 == 0:
            msg += "Fizz"
        if i % 5 == 0:
            msg += "Buzz"
        if msg:
            print(msg)
        else:
            print(i)


def fizzbuzz3(n):
    """
    Or print on one line...
    """
    for i in range(1, n + 1):
        num = True
        if i % 3 == 0:
            print("\nFizz", end='')
            num = False
        if i % 5 == 0:
            if num:
                print()
            print("Buzz", end='')
            num = False
        else:
            if num:
                print("\n", i, end='')


def fizzbuzz4(n):
    """
    use conditional expressions:
    """
    for i in range(1, n + 1):
        msg = "Fizz" if i % 3 == 0 else ''
        msg += "Buzz" if i % 5 == 0 else ''
        print(msg or i)


def fizzbuzz5(n):
    """
    a one liner
    """
    for i in range(1, n + 1): print (("Fizz" * (not (i % 3)) + "Buzz" * (not (i % 5))) or i)


if __name__ == "__main__":
    fizzbuzz1(16)
    print()
    fizzbuzz2(16)
    print()
    fizzbuzz3(16)
    print()
    fizzbuzz4(16)
    print()
    fizzbuzz4(16)
    print()
