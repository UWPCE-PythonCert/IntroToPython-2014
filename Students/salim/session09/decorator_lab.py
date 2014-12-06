#!/usr/bin/env python


def p_wrapper(func):
    def wrap(string, tag):
        return '<{}>{}</{}>'.format(tag, string.strip(), tag)
    return wrap

@p_wrapper
def return_a_string():
    return

return_a_string('this is my string', 'p')


# class example
def logged_func(func):
    def logged(*args, **kwargs):
        print "Function %r called" % func.__name__
        if args:
            print "\twith args: %r" % args
        if kwargs:
            print "\twith kwargs: %r" % kwargs
        result = func(*args, **kwargs)
        print "\t Result --> %r" % result
        return result
    return logged

@logged_func
def add(a, b):
    return a + b
