##Session 8: Callable Classes, Iterators, Generators  

###Callable Classes  

What do you do when you want to evaluate the same function several times with the same set of arguments?  

This is a good place to apply a callable -- something you can call like a function.  

A class object is itself a callable.

```python
__call__(*args, **kwargs)

class Callable(object):
    def __init__(self, ...._)
        some init stuff
    def __call__(self, some parameters)
````

**Key Sequence Protocols**  

    def__len__():
        pass

    def__getitem__():
        pass

    def__setitem__():
        pass

    def__delitem__():
        pass

    def__contains__():
        pass


###Iterators  
Any iterator has the method: ```python some_iterator.__iter__():```  
Followed by: ```python some_iterator.next()```  

With these two methods added to an object you can iterate over it

An iterable is something that can be iterated over.

An iterator is a class object that can be stepped through using next()  
(i.e. somthing that iter() has been called on)

**Some examples shown in class:**
```python
l = [2,4,5,7]

l.next()  #raises AttributeError
it = l.__iter__()  # returns list iterator method

type(it)
it.next() # will call the next item in the sequence

# for an arbitrary object iter() calls the __iter__ method
s = 'string'
iter(s)
```

_Itertools_ module allows easy construction of iterators over sequences that are passed into the  environment

iterators are useful in other capacities than calling for-type looping  
* sum
* sorted
* other stuff that works on an iterable or list

Python and Excel  
* DataNitro -- adds python shell to excel for a price
* ExcelPython v2 on GitHub -- seems very clunky, better off with Pandas and scipy


###Generators  
Generators give you the iterator immediately  
* No access to the underlying data
* Generator is an iterator that yields a value then stops
* State is preserved between yields

```python
gen_a = a_generator()
gen_b = b_generator()

def y_xrange(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

# a very simple generator function
def gen_fun():
    yield 1
    yield 2
    yield 3
```

dir(object) to get all available methods including magic

Comprehensions written with normal parens will return a generator object that allows access to generator methods so the list does not need to be copied.

Once the generator has been created it allows iteration on each individual item as well, this allows for v. efficient looping.

**Homework**  
* Finish labs
    + Quadractic class and sparse array
    + Extend iterator_1.py to act like xrange() with 3 x inputs
    + Turn sparse array into an iterator
    + Write generators for sum of integers, a doubler, fibonacci sequence, prime numbers  
* Start project and send proposal
