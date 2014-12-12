##Session 09: Decorators, Context Managers, Packages and packaging  

###Decorators  
Functions are things that generate values based on input. (First class objects.)

*Decorators* are functions that take a function as an argument and return a function value.

Consider the case where you are debugging a function and start adding print statements as a way to see what's going on:

```python
def add(a, b):
    print "Function 'add' called with args: %r, %r"%(a, b)
    result = a + b
    print "\tResult --> %r" % result
    return result

## pretty clunky, so let's write a function that does it for us

def logged_func(func):
    def logged(*args, **kwargs):
        print "Function %r called" % func.__name__
        if args:
            print "\twith args: %r" % args
        if kwargs:
            print "\twith kwargs: %r" % kwargs
        result = func(*args, **kwargs)  # this is the function that was passed into logged_func
        print "\t Result --> %r" % result
        return result
    return logged

## now remap / rebind add to the logged function
def logged_func(func):
    #as shown

def add(a, b):
    return a + b
add = logged_func(add)  # intentionally oudented

# declarative form of the rebound function above
@logged_func
def add(a, b):
    return a + b
```

The "@" symbol is the declaration, it must precede the decorated function.

Decorators are very common and frequntly previously defined decorators are applied (need to write original decorators is limited)  
Examples:  
* @property
* @x.setter
* @x.deleter
* @parameterize

####property()  
```python
#the code:
class C(object):
    def __init__(self):
        self._x = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

#is equivalent to:

class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx,
                 "I'm the 'x' property.")
```

###Context Managers

A way to access resources withouth leaving resources open, e.g. opening a file, running a process, hitting an exception and leaving it open

*with* will perform actions in context defensively, if something goes wrong the resource is always closed

```python
with open('fileneame.ext') as fid:
    do a bunch of stuff
# file is automatically closed by outdent
```

**netcdf** module works with oceanographic and meteorologic data

**Creating your own context manager:**  
Requires special dunder methods  
* __enter__(self)
* __??__(self)
* __exit__(self, e_type, e_val, e_traceback)

*Doug Hellmann's Python Module of the Week http://pymotw.com*

contextlib.contextmanager has a decorator as well

```python
from contextlib import contextmanager

@contextmanager
def context(boolean):
print "__init__ code here"
try:
    #instructions
except:
    #exceptions
finally:
    # __exit__ cleanup goes here
```


