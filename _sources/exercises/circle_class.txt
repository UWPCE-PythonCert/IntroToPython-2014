.. _exercise_circle_class:

======================
Circle Class Excercise
======================

Circle Class
============

Goal:
------

The goal is to create a class that represents a simple circle.

A Circle can be defined by either specifying the radius or the diameter,
and the user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

 * Compute the circle's area
 * Print the circle and get something nice
 * Be able to add two circles together
 * Be able to compare two circles to see which is bigger
 * Be able to compare to see if there are equal
 * (follows from above) be able to put them in a list and sort them

.. nextslide::

You will use:

  - properties
  - a classmethod
  - a define a bunch of "special methods"


General Instructions:
---------------------

1. For each step, write a couple of unit tests that test the new features.

2. Run these tests (and they will fail the first time)

3. Add the code required for your tests to pass.


Step 1:
-------

create class called ``Circle`` -- it's signature should look like::

  c = Circle(the_radius)

The radius is a required parameter (can't have a circle without one!)

the resulting circle should have a attribute for the radius::

  c.radius

So you can do:

.. code-block:: python

    >> c = Circle(4)
    >> print c.radius
    4

Remember: tests first!

Step 2:
-------

Add a "diameter" property, so the user can get the diameter of the circle:

.. code-block:: python

    >> c = Circle(4)
    >> print c.diameter
    8

Step 3:
-------

Set up the diameter property so that the user can set the diameter of the circle:

.. code-block:: python

    >> c = Circle(4)
    >> c.diameter = 2
    >> print c.diameter
    2
    >> print c.radius
    1

**NOTE** that the radius has changed!

Step 4:
--------

Add an ``area`` property so the user can get the area of the circle:

.. code-block:: python

    >> c = Circle(2)
    >> print c.area
    12.566370

(``pi`` can be found in the math module)

The user should not be able to set the area:

.. code-block:: python

    >> c = Circle(2)
    >> c.area = 42
    AttributeError

Step 5:
-------

Add an "alternate constructor" that lets the user create a Circle directly
with the diameter:

.. code-block:: python

    >> c = Circle.from_diameter(8)
    >> print c.diameter
    8
    >> print c.radius
    4

Step 6:
-------

Add __str__ and __repr__ methods to your Circle class.

Now you can print it:

.. code-block:: ipython

    In [2]: c = Circle(4)

    In [3]: print c
    Circle with radius: 4.000000

    In [4]: repr(c)
    Out[4]: 'Circle(4)'

    In [5]: d = eval(repr(c))

    In [6]: d
    Out[6]: Circle(4)

Step 7:
--------

Add some of the numeric protocol to your Circle:

You should be able to add two circles:

.. code-block:: ipython

    In [7]: c1 = Circle(2)

    In [8]: c2 = Circle(4)

    In [9]: c1 + c2
    Out[9]: Circle(6)

and multiply one times a number:

.. code-block:: ipython

    In [16]: c2 * 3
    Out[16]: Circle(12)

(what happens with ``3 * c2`` ? -- can you fix that?)

.. nextslide::

Step 8:
--------
add the ability to compare two circles:

.. code-block:: ipython

    In [10]: c1 > c2
    Out[10]: False

    In [11]: c1 < c2
    Out[11]: True

    In [12]: c1 == c2
    Out[12]: False

    In [13]: c3 = Circle(4)

    In [14]: c2 == c3
    Out[14]: True

.. nextslide::

Once the comparing is done,  you should be able to sort a list of circles:

.. code-block:: ipython

    In [18]: print circles
    [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    In [19]: circl
    circle      circle.py   circle.pyc  circles

    In [19]: circles.sort()

    In [20]: print circles
    [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4), Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

**NOTE:** make sure to write unit tests for all of this! Ideally before writing the code.

Step 8: Optional Features:
--------------------------

* See if you can make "reflected" numerics do the right thing:

.. code-block:: python

    a_circle * 3 == 3 * a_circle

* What else makes sense: division?  others?

* Add the "augmented assignment" operators, where they make sense:

.. code-block:: python

  a_circle += another_circle

  a_circle *= 2

* look through all the "magic methods" and see what makes sense for circles


