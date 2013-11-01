#!/usr/bin/env python

"""
example code for using lambda, keywords, and keyword scope


The challenge:

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increaseing number.

you should use a for loop, lambda, and a keyword argument

extra credit: do it with a list comprhension, instead of a for loop

"""

def function_builder(n):

    l = []
    for i in range(n):
        l.append( lambda x, i=i: x+i )
    return l

def function_builder2(n):

    return [ lambda x, i=i: x+i for i in range(n) ]

