
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

******************************************************************************************
Session Six: Object oriented programming: Classes, instances, attributes, and subclassing
******************************************************************************************


================
Review/Questions
================

Review of Previous Class
------------------------

* Argument Passing: ``*args``, ``**kwargs``

* comprehensions

* ``lambda``


Homework review
---------------

Homework Questions?

If it seems harder than it should be -- it is!

My Solution to the trigram:

 * (``dict.setdefault()``  trick...)

``global`` keyword?

Unicode Notes
-------------

To put unicode in your source file, put:

.. code-block:: python

  #!/usr/bin/env python
  # -*- coding: utf-8 -*-

at the top of your file ... and be sure to save it as utf-8!
(file->save with encoding in Sublime)

You also might want to put::

    from __future__ import unicode_literals


Additional notes on using Unicode in Python see:

 :ref:`unicode_supplement`


===========================
Object Oriented Programming
===========================

Object Oriented Programming
---------------------------

More about Python implementation than OO design/strengths/weaknesses

One reason for this:

Folks can't even agree on what OO "really" means

See: The Quarks of Object-Oriented Development

  - Deborah J. Armstrong

http://agp.hx0.ru/oop/quarks.pdf


.. nextslide::

Is Python a "True" Object-Oriented Language?

(Doesn't support full encapsulation, doesn't *require*
classes,  etc...)

.. nextslide::

.. rst-class:: center large

    I don't Care!


Good software design is about code re-use, clean separation of concerns,
refactorability, testability, etc...

OO can help with all that, but:
  * It doesn't guarantee it
  * It can get in the way

.. nextslide::

Python is a Dynamic Language

That clashes with "pure" OO

Think in terms of what makes sense for your project
 -- not any one paradigm of software design.


.. nextslide::

So what is "object oriented programming"?

    "Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use"


http://en.wikipedia.org/wiki/Object-oriented_programming

.. nextslide::

Even simpler:


"Objects are data and the functions that act on them in one place."

This is the core of "encapsulation"

In Python: just another namespace.

.. nextslide::

The OO buzzwords:

  * data abstraction
  * encapsulation
  * modularity
  * polymorphism
  * inheritance

Python does all of this, though it doesn't enforce it.

.. nextslide::

You can do OO in C

(see the GTK+ project)


"OO languages" give you some handy tools to make it easier (and safer):

  * polymorphism (duck typing gives you this anyway)
  * inheritance


.. nextslide::

OO is the dominant model for the past couple decades

You will need to use it:

- It's a good idea for a lot of problems

- You'll need to work with OO packages

(Even a fair bit of the standard library is Object Oriented)


.. nextslide:: Some definitions

class
  A category of objects: particular data and behavior: A "circle" (same as a type in python)

instance
  A particular object of a class: a specific circle

object
  The general case of a instance -- really any value (in Python anyway)

attribute
  Something that belongs to an object (or class): generally thought of
  as a variable, or single object, as opposed to a ...

method
  A function that belongs to a class

.. nextslide::

.. rst-class:: center

    Note that in python, functions are first class objects, so a method *is* an attribute


==============
Python Classes
==============

Python Classes
--------------

The ``class``  statement

``class``  creates a new type object:

.. code-block:: ipython

    In [4]: class C(object):
        pass
       ...:
    In [5]: type(C)
    Out[5]: type

A class is a type -- interesting!

It is created when the statement is run -- much like ``def``

You don't *have* to subclass from ``object``, but you *should* 

(note on "new style" classes)

.. nextslide::

About the simplest class you can write

.. code-block:: python

    >>> class Point(object):
    ...     x = 1
    ...     y = 2
    >>> Point
    <class __main__.Point at 0x2bf928>
    >>> Point.x
    1
    >>> p = Point()
    >>> p
    <__main__.Point instance at 0x2de918>
    >>> p.x
    1

.. nextslide::

Basic Structure of a real class:

