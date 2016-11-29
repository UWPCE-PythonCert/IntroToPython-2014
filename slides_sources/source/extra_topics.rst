.. _extra_topics:

************
Extra Topics
************

Here are some extra topics that we didn't have time for in the regular class sessions:

==============================
Closures and function Currying
==============================

Defining specialized functions on the fly

Closures
--------

"Closures" and "Currying" are cool CS terms for what is really just defining functions on the fly.

you can find a "proper" definition here:

https://en.wikipedia.org/wiki/Closure_(computer_programming)

but I even have trouble following that.

So let's go straight to an example:

.. nextslide::

.. code-block:: python

    def counter(start_at=0):
        count = [start_at]
        def incr():
            count[0] += 1
            return count[0]
        return incr

What's going on here?

We have stored the ``start_at`` value in a list.

Then defined a function, ``incr`` that adds one to the value in the list, and returns that value.

[ Quiz: why is it: ``count = [start_at]``, rather than just ``count=start_at`` ]

.. nextslide::

So what type of object do you get when you call ``counter()``?

.. code-block:: ipython

    In [37]: c = counter(start_at=5)

    In [38]: type(c)
    Out[38]: function

So we get a function back -- makes sense. The ``def`` defines a function, and that function is what's getting returned.

Being a function, we can, of course, call it:

.. code-block:: ipython

    In [39]: c()
    Out[39]: 6

    In [40]: c()
    Out[40]: 7

Each time is it called, it increments the value by one.

.. nextslide::

But what happens if we call ``counter()`` multiple times?

.. code-block:: ipython

    In [41]: c1 = counter(5)

    In [42]: c2 = counter(10)

    In [43]: c1()
    Out[43]: 6

    In [44]: c2()
    Out[44]: 11

So each time ``counter()`` is called, a new function is created. And that function has its own copy of the ``count`` object. This is what makes in a "closure" -- it carries with it the scope in which is was created.

the returned ``incr`` function is a "curried" function -- a function with some parameters pre-specified.

``functools.partial``
---------------------

The ``functools`` module in the standard library provides utilities for working with functions:

https://docs.python.org/3.5/library/functools.html

Creating a curried function turns out to be common enough that the ``functools.partial`` function provides an optimized way to do it:

What functools.partial does is:

 * Makes a new version of a function with one or more arguments already filled in.
 * The new version of a function documents itself.

Example:

.. code-block:: python

    def power(base, exponent):
        """returns based raised to the give exponent"""
        return base ** exponent

Simple enough. but what if we wanted a specialized ``square`` and ``cube`` function?

We can use ``functools.partial`` to *partially* evaluate the function, giving us a specialized version:

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

Reading:
--------

http://www.pydanny.com/python-partials-are-fun.html

https://pymotw.com/3/functools/

http://www.programiz.com/python-programming/closure

https://www.clear.rice.edu/comp130/12spring/curry/

