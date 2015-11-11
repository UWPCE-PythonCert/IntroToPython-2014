.. _exercise_trapezoidal_rule:

*****************
Trapezoidal Rule
*****************

Passing functions around
=========================


.. rst-class:: large left

    Goal:

.. rst-class:: medium left

    Making use of functions as objects -- functions that act on functions.


Trapezoidal rule
----------------

.. rst-class:: medium

  The "trapezoidal rule":

  https://en.wikipedia.org/wiki/Trapezoidal_rule

  Is one of the easiest "quadrature" methods.

  Otherwise known as computing a definite integral, or, simply,

  Computing the area under a curve.

The task
--------

Your task is to write a ``trapz()`` function that will compute the area under an arbitrary function, using the trapezoidal rule.

The function will take another function as an argument, as well as the start and end points to compute, and return the area under the curve.

Example:
--------

.. code-block:: python

    def line(x):
        '''a very simple straight horizontal line'''
        return 3

    area = trapz(line, 0, 10)

    area
    50

About the simplest "curve" you can have is a horizontal straight line, in this case, at y = 5. The area under that line from 0 to 10 is a rectangle that is 10 wide and 5 high, so with an area of 50.

Of course in this case, it's easiest to simply multiply the height times the width, but we want a function that will work for **Any** curve.

HINT: this simple example could be a good test case!

The Solution:
-------------

Your function definition should look like:

.. code-block:: python

  def trapz(fun, a, b):
      """
      Compute the area under the curve defined by
      y = fun(x), for x between a and b

      :param fun: the function to evaluate
      :type fun: a function that takes a single parameter

      :param a: the start point for teh integration
      :type a: a numeric value

      :param b: the end point for the integration
      :type b: a numeric value
      """
      pass

.. nextslide::

In the function, you want to compute the following equation:

.. math::

    result = \frac{b-a}{2N}(f(x_1) + 2f(x_2) + 2f(x_3) + 2f(x_4) + \dotsb + 2f(x_N) + f(x_{N+1}))

So you will need to:

 - create a list of x values from a to b (maybe 100 or so values to start)

 - compute the function for each of those values and double them

 - add them all up

 - multiply by the half of the difference between a and b.

Note that the first and last values are not doubled.

Can you use comprehensions for this?

NOTE: ``range()`` only works for integers -- how can you deal with that?

.. nextslide::

Once you have that, it should work for any function that can be evaluated between a and b.

Try it for some built-in math functions, like ``math.sin``

tests
-----

Do this using test-drive development.

A few examples:

A simple horizontal line -- see above.

A sloped straight line:

.. math::

  \int_a^b  y = mx + B = \frac{1}{2} m (b^2-a^2) + B (b-a)

The sine function:

.. math::

  \int_a^b \sin(x) = -\cos(b) + \cos(a)

Computational Accuracy
----------------------

In the case of the linear functions, the result should theoretically be exact. But with the vagaries of floating point math may not be.

And for non-linear functions, the result will certainly not be exact.

So you want to check if the answer is *close* to what you expect.

In py3.5 -- there is an ``isclose()`` function (PEP485)

https://www.python.org/dev/peps/pep-0485/

In earlier pythons -- you'll need your own. There is one in:

``Examples/Session06/test_trapz.py``



Stage two:
----------

Some functions need extra parameters to do their thing. But the above will only handle a single parameter. For example, a quadratic function:

.. math::

    y = a x^2 + bx + c

Requires values for a, b, and c in order to compute y from an given x.

You could write a specialized version of this function for each a, b, and c:

.. code-block:: python

  def quad1(x):
      return 3 + x**2 + 2 + 4

But then you need to write a new function for any value of these parameters you might need.

.. nextslide::

Instead, you can pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a=0, b=0, c=0):
        return a * x**2 + b * x + c

Nice and general purpose.

But how would we compute the area under this function? the function we wrote above only passes x in to the function it is integrating.

Passing arguments through:
--------------------------

Update your trapz() function so that you can give it a function that takes arbitrary extra arguments, either positional or keyword, after the x.

So you can do:

.. code-block:: python

    trapz(quadratic, 2, 20, a=1, b=3, c=2)

or

.. code-block:: python

    trapz(quadratic, 2, 20, 1, 3, c=2)

or

.. code-block:: python

    coef = {'a':1, 'b':3, 'c': 2}
    trapz(quadratic, 2, 20, **coef)


Currying
--------

Another way to solve the above problem is to use the original ``trapz``, and create a custom version of the quadratic() function instead.

Write a function that takes ``a, b, and c`` as arguments, and returns a function that evaluates the quadratic for those particular coefficients.

Try passing the results of this into your ``trapz()`` and see if you get the same answer.

partial
-------

Do the above with ``functools.partial`` as well.

Extra credit
------------

This isn't really the point of the exercise, but see if you can make it dynamically accurate.

How accurate it is depends on how small the chunks are that you break the function up into.

See if you can think of a way to dynamically determine how small a step you should use.



















