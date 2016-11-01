.. include:: include.rst

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
    Out[25]: [14, 20, 24, 34, 22, 18]


But if it's a small function, and you only need it once:

.. code-block:: ipython

    In [26]: map(lambda x: x*2 + 10, l)
    Out[26]: [14, 20, 24, 34, 22, 18]


filter
------

``filter``  "filters" a sequence of objects with a boolean function --
It keeps only those for which the function is True -- filtering our the rest.

To get only the even numbers:

.. code-block:: ipython

    In [27]: l = [2, 5, 7, 12, 6, 4]
    In [28]: filter(lambda x: not x%2, l)
    Out[28]: [2, 12, 6, 4]

If you pass ``None`` to ``filter()``, you get only items that evaluate to true:

.. code-block:: ipython

    In [1]: l = [1, 0, 2.3, 0.0, 'text', '', [1,2], [], False, True, None ]

    In [2]: filter(None, l)
    Out[2]: [1, 2.3, 'text', [1, 2], True]


reduce
------

``reduce``  "reduces" a sequence of objects to a single object with a function that combines two arguments

To get the sum:

.. code-block:: ipython

    In [30]: l = [2, 5, 7, 12, 6, 4]
    In [31]: reduce(lambda x,y: x+y, l)
    Out[31]: 36


To get the product:

.. code-block:: ipython

    In [32]: reduce(lambda x,y: x*y, l)
    Out[32]: 20160

or

.. code-block:: ipython

    In [13]: import operator
    In [14]: reduce(operator.mul, l)
    Out[14]: 20160

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

(Except Reduce)

But Guido thinks almost all uses of reduce are really ``sum()``

Functional Programming
----------------------

Comprehensions and map, filter, reduce are all "functional programming" approaches}

``map, filter``  and ``reduce``  pre-date comprehensions in Python's history

Some people like that syntax better

And "map-reduce" is a big concept these days for parallel processing of "Big Data" in NoSQL databases.

(Hadoop, MongoDB, etc.)


A bit more about lambda
------------------------

It is very useful for specifying sorting as well:

.. code-block:: ipython

    In [55]: lst = [("Chris","Barker"), ("Fred", "Jones"), ("Zola", "Adams")]

    In [56]: lst.sort()

    In [57]: lst
    Out[57]: [('Chris', 'Barker'), ('Fred', 'Jones'), ('Zola', 'Adams')]

    In [58]: lst.sort(key=lambda x: x[1])

    In [59]: lst
    Out[59]: [('Zola', 'Adams'), ('Chris', 'Barker'), ('Fred', 'Jones')]

lambda in keyword arguments
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

Lightning Talk
--------------

.. rst-class:: medium

|
| Paul A Casey
|

==============
dict as switch
==============

What to use instead of "switch-case"?

switch-case
-----------

A number of languages have a "switch-case" construct::

    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };

How do you spell this in python?

``if-elif`` chains
-------------------

The obvious way to spell it is a chain of ``elif`` statements:

.. code-block:: python

    if argument ==  0:
        return "zero"
    elif argument == 1:
        return "one"
    elif argument == 2:
        return "two"
    else:
        return "nothing"

And there is nothing wrong with that, but....

.. nextslide::

The ``elif`` chain is neither elegant nor efficient. There are a number of ways to spell it in python -- but one elgant one is to use a dict:

.. code-block:: python

    arg_dict = {0:"zero", 1:"one", 2: "two"}
        dict.get(argument, "nothing")

Simple, elegant, and fast.

You can do a dispatch table by putting functions as the value.

Example: Chris' mailroom2 solution.

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

===
LAB
===

Let's use some of this ability to use functions a objects for something useful:

:ref:`exercise_trapezoidal_rule`

Some reading on these topics:

http://www.pydanny.com/python-partials-are-fun.html

https://pymotw.com/2/functools/

http://www.programiz.com/python-programming/closure

https://www.clear.rice.edu/comp130/12spring/curry/



***************************
Object Oriented Programming
***************************

.. rst-class:: medium centered

.. container::

  Classes

  Instances

  Class and instance attributes

  Subclassing

  Overriding methods


================
Review/Questions
================

Review of Previous Class
------------------------

.. rst-class:: medium
  Advanced Argument passing

  Lambda

  Functions as Objects

Homework review
---------------

Homework Questions?

Did you all get a trapedzoidal rule function working?

Anyone get the "passing through of arguments"?

How about the adaptive solutions?


Notes on Floating point
-----------------------

Did anyone look at the isclose() function?

How to make a range of numbers in floating point?

Anyone do something like this?:

.. code-block:: python

  s = []
  x = a
  while x <= b:
      s.append(x)
      x += delta_x

  -- see my solution.

Some notes about FP issues:

https://docs.python.org/3.5/tutorial/floatingpoint.html

Code Review
-----------

Anyone unsatisfied with their solution -- or stuck?

Let's do a code review!


Lightning Talks Today:
-----------------------

.. rst-class:: medium

Charles E Robison

Paul S Briant

Paul Vosper


===========================
Object Oriented Programming
===========================

A Core approach to organizing code.

I'm going to go through this fast.

So we can get to the actual coding.


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

|
    "Objects can be thought of as wrapping their data
    within a set of functions designed to ensure that
    the data are used appropriately, and to assist in
    that use"

|

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

.. rst-class:: left

    The ``class``  statement

    ``class``  creates a new type object:

    .. code-block:: ipython

        In [4]: class C:
            pass
           ...:
        In [5]: type(C)
        Out[5]: type

    A class is a type -- interesting!

    It is created when the statement is run -- much like ``def``

Python Classes
--------------

About the simplest class you can write

