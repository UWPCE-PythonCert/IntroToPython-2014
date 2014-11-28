# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## Demonstration of Decorators:
# 
#     (Adapted from Jon Jacky's Intro to Python class)
# 
# ### Creating a function in a function....

# <codecell>

def addn(n):
    def adder(i):
        return i + n
    return adder

# <markdowncell>

# NOTE: you oculd use lambda for something as simple as this...

# <codecell>

add2 = addn(2)

# <codecell>

add2 (1)

# <codecell>

add3 = addn(3)

# <codecell>

add3(1)

# <markdowncell>

# A function that takes a function as an argument, and returns a function can be a decorator.
# 
# It usually creates a function inside its scope...

# <markdowncell>

# Pass a function as an argument, use that to define the function you return.
# 
# (first a couple functions to use...)

# <codecell>

def odd(i):
    return i%2
def even(i):
    return not odd(i)

# <markdowncell>

# And write a wrapper for them....

# <codecell>

def sieve(f):
    def siever(s):
        return [x for x in s if f(x)]
    return siever

# <markdowncell>

# Make a couple of sieves:

# <codecell>

oddsieve = sieve(odd)
evensieve = sieve(even)

# <markdowncell>

# And try them out:

# <codecell>

s = range(10)
s

# <codecell>

oddsieve(s)

# <codecell>

evensieve(s)

# <markdowncell>

# The decorator operator @ abbreviates the preceding pattern
# 
# `@f
#    def g
# `
# means
# 
# `g = f(g)`

# <codecell>

@sieve
def osieve(i):
    return i % 2

@sieve
def esieve(i):
    return not (i % 2)

# <codecell>

osieve(s)

# <codecell>

esieve(s)

# <markdowncell>

# A callable class can be used as a function, so 
# you can also use a class as a decorator
# 
# (classes and objects are callable (via `__init__` and `__call__`))

# <codecell>

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

# <markdowncell>

# To use it -- the nifty decorator syntax:

# <codecell>

@Memoize        # same effect as sum2x = memoize(sum2x)
def sum2x(n):
    return sum(2 * i for i in xrange(n))  # takes time when n > 10 million

# <markdowncell>

# call it:

# <codecell>

sum2x(10)

# <codecell>

sum2x(10)

# <markdowncell>

# But slow if you call it with a big number:

# <codecell>

import time
start = time.clock()
sum2x(10000000)
print "it took %f seconds to run"%(time.clock() - start)

# <markdowncell>

# But the second time...

# <codecell>

import time
start = time.clock()
sum2x(10000000)
print "it took %f seconds to run"%(time.clock() - start)

# <markdowncell>

# Quiz time: what type of object is sum2x ?

# <codecell>

repr(sum2x)

# <codecell>


