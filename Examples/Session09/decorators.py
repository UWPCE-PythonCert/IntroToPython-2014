# -*- coding: utf-8 -*-


def substitute(a_function):
    """return a different function than the one supplied"""
    def new_function(*args, **kwargs):
        return "I'm not that other function"
    return new_function


def add(a, b):
    print "Function 'add' called with args: %r" % locals()
    result = a + b
    print "\tResult --> %r" % result
    return result


def logged_func(func):
    def logged(*args, **kwargs):
        print "Function %r called" % func.__name__
        if args:
            print "\twith args: %r" % (args, )
        if kwargs:
            print "\twith kwargs: %r" % kwargs
        result = func(*args, **kwargs)
        print "\t Result --> %r" % result
        return result
    return logged


def simple_add(a, b):
    return a + b


class Memoize:
    """
    memoize decorator from avinash.vora
    http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    """
    def __init__(self, function):  # runs when memoize class is called
        self.function = function
        self.memoized = {}

    def __call__(self, *args):  # runs when memoize instance is called
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


@Memoize
def sum2x(n):
    return sum(2 * i for i in xrange(n))

import time


def timed_func(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed

@timed_func
@Memoize
def sum2x(n):
    return sum(2 * i for i in xrange(n))
