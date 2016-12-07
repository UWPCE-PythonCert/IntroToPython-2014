.. include:: include.rst

************************************************************
Anonymous Functions and Iterators, Iterables, and Generators
************************************************************

====================
Lightning Talks Now:
====================

.. rst-class:: medium

    Jack M Hefner

    Ninad Naik

    Simbarashe P Change


===================
Anonymous functions
===================

lambda
------

.. code-block:: ipython

    In [171]: f = lambda x, y: x+y
    In [172]: f(2,3)
    Out[172]: 5

Content of function can only be an expression -- not a statement

Anyone remember what the difference is?

Called "Anonymous": it doesn't get a name.

.. nextslide::

It's a python object, it can be stored in a list or other container

.. code-block:: ipython

    In [7]: l = [lambda x, y: x+y]
    In [8]: type(l[0])
    Out[8]: function


And you can call it:

.. code-block:: ipython

    In [9]: l[0](3,4)
    Out[9]: 7


Functions as first class objects
---------------------------------

You can do that with "regular" functions too:

.. code-block:: ipython

    In [12]: def fun(x,y):
       ....:     return x+y
       ....:
    In [13]: l = [fun]
    In [14]: type(l[0])
    Out[14]: function
    In [15]: l[0](3,4)
    Out[15]: 7



======================
Functional Programming
======================

No real consensus about what that means.

But there are some "classic" methods available in Python.

map
---

``map``  "maps" a function onto a sequence of objects -- It applies the function to each item in the list, returning another list


.. code-block:: ipython

    In [23]: l = [2, 5, 7, 12, 6, 4]
    In [24]: def fun(x):
                 return x*2 + 10
    In [25]: map(fun, l)
    Out[25]: <map at 0x104552b38>

Huh? what's a "map" object? It's an iterator (more on that later).

.. code-block:: ipython

    In [19]: list(map(fun, l))
    Out[19]: [14, 20, 24, 34, 22, 18]

Ah, that's better.

But if it's a small function, and you only need it once:

.. code-block:: ipython

    In [26]: list(map(lambda x: x*2 + 10, l))
    Out[26]: [14, 20, 24, 34, 22, 18]


filter
------

``filter``  "filters" a sequence of objects with a boolean function --
It keeps only those for which the function is True -- filtering out the rest.

To get only the even numbers:

.. code-block:: ipython

    In [27]: l = [2, 5, 7, 12, 6, 4]
    In [28]: list(filter(lambda x: not x%2, l))
    Out[28]: [2, 12, 6, 4]

If you pass ``None`` to ``filter()``, you get only items that evaluate to true:

.. code-block:: ipython

    In [1]: l = [1, 0, 2.3, 0.0, 'text', '', [1,2], [], False, True, None ]

    In [2]: list(filter(None, l))
    Out[2]: [1, 2.3, 'text', [1, 2], True]


Comprehensions
--------------

Couldn't you do all this with comprehensions?

Yes:

.. code-block:: ipython

    In [33]: [x+2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]

    In [34]: [x for x in l if not x%2]
    Out[34]: [2, 12, 6, 4]

    In [6]: l
    Out[6]: [1, 0, 2.3, 0.0, 'text', '', [1, 2], [], False, True, None]
    In [7]: [i for i in l if i]
    Out[7]: [1, 2.3, 'text', [1, 2], True]


Functional Programming
----------------------

Comprehensions, map, and filter are all "functional programming" approaches

``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

Some people like that syntax better

And "map-reduce" is a big concept these days for parallel processing of "Big Data" in NoSQL databases.

(Hadoop, MongoDB, etc.)


A bit more about lambda
------------------------

It is very useful for specifying the sorting key:

.. code-block:: ipython

    In [55]: lst = [("Chris","Barker"), ("Fred", "Jones"), ("Zola", "Adams")]

    In [56]: lst.sort()

    In [57]: lst
    Out[57]: [('Chris', 'Barker'), ('Fred', 'Jones'), ('Zola', 'Adams')]

    In [58]: lst.sort(key=lambda x: x[1])

    In [59]: lst
    Out[59]: [('Zola', 'Adams'), ('Chris', 'Barker'), ('Fred', 'Jones')]

lambda and keyword arguments
----------------------------

.. code-block:: ipython

    In [186]: l = []
    In [187]: for i in range(3):
        l.append(lambda x, e=i: x**e)
       .....:
    In [189]: for f in l:
        print(f(3))
    1
    3
    9

Note when the keyword argument is evaluated: this turns out to be very handy!

===
LAB
===

Here's an exercise to try out some of this:

:ref:`exercise_lambda_magic`



===
LAB
===

Let's use some of this ability to use functions a objects for something useful:

:ref:`exercise_trapezoidal_rule`


=========================
Iterators and Generators
=========================


.. rst-class:: large centered

  The Tools of Pythonicity


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

Using iterators when you can
----------------------------

Example: trigrams:

.. code-block:: ipython

    triplets = zip(words, words[1:], words[2:])

zip() returns an iterable -- it does not build up the whole list.
So this is quite efficient.

but slicing: ([1:]) produces a copy -- so this does use three copies of
the list -- not so good if memory is tight. Note that they are shallow copies, so not **that** bad.

Nevertheless, we can do better:

.. code-block:: ipython

    from itertools import islice

    In [68]: triplets = zip(words, islice(words, 1, None), islice(words, 2, None))

    In [69]: for triplet in triplets:
        ...:     print(triplet)
        ...:
    ('this', 'that', 'the')
    ('that', 'the', 'other')
    ('the', 'other', 'and')
    ('other', 'and', 'one')
    ('and', 'one', 'more')


The Iterator Protocol
----------------------

The main thing that differentiates an iterator from an iterable (sequence)
is that an iterator saves state.

An iterable must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Usually returns the iterator object itself.

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


More about iterators and generators:

http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

:download:`yield_example.py <../../Examples/Session09/yield_example.py>`

generator comprehension
-----------------------

yet another way to make a generator:

.. code-block:: python

    >>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print n
    ... 2 4 6


More interesting if [1, 2, 3] is also a generator

Note that `map` and `filter` produce iterators.

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


Homework
---------

Finish up the labs

Work on your project -- not much time left!

And *do* let me know what you're doing if you haven't yet!
