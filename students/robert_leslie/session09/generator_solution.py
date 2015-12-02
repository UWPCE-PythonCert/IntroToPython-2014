#! /usr/bin/env python3


def intsum():
    i = 0
    last = 0
    while 1:
        last = last + i
        yield last
        i += 1


def intsum2():
    pass


def doubler():
    i = 1
    while 1:
        yield i
        i = i*2


def fib():
    pass


def prime():
    pass


if __name__ == '__main__':

    fib()
