# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

def add(a,b):
    return a+b

# <codecell>

add(3,4)

# <markdowncell>

# What if we want to log when that function is called?

# <codecell>

def logged_add(a, b):
    print '### %s(%r, %r)' % ('add', a, b)
    result = add(a, b)
    print '### %s(%r, %r) --> %r' % ('add', a, b, result)
    return result

# <markdowncell>

# could change all calls to this -- blech!
# 
# so instead write a wrapper:

# <codecell>

def logged(func):
    def wrapper(a, b):
        print '### %s(%r, %r)' % (func.func_name, a, b)
        result = func(a, b)
        print '### %s(%r, %r) --> %r' % (func.func_name, a, b, result)
        return result
    return wrapper

# <markdowncell>

# re-define add...

# <codecell>

add = logged(add)

# <codecell>

add(3,4)

# <markdowncell>

# And use it for other functions, too:

# <codecell>

def subtract(a, b):
    """subtract() subtracts two things"""
    return a - b
subtract = logged(subtract)

# <codecell>

subtract(7,4)

# <markdowncell>

# Make it more general -- to take any number of arguments:

# <codecell>

def logged(func):
    def wrapper(*args):
        print '### %s(%s)' % (func.func_name, args)
        result = func(*args)
        print '### %s(%s) --> %r' % (func.func_name, args, result)
        return result
    return wrapper

# <markdowncell>

# A function with one argument:

# <codecell>

def even(a):
    """even() returns True if the value is even"""
    return a % 2 == 0
even = logged(even)

# <codecell>

even(3)

# <codecell>

even(4)

# <markdowncell>

# Wouldn't it be nice to have a cleaner syntax that this???

