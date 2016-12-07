.. _exercise_trapezoidal_rule:

*****************
Trapezoidal Rule
*****************

Passing functions around
=========================


.. rst-class:: medium left

    Goal:

.. rst-class:: left

    Making use of functions as objects -- functions that act on functions.


Trapezoidal rule
----------------

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
        '''a very simple straight horizontal line at y = 5'''
        return 5

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

    area = \frac{b-a}{2N}(f(x_0) + 2f(x_1) + 2f(x_2) + \dotsb + 2f(x_{N-1}) + f(x_N))

So you will need to:

 - create a list of x values from a to b (maybe 100 or so values to start)

 - compute the function for each of those values and double them

 - add them all up

 - multiply by the half of the difference between a and b divided by the number of steps.

.. nextslide::

Note that the first and last values are not doubled, so it may be more efficient to rearrange it like this:

.. math::

  area = \frac{b-a}{N} \left( \frac{f(x_0) + f(x_{N})}{2} + \sum_{i=1}^{N-1} f(x_i) \right)

Can you use comprehensions for this?

NOTE: ``range()`` only works for integers -- how can you deal with that?

.. nextslide::

Once you have that, it should work for any function that can be evaluated between a and b.

Try it for some built-in math functions, like ``math.sin``

tests
-----

Do this using test-drive development.

A few examples of analytical solutions you can use for tests:

A simple horizontal line -- see above.

.. nextslide::

A sloped straight line:

.. math::

  \int_a^b  y = mx + B = \frac{1}{2} m (b^2-a^2) + B (b-a)

The quadratic:

.. math::

  \int_a^b  y = Ax^2 + Bx + C = \frac{A}{3} (b^3-a^3) + \frac{B}{2} (b^2-a^2) + C (b-a)


The sine function:

.. math::

  \int_a^b \sin(x) = \cos(a) - \cos(b)

Computational Accuracy
----------------------

In the case of the linear functions, the result should theoretically be exact. But with the vagaries of floating point math may not be.

And for non-linear functions, the result will certainly not be exact.

So you want to check if the answer is *close* to what you expect.

In py3.5 -- there is an ``isclose()`` function (PEP485)

https://www.python.org/dev/peps/pep-0485/

In earlier pythons -- you'll need your own. There is one in:

``Examples/Session09/test_trapz.py``



Stage two:
----------

Some functions need extra parameters to do their thing. But the above will only handle a single parameter. For example, a quadratic function:

.. math::

    y = A x^2 + Bx + C

Requires values for A, B, and C in order to compute y from an given x.

You could write a specialized version of this function for each A, B, and C:

.. code-block:: python

  def quad1(x):
      return 3 * x**2 + 2*x + 4

But then you need to write a new function for any value of these parameters you might need.

.. nextslide::

Instead, you can pass in A, B and C each time:

.. code-block:: python

    def quadratic(x, A=0, B=0, C=0):
        return A * x**2 + B * x + C

Nice and general purpose.

But how would we compute the area under this function?

The function we wrote above only passes x in to the function it is integrating.

Passing arguments through:
--------------------------

Update your trapz() function so that you can give it a function that takes arbitrary extra arguments, either positional or keyword, after the x.

So you can do:

.. code-block:: python

    trapz(quadratic, 2, 20, A=1, B=3, C=2)

or

.. code-block:: python

    trapz(quadratic, 2, 20, 1, 3, C=2)

or

.. code-block:: python

    coef = {'A':1, 'B':3, 'C': 2}
    trapz(quadratic, 2, 20, **coef)

.. nextslide::

**NOTE:** Make sure this will work with ANY function, with **ANY** additional positional or keyword arguments -- not just this particular function.

This is pretty conceptually challenging -- but it's very little code!

If you are totally lost -- look at the lecture notes from previous classes -- how can you both accept and pass arbitrary arguments to/from a function?

.. nextslide::

You want your trapz function to take ANY function that can take ANY arbitrary extra arguments -- not just the quadratic function, and not just ``A,B, and C``. So good to test with another example.

The generalized sine function is:

.. math::

  A \sin(\omega t)

where :math:`A` is the amplitude, and :math:`\omega` is the frequency of the function. In this case, the area under the curve from a to b is:

.. math::

  \frac{A}{\omega} \left( \cos(\omega a) - \cos(\omega b) \right)

The test code has a test for this one, too.

Currying
--------

Another way to solve the above problem is to use the original ``trapz``, and create a custom version of the quadratic() function instead.

Write a function that takes ``A, B, and C`` as arguments, and returns a function that evaluates the quadratic for those particular coefficients.

Try passing the results of this into your ``trapz()`` and see if you get the same answer.

partial
-------

Do the above with ``functools.partial`` as well.

Extra credit
------------

This isn't really the point of the exercise, but see if you can make it dynamically accurate.

How accurate it is depends on how small the chunks are that you break the function up into.

See if you can think of a way to dynamically determine how small a step you should use.

This is one for the math and computational programming geeks!



