.. code-block:: python

    class Point(object):
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print "p.x is:", p.x
    print "p.y is:", p.y


see: ``Examples/Session06/simple_class``

.. nextslide::

The Initializer

The ``__init__``  special method is called when a new instance of a class is created.

You can use it to do any set-up you need

.. code-block:: python

    class Point(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y


It gets the arguments passed when you call the class object:

.. code-block:: python  

    Point(x, y)

.. nextslide::


What is this ``self`` thing?

The instance of the class is passed as the first parameter for every method.

"``self``" is only a convention -- but you DO want to use it.

.. code-block:: python

    class Point(object):
        def a_function(self, x, y):
    ...


Does this look familiar from C-style procedural programming?


.. nextslide::

Anything assigned to a ``self.``  attribute is kept in the instance
name space -- ``self`` *is* the instance.

That's where all the instance-specific data is.

.. code-block:: python

    class Point(object):
        size = 4
        color= "red"
        def __init__(self, x, y):
            self.x = x
            self.y = y

.. nextslide::

Anything assigned in the class scope is a class attribute -- every
instance of the class shares the same one.

Note: the methods defined by ``def`` are class attributes as well.

The class is one namespace, the instance is another.


.. code-block:: python  

    class Point(object):
        size = 4
        color= "red"
    ...
        def get_color():
            return self.color
    >>> p3.get_color()
     'red'


class attributes are accessed with ``self``  also.


.. nextslide::

Typical methods:

.. code-block:: python  

    class Circle(object):
        color = "red"

        def __init__(self, diameter):
            self.diameter = diameter

        def grow(self, factor=2):
            self.diameter = self.diameter * factor


Methods take some parameters, manipulate the attributes in ``self``.

They may or may not return something useful.

.. nextslide::

Gotcha!

.. code-block:: python  

    ...
        def grow(self, factor=2):
            self.diameter = self.diameter * factor
    ...
    In [205]: C = Circle(5)
    In [206]: C.grow(2,3)

    TypeError: grow() takes at most 2 arguments (3 given)

Huh???? I only gave 2

``self`` is implicitly passed in for you by python.

(demo of bound vs. unbound methods)

LAB / homework
---------------

Let's say you need to render some html..

The goal is to build a set of classes that render an html page.

``Examples/Session06/sample_html.html``

We'll start with a single class, then add some sub-classes to specialize the behavior

Details in:

:ref:`homework_html_renderer`


Let's see if we can do step 1. in class...


=======================
Subclassing/Inheritance
=======================

Inheritance
-----------

In object-oriented programming (OOP), inheritance is a way to reuse code of existing objects, or to establish a subtype from an existing object.


Objects are defined by classes, classes can inherit attributes and behavior from pre-existing classes called base classes or super classes.

The resulting classes are known as derived classes or subclasses.

(http://en.wikipedia.org/wiki/Inheritance_%28object-oriented_programming%29)

Subclassing
-----------

A subclass "inherits" all the attributes (methods, etc) of the parent class.

You can then change ("override") some or all of the attributes to change the behavior.

You can also add new attributes to extend the behavior.

The simplest subclass in Python:

.. code-block:: python

    class A_subclass(The_superclass):
        pass

``A_subclass``  now has exactly the same behavior as ``The_superclass``

NOTE: when we put ``object`` in there, it means we are deriving from object -- getting core functionality of all objects.

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle(object):
        color = "red"

    ...

    class NewCircle(Circle):
        color = "blue"
    >>> nc = NewCircle
    >>> print nc.color
    blue


all the ``self``  instances will have the new attribute.

Overriding methods
------------------

Same thing, but with methods (remember, a method *is* an attribute in python)

.. code-block:: python

    class Circle(object):
    ...
        def grow(self, factor=2):
            """grows the circle's diameter by factor"""
            self.diameter = self.diameter * factor
    ...

    class NewCircle(Circle):
    ...
        def grow(self, factor=2):
            """grows the area by factor..."""
            self.diameter = self.diameter * math.sqrt(2)


all the instances will have the new method

.. nextslide::

Here's a program design suggestion:
  whenever you override a method, the
  interface of the new method should be the same as the old.  It should take
  the same parameters, return the same type, and obey the same preconditions
  and postconditions.

  If you obey this rule, you will find that any function
  designed to work with an instance of a superclass, like a Deck, will also work
  with instances of subclasses like a Hand or PokerHand.  If you violate this
  rule, your code will collapse like (sorry) a house of cards.

[ThinkPython 18.10]


( Demo of class vs. instance attributes )

===================
More on Subclassing
===================

Overriding \_\_init\_\_
-----------------------

``__init__`` common method to override}

You often need to call the super class ``__init__``  as well

.. code-block:: python

    class Circle(object):
        color = "red"
        def __init__(self, diameter):
            self.diameter = diameter
    ...
    class CircleR(Circle):
        def __init__(self, radius):
            diameter = radius*2
            Circle.__init__(self, diameter)



exception to: "don't change the method signature" rule.

More subclassing
----------------
You can also call the superclass' other methods:

.. code-block:: python  

    class Circle(object):
    ...
        def get_area(self, diameter):
            return math.pi * (diameter/2.0)**2


    class CircleR2(Circle):
    ...
        def get_area(self):
            return Circle.get_area(self, self.radius*2)

There is nothing special about ``__init__``  except that it gets called
automatically when you instantiate an instance.


When to Subclass
----------------

"Is a" relationship: Subclass/inheritance

"Has a" relationship: Composition

.. nextslide::

"Is a" vs "Has a"

You may have a class that needs to accumulate an arbitrary number of objects.

A list can do that -- so should you subclass list?

Ask yourself:

-- **Is** your class a list (with some extra functionality)?

or

-- Does you class **have** a list?

You only want to subclass list if your class could be used anywhere a list can be used.


Attribute resolution order
--------------------------

When you access an attribute:

``An_Instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...


It can get more complicated...

http://www.python.org/getit/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html


What are Python classes, really?
--------------------------------

Putting aside the OO theory...

Python classes are:

  * Namespaces

    * One for the class object
    * One for each instance

  * Attribute resolution order
  * Auto tacking-on of ``self`` when methods are called


That's about it -- really!


Type-Based dispatch
-------------------

You'll see code that looks like this:

.. code-block:: python

      if isinstance(other, A_Class):
          Do_something_with_other
      else:
          Do_something_else


Usually better to use "duck typing" (polymorphism)

But when it's called for:

    * ``isinstance()``
    * ``issubclass()``

.. nextslide::

GvR: "Five Minute Multi- methods in Python":

http://www.artima.com/weblogs/viewpost.jsp?thread=101605

http://www.python.org/getit/releases/2.3/mro/

http://python-history.blogspot.com/2010/06/method-resolution-order.html


Wrap Up
-------

Thinking OO in Python:

Think about what makes sense for your code:

* Code re-use
* Clean APIs
* ...

Don't be a slave to what OO is *supposed* to look like.

Let OO work for you, not *create* work for you

.. nextslide::

OO in Python:

The Art of Subclassing: *Raymond Hettinger*

http://pyvideo.org/video/879/the-art-of-subclassing

"classes are for code re-use -- not creating taxonomies"

Stop Writing Classes: *Jack Diederich*

http://pyvideo.org/video/880/stop-writing-classes

"If your class has only two methods -- and one of them is ``__init__``
-- you don't need a class"


Homework
--------

Build an html rendering system:

:ref:`homework_html_renderer`

|

You will build an html generator, using:

* A Base Class with a couple methods
* Subclasses overriding class attributes
* Subclasses overriding a method
* Subclasses overriding the ``__init__``

These are the core OO approaches

