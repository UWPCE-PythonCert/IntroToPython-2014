******************************************************
Session Eight: Callable classes, Iterators, Generators
******************************************************

.. rst-class:: large centered

The tools of Pythonicity


================
Review/Questions
================

Review of Previous Class
------------------------

* Advanced OO Concepts

  * Properties
  * Special Methods

Homework review
---------------

* Circle Class
* Writing Tests using the ``pytest`` module

Lightning Talks Today:
-----------------------

.. rst-class:: medium

Alireza Hashemloo

Arielle R Simmons

Eric W Westman

Ryan J Albright

=========================
Emulating Standard types
=========================

.. rst-class:: medium

  Making your classes behave like the built-ins


Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)

.. nextslide::

But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable(object):
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)


Writing your own sequence type
-------------------------------

Python has a handful of nifty sequence types built in:

 * lists
 * tuples
 * strings
 * ...

But what if you need a sequence that isn't built in?

A Sparse array
--------------

Example: Sparse Array

Sometimes we have data sets that are "sparse" -- i.e. most of the values are zero.

So you may not want to store a huge bunch of zeros.

But you do want the array to look like a regular old sequence.

So how do you do that?

The Sequence protocol
----------------------

You can make your class look like a regular python sequence by defining
the set of special methods you need:

https://docs.python.org/2/reference/datamodel.html#emulating-container-types

and

http://www.rafekettler.com/magicmethods.html#sequence

The key ones are:

+-------------------+-----------------------+
|  ``__len__``      | for ``len(sequence)`` |
+-------------------+-----------------------+
|  ``__getitem__``  | for  ``x = seq[i]``   |
+-------------------+-----------------------+
|  ``__setitem__``  | for ``seq[i] = x``    |
+-------------------+-----------------------+
|  ``__delitem__``  | for ``del seq[i]``    |
+-------------------+-----------------------+
|  ``__contains__`` | for ``x in seq``      |
+-------------------+-----------------------+

====
LAB
====

.. rst-class:: medium

    Let's do the previous motivating examples.

Callables:
-----------

Write a class for a quadratic equation.

* The initializer for that class should take the parameters: ``a, b, c``

* It should store those parameters as attributes.

* The resulting instance should evaluate the function when called, and return the result:


.. code-block:: python

    my_quad = Quadratic(a=2, b=3, c=1)

    my_quad(0)

Sparse Array:
-------------

Write a class for a sparse array

* Internally, it can store the values in a dict, with the index as the keys)

* It should take a sequence of values as an initializer

* you should be able to tell how long it is: ``len(my_array)``

* It should support getting and setting particular elements via indexing.

* It should support deleting an element by index.

* It should raise an ``IndexError`` if you try to access an index beyond the end.

* Can you make it support slicing?

* How else can you  make it like a list?

.. code-block:: ipython

    In [10]: my_array = SparseArray( (1,0,0,0,2,0,0,0,5) )
    In [11]: my_array[4]
    Out[11]: 2
    In [12]: my_array[2]
    Out[12]: 0

Lightning Talks
----------------

.. rst-class:: medium

|
| Alireza Hashemloo
|
| Arielle R Simmons
|


=========================
Iterators and Generators
=========================

.. rst-class:: medium

    What goes on in those for loops?

Iterators
---------

Iterators are one of the main reasons Python code is so readable:

.. code-block:: python

    for x in just_about_anything:
        do_stuff(x)

It does not have to be a "sequence": list, tuple, etc.

Rather: you can loop through anything that satisfies the "iterator protocol"

http://docs.python.org/library/stdtypes.html#iterator-types

The Iterator Protocol
----------------------

An iterator must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Returns the iterator object itself. This is required to allow both containers
and iterators to be used with the ``for`` and ``in`` statements.

.. code-block:: python

    an_iterator.next()

Returns the next item from the container. If there are no further items,
raises the ``StopIteration`` exception.

List as an Iterator:
--------------------

.. code-block:: ipython

    In [10]: a_list = [1,2,3]

    In [11]: list_iter = a_list.__iter__()

    In [12]: list_iter.next()
    Out[12]: 1

    In [13]: list_iter.next()
    Out[13]: 2

    In [14]: list_iter.next()
    Out[14]: 3

    In [15]: list_iter.next()
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 list_iter.next()
    StopIteration:

Making an Iterator
-------------------

A simple version of ``xrange()``

