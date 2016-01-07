.. include:: include.rst

**************************************************
Session Nine: Iterators, Iterables, and Generators
**************************************************

.. rst-class:: large centered

The tools of Pythonicity


======================
Lightning Talks Today:
======================

.. rst-class:: medium

    Erica Winberry

    Robert Jenkins

    Kathleen Devlin

================
Review/Questions
================

Review of complete sparse array class


=========================
Iterators and Generators
=========================

.. rst-class:: medium

    What goes on in those for loops?

Iterators and Iterables
-----------------------

Iteration is one of the main reasons Python code is so readable:

.. code-block:: python

    for x in just_about_anything:
        do_stuff(x)

An iterable is anything that can be looped over sequentially, so it does not have to be
a "sequence": list, tuple, etc.  For example, a string is iterable.

An iterator is an iterable that remembers state. All sequences are iterable, but
not all sequences are iterators. To make a sequence an iterator, you can call it with iter:

.. code-block:: python

   my_iter = iter(my_sequence)

Iterator Types:

https://docs.python.org/3/library/stdtypes.html#iterator-types

Iterables
---------

To make an object iterable, you simply have to implement the __getitem__ method.

.. code-block:: python

    class T:
        def __getitem__(self, position):
        if position > 5:
            raise IndexError
        return position

Demo


``iter()``
-----------

How do you get the iterator object from an "iterable"?

The iter function will make any iterable an iterator. It first looks for the __iter__
method, and if none is found, uses get_item to create the iterator.

The ``iter()`` function:

.. code-block:: ipython

    In [20]: iter([2,3,4])
    Out[20]: <listiterator at 0x101e01350>

    In [21]: iter("a string")
    Out[21]: <iterator at 0x101e01090>

    In [22]: iter( ('a', 'tuple') )
    Out[22]: <tupleiterator at 0x101e01710>


List as an Iterator:
--------------------

.. code-block:: ipython

    In [10]: a_list = [1,2,3]

    In [11]: list_iter = iter(a_list)

    In [12]: next(list_iter)
    Out[12]: 1

    In [13]: next(list_iter)
    Out[13]: 2

    In [14]: next(list_iter)
    Out[14]: 3

    In [15]: next(list_iter)
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 next(list_iter)
    StopIteration:


The Iterator Protocol
----------------------

The main thing that differentiates an iterator from an iterable (sequence) is that an iterator saves state.

An iterator must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Returns the iterator object itself.

.. code-block:: python

    an_iterator.__next__()

Returns the next item from the container. If there are no further items,
raises the ``StopIteration`` exception.


Making an Iterator
-------------------

A simple version of ``range()``

.. code-block:: python

    class IterateMe_1:
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def __next__(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration

(demo: :download:`iterator_1.py <../../Examples/Session09/iterator_1.py>`)

What does ``for`` do?
----------------------

Now that we know the iterator protocol, we can write something like a for loop:


:download:`my_for.py <../../Examples/Session09/my_for.py>`

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
                i = next(iterator)
            except StopIteration:
                break
            func(i)


Itertools
---------

``itertools``  is a collection of utilities that make it easy to
build an iterator that iterates over sequences in various common ways

http://docs.python.org/3/library/itertools.html

NOTE:

iteratables are not *only* for ``for``

They can be used with anything that expects an iterable:

``sum``, ``tuple``, ``sorted``, and ``list``


LAB
-----

In the ``Examples/session09`` dir, you will find:
:download:`iterator_1.py <../../Examples/Session09/iterator_1.py>`

* Extend (``iterator_1.py`` ) to be more like ``range()`` -- add three input parameters: ``iterator_2(start, stop, step=1)``

* What happens if you break from a loop and try to pick it up again:

.. code-block:: python

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)

.. code-block:: python

    for i in it:
        print(i)

* Does ``range()``  behave the same?

  - make yours match ``range()``

  - is range an iterator or an iteratable?


Generators
----------

Generators

* give you an iterator object
* no access to the underlying data ... if it even exists


Conceptually:
  Iterators are about various ways to loop over data.

  Generators can generate the data on the fly.

Practically:
  You can use either one either way (and a generator is one type of iterator).

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

An example: like ``range()``

.. code-block:: python

    def y_range(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

Real World Example from FloatCanvas:

https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L100


.. nextslide::

Note:

.. code-block:: ipython

    In [164]: gen = y_range(2,6)
    In [165]: type(gen)
    Out[165]: generator
    In [166]: dir(gen)
    Out[166]:
    ...
     '__iter__',
    ...
     '__next__',


So the generator **is** an iterator

Note: A generator function can also be a method in a class


.. More about iterators and generators:

.. http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

:download:`yield_example.py <../../Examples/Session09/yield_example.py>`

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
:download:`test_generator.py <../../Examples/Session09/test_generator.py>`)

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


==========
Next Week
==========

Decorators and Context managers -- fun stuff!

Cris Ewing will come by to talk about the second quarter
web development class

Homework
---------

Finish up the labs

Work on your project -- not much time left!

And *do* let me know what you're doing if you haven't yet!