.. code-block:: python

    >>> class Point:
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

    class Point:
    # everything defined in here is in the class namespace

        def __init__(self, x, y):
            self.x = x
            self.y = y

    ## create an instance of the class
    p = Point(3,4)

    ## access the attributes
    print("p.x is:", p.x)
    print("p.y is:", p.y)


see: ``Examples/Session07/simple_classes.py``

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

    class Point:
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

    class Point:
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

    class Circle:
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

LAB
----

Let's say you need to render some html...

The goal is to build a set of classes that render an html
page.

We'll start with a single class, then add some sub-classes
to specialize the behavior

Details in:

:ref:`exercise_html_renderer`

Let's get a start with step 1. in class.

I'll give you a few minutes to think about it -- then we'll get started as a group.


Lightning Talks
----------------

.. rst-class:: medium

|
| Charles E Robison
|
| Paul S Briant
|
| Paul Vosper
|

=======================
Subclassing/Inheritance
=======================

Inheritance
-----------

In object-oriented programming (OOP), inheritance is a way to reuse code
of existing objects, or to establish a subtype from an existing object.

Objects are defined by classes, classes can inherit attributes and behavior
from pre-existing classes called base classes or super classes.

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

Overriding attributes
---------------------

Overriding is as simple as creating a new attribute with the same name:

.. code-block:: python

    class Circle:
        color = "red"

    ...

    class NewCircle(Circle):
        color = "blue"
    >>> nc = NewCircle
    >>> print(nc.color)
    blue


all the ``self``  instances will have the new attribute.

Overriding methods
------------------

Same thing, but with methods (remember, a method *is* an attribute in python)

.. code-block:: python

    class Circle:
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

"""

Whenever you override a method, the interface of the new method should be the same as the old.  It should takethe same parameters, return the same type, and obey the same preconditions and postconditions.

If you obey this rule, you will find that any function designed to work with an instance of a superclass, like a Deck, will also work with instances of subclasses like a Hand or PokerHand.  If you violate this rule, your code will collapse like (sorry) a house of cards.

"""

|
| [ThinkPython 18.10]
|
| ( Demo of class vs. instance attributes )


===================
More on Subclassing
===================

Overriding \_\_init\_\_
-----------------------

``__init__`` common method to override

You often need to call the super class ``__init__``  as well

.. code-block:: python

    class Circle:
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

    class Circle:
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

``an_instance.something``

Python looks for it in this order:

  * Is it an instance attribute ?
  * Is it a class attribute ?
  * Is it a superclass attribute ?
  * Is it a super-superclass attribute ?
  * ...


It can get more complicated...

https://www.python.org/download/releases/2.3/mro/

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

https://www.python.org/download/releases/2.3/mro/

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


===
LAB
===

.. rst-class:: left medium

    * html renderer: let's see how much more we can do!

:ref:`exercise_html_renderer`


Now we have a base class, and we can:

* Subclass overriding class attributes
* Subclass overriding a method
* Subclass overriding the ``__init__``

These are the core OO approaches


===================
More on Subclassing
===================

.. rst-class:: left

    This is a great talk (yes, I'm repeating):

    The Art of Subclassing: *Raymond Hettinger*

    http://pyvideo.org/video/879/the-art-of-subclassing

    If you haven't watched it,  It's well worth your time

What's a Subclass For?
----------------------

The most salient points from that video are as follows:

* **Subclassing is not for Specialization**

* **Subclassing is for Reusing Code**

* **Bear in mind that the subclass is in charge**


Multiple Inheritance
--------------------

Multiple inheritance: Inheriting from more than one class

Simply provide more than one parent.

.. code-block:: python

    class Combined(Super1, Super2, Super3):
        def __init__(self, something, something else):
            # some custom initialization here.
            Super1.__init__(self, ......)
            Super2.__init__(self, ......)
            Super3.__init__(self, ......)
            # possibly more custom initialization

(calls to the super class ``__init__``  are optional -- case dependent)

.. nextslide:: Method Resolution Order

.. code-block:: python

    class Combined(Super1, Super2, Super3)

Attributes are located bottom-to-top, left-to-right

* Is it an instance attribute ?
* Is it a class attribute ?
* Is it a superclass attribute ?

  - Is  it an attribute of the left-most superclass?
  - Is  it an attribute of the next superclass?
  - and so on up the hierarchy...

* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

.. nextslide:: Mix-ins

So why would you want to do this? One reason:  *mixins*

Provides an subset of expected functionality in a re-usable package.

Huh? this is why --

Hierarchies are not always simple:

* Animal

  * Mammal

    * GiveBirth()

  * Bird

    * LayEggs()

Where do you put a Platypus?

Real World Example: `FloatCanvas`_

.. _FloatCanvas: https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L485


``super()``
-----------

``super()``: use it to call a superclass method, rather than explicitly calling
the unbound method on the superclass.

instead of:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            B.__init__(self, *argw, **kwargs)
            ...

You can do:

.. code-block:: python

    class A(B):
        def __init__(self, *args, **kwargs)
            super().__init__(*argw, **kwargs)
            ...

.. nextslide:: Caveats

Caution: There are some subtle differences with multiple inheritance.

You can use explicit calling to ensure that the 'right' method is called.

.. rst-class:: medium

    **Background**

Two seminal articles about ``super()``:

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/

(Both worth reading....)

========
Homework
========

Complete your html renderer.

Watch those videos:

Python class toolkit: *Raymond Hettinger* -- https://youtu.be/HTLu2DFOdTg

https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger

The Art of Subclassing: *Raymond Hettinger* -- http://pyvideo.org/video/879/the-art-of-subclassing

Stop Writing Classes: *Jack Diederich* -- http://pyvideo.org/video/880/stop-writing-classes

Read up on super()