.. code-block:: python

    class IterateMe_1(object):
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def next(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration

(demo: :download:`iterator_1.py <../../Examples/Session08/iterator_1.py>`)

``iter()``
-----------

How do you get the iterator object (the thing with the next() method) from an "iterable"?

The ``iter()`` function:

.. code-block:: ipython

    In [20]: iter([2,3,4])
    Out[20]: <listiterator at 0x101e01350>

    In [21]: iter("a string")
    Out[21]: <iterator at 0x101e01090>

    In [22]: iter( ('a', 'tuple') )
    Out[22]: <tupleiterator at 0x101e01710>

for an arbitrary object, ``iter()`` calls the ``__iter__`` method. But it knows about some objects (``str``, for instance) that don't have a ``__iter__`` method.


What does ``for`` do?
----------------------

Now that we know the iterator protocol, we can write something like a for loop:


:download:`my_for.py <../../Examples/Session08/my_for.py>`

.. code-block:: python

    def my_for(an_iterable, func):
        """
        Emulation of a for loop.

        func() will be called with each item in an_iterable
        """
        # equiv of "for i in l:"
        iterator = iter(an_iterable)
        while True:
            try:
                i = iterator.next()
            except StopIteration:
                break
            func(i)


Itertools
---------

``itertools``  is a collection of utilities that make it easy to
build an iterator that iterates over sequences in various common ways

http://docs.python.org/library/itertools.html

NOTE:

iterators are not *only* for ``for``

They can be used with anything that expects an iterator:

``sum``, ``tuple``, ``sorted``, and ``list``

For example.

LAB
-----

In the ``Examples/session08`` dir, you will find:
:download:`iterator_1.py <../../Examples/Session08/iterator_1.py>`

* Extend (``iterator_1.py`` ) to be more like ``xrange()`` -- add three input parameters: ``iterator_2(start, stop, step=1)``

* See what happens if you break out in the middle of the loop:

.. code-block:: python

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print i

And then pick up again:

.. code-block:: python

    for i in it:
        print i

* Does ``xrange()``  behave the same?

  - make yours match ``xrange()``

LAB2
-----

Make the SparseArray class from the previous lab an iterator, so you can do:

.. code-block:: python

    for i in my_sparse_array:
        do_something_with(i)


Lightning Talks
----------------

.. rst-class:: medium

|
| Eric W Westman
|
| Ryan J Albright
|



Generators
----------

Generators give you the iterator immediately:

* no access to the underlying data ... if it even exists


Conceptually:
  Iterators are about various ways to loop over data, generators generate the data on the fly.

Practically:
  You can use either one either way (and a generator is one type of iterator)

  Generators do some of the book-keeping for you -- simpler syntax.

yield
------

``yield``  is a way to make a quickie generator with a function:

.. code-block:: python

    def a_generator_function(params):
        some_stuff
        yield something

Generator functions "yield" a value, rather than returning a value.

State is preserved in between yields.


.. nextslide:: generator functions

A function with ``yield``  in it is a "factory" for a generator

Each time you call it, you get a new generator:

.. code-block:: python

    gen_a = a_generator()
    gen_b = a_generator()

Each instance keeps its own state.

Really just a shorthand for an iterator class that does the book keeping for you.

.. nextslide::

An example: like ``xrange()``

.. code-block:: python

    def y_xrange(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

Real World Example from FloatCanvas:

https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L100


.. nextslide::

Note:

.. code-block:: ipython

    In [164]: gen = y_xrange(2,6)
    In [165]: type(gen)
    Out[165]: generator
    In [166]: dir(gen)
    Out[166]:
    ...
     '__iter__',
    ...
     'next',


So the generator **is** an iterator

Note: A generator function can also be a method in a class


.. More about iterators and generators:

.. http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

:download:`yield_example.py <../../Examples/Session08/yield_example.py>`

generator comprehension
-----------------------

yet another way to make a generator:

.. code-block:: python

    ￼>>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print n
    ... 2 4 6


More interesting if [1, 2, 3] is also a generator

LAB
----

Write a few generators:

* Sum of integers
* Doubler
* Fibonacci sequence
* Prime numbers

(test code in
:download:`test_generator.py <../../Examples/Session08/test_generator.py>`)

Descriptions:

Sum of the integers:
  keep adding the next integer

  0 + 1 + 2 + 3 + 4 + 5 + ...

  so the sequence is:

  0, 1, 3, 6, 10, 15 .....

.. nextslide::

Doubler:
  Each value is double the previous value:

  1, 2, 4, 8, 16, 32,

Fibonacci sequence:
  The fibonacci sequence as a generator:

  f(n) = f(n-1) + f(n-2)

  1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers:
  Generate the prime numbers (numbers only divisible by them self and 1):

  2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
  Try x^2, x^3, counting by threes, x^e, counting by minus seven, ...


========
Homework
========

.. rst-class:: left medium

    Finish up the Labs from class

    Get started on your project!

    (Send me a proposal if you haven't already)
