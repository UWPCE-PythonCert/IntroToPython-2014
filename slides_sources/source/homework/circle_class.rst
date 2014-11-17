.. _homework_circle_class:

==================================
Circle Class Homework Assignment
==================================

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

This exercise should use "new style classes" i.e. inherit from ``object``

You will also use:

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

NOTE: ``pi`` can be found in the math module

The user should not be able to set the area:

.. code-block:: python

    >> c = Circle(2)
    >> c.area = 42
    AttributeError

Step 5:
-------

more to come...


