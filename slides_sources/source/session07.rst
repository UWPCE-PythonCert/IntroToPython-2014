
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

***************************
Object Oriented Programming
***************************

.. rst-class:: medium centered

.. container::

  Multiple Inheritance

  Properties

  Class methods and  static methods

  Special (Magic) Methods

================
Review/Questions
================

Review of Previous Class
------------------------

* Object Oriented Programming:

  - classes

  - instances

  - attributes and methods

  - subclassing

  - overriding methods

Homework review
---------------

Homework Questions?

Did you all get a trapedzoidal rule function working?

Do you have a feel for classes, subclassing, overriding methods, ...?

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


Lightning Talks Today:
-----------------------

.. rst-class:: medium

 Eric Vegors

 Ian Cote

 Masako Tebbetts

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

LAB
----

Let's say you need to render some html...

The goal is to build a set of classes that render an html
page like this:

``Examples/Session06/sample_html.html``

We'll start with a single class, then add some sub-classes
to specialize the behavior

Details in:

:ref:`exercise_html_renderer`


Let's see if you can do step 1. in class...


Lightning Talks
----------------

.. rst-class:: medium

|
| Gideon Sylvan
|
| Hui Zhang
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
    >>> print(nc.color)
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

"""

Whenever you override a method, the
interface of the new method should be the same as the old.  It should take
the same parameters, return the same type, and obey the same preconditions
and postconditions.

If you obey this rule, you will find that any function
designed to work with an instance of a superclass, like a Deck, will also work
with instances of subclasses like a Hand or PokerHand.  If you violate this
rule, your code will collapse like (sorry) a house of cards.

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

``an_instance.something``

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


========
Homework
========

.. rst-class:: left medium

    * finish the lambda:keyword magic lab

    * functional files

    * html renderer


Functional files
-----------------

Write a program that takes a filename and "cleans" the file be removing
all the leading and trailing whitespace from each line.

Read in the original file and write out a new one, either creating a new
file or overwriting the existing one.

Give your user the option of which to perform.

Use ``map()`` to do the work.

Write a second version using a comprehension.

.. nextslide:: Hint

``sys.argv`` hold the command line arguments the user typed in. If the
user types:

.. code-block:: bash

  $ python the_script a_file_name

Then:

.. code-block:: python

    import sys
    filename = sys.argv[1]

will get ``filename == "a_file_name"``


Html rendering system:
-----------------------

:ref:`exercise_html_renderer`

|

You will build an html generator, using:

* A Base Class with a couple methods
* Subclasses overriding class attributes
* Subclasses overriding a method
* Subclasses overriding the ``__init__``

These are the core OO approaches


===================
More on Subclassing
===================

.. rst-class:: left

    I pointed you to this Video last class:

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


.. nextslide:: New-Style Classes

All the class definitions we've been showing inherit from ``object``.

This is referred to as a "new style" class.

They were introduced in python2.2 to better merge types and classes, and clean
up a few things.

There are differences in method resolution order and properties.

**Always Make New-Style Classes**

(that is, always subclass from object...)

The differences are subtle, and may not appear until they jump up to bite you.


.. nextslide:: ``super()``

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
            super(A, self).__init__(*argw, **kwargs)
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

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/}

(Both worth reading....)

==========
Properties
==========

.. rst-class:: left
.. container::

    One of the strengths of Python is lack of clutter.

    Attributes are simple and concise:

    .. code-block:: ipython

        In [5]: class C(object):
                def __init__(self):
                        self.x = 5
        In [6]: c = C()
        In [7]: c.x
        Out[7]: 5
        In [8]: c.x = 8
        In [9]: c.x
        Out[9]: 8


Getter and Setters?
-------------------

But what if you need to add behavior later?

.. rst-class:: build

* do some calculation
* check data validity
* keep things in sync


.. nextslide::

.. code-block:: ipython

    In [5]: class C(object):
       ...:     def __init__(self):
       ...:         self.x = 5
       ...:     def get_x(self):
       ...:         return self.x
       ...:     def set_x(self, x):
       ...:         self.x = x
       ...:
    In [6]: c = C()
    In [7]: c.get_x()
    Out[7]: 5
    In [8]: c.set_x(8)
    In [9]: c.get_x()
    Out[9]: 8


<shudder> This is ugly and verbose -- `Java`_?

.. _Java: http://dirtsimple.org/2004/12/python-is-not-java.html

properties
-----------

.. code-block:: ipython

    class C(object):
        _x = None
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value

    In [28]: c = C()
    In [30]: c.x = 5
    In [31]: print(c.x)
    5

Now the interface is like simple attribute access!

.. nextslide::

What's up with the "@" symbols?

Those are "decorations" it's a syntax for wrapping functions up with something special.

We'll cover that in detail in a couple weeks, but for now -- just copy the syntax.

.. code-block:: python

    @property
    def x(self):

means: make a property called x with this as the "getter".

.. code-block:: python

    @x.setter
    def x(self, value):

means: make the "setter" of the 'x' property this new function

.. nextslide:: "Read Only" Attributes

You do not need to define a setter. If you don't, you get a "read only" attribute:

.. code-block:: ipython

    In [11]: class D(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     @property
       ....:     def getx(self):
       ....:     """I am read only"""
       ....:         return self._x
       ....:
    In [12]: d = D()
    In [13]: d.x
    Out[13]: 5
    In [14]: d.x = 6
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-14-c83386d97be3> in <module>()
    ----> 1 d.x = 6
    AttributeError: can't set attribute

deleters
---------

If you want to do something special when a property is deleted, you can define
a deleter is well:

.. code-block:: ipython

    In [11]: class D(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.deleter
       ....:     def x(self):
       ....:         del self._x

If you leave this out, the property can't be deleted, which is usually
what you want.

.. rst-class:: centered

[demo: :download:`properties_example.py <../../Examples/Session07/properties_example.py>`]


LAB
----

Let's use some of this to build a nice class to represent a Circle.

For now, Let's do steps 1-4 of:

:ref:`exercise_circle_class`

Lightning Talks
----------------

.. rst-class:: medium

|
| Andrew P Klock
|
| Vinay Gupta
|


========================
Static and Class Methods
========================

.. rst-class:: left build
.. container::

    You've seen how methods of a class are *bound* to an instance when it is
    created.

    And you've seen how the argument ``self`` is then automatically passed to
    the method when it is called.

    And you've seen how you can call *unbound* methods on a class object so
    long as you pass an instance of that class as the first argument.

    .. rst-class:: centered

    **But what if you don't want or need an instance?**


Static Methods
--------------

A *static method* is a method that doesn't get self:

.. code-block:: ipython

    In [36]: class StaticAdder(object):

       ....:     @staticmethod
       ....:     def add(a, b):
       ....:         return a + b
       ....:

    In [37]: StaticAdder.add(3, 6)
    Out[37]: 9

.. rst-class:: centered

[demo: :download:`static_method.py <../../Examples/Session07/static_method.py>`]


.. nextslide:: Why?

.. rst-class:: build
.. container::

    Where are static methods useful?

    Usually they aren't

    99% of the time, it's better just to write a module-level function

    An example from the Standard Library (tarfile.py):

    .. code-block:: python

        class TarInfo(object):
            # ...
            @staticmethod
            def _create_payload(payload):
                """Return the string payload filled with zero bytes
                   up to the next 512 byte border.
                """
                blocks, remainder = divmod(len(payload), BLOCKSIZE)
                if remainder > 0:
                    payload += (BLOCKSIZE - remainder) * NUL
                return payload


Class Methods
-------------

A class method gets the class object, rather than an instance, as the first
argument

.. code-block:: ipython

    In [41]: class Classy(object):
       ....:     x = 2
       ....:     @classmethod
       ....:     def a_class_method(cls, y):
       ....:         print("in a class method: ", cls)
       ....:         return y ** cls.x
       ....:
    In [42]: Classy.a_class_method(4)
    in a class method:  <class '__main__.Classy'>
    Out[42]: 16

.. rst-class:: centered

[demo: :download:`class_method.py <../../Examples/Session07/class_method.py>`]


.. nextslide:: Why?

.. rst-class:: build
.. container::

    Unlike static methods, class methods are quite common.

    They have the advantage of being friendly to subclassing.

    Consider this:

    .. code-block:: ipython

        In [44]: class SubClassy(Classy):
           ....:     x = 3
           ....:

        In [45]: SubClassy.a_class_method(4)
        in a class method:  <class '__main__.SubClassy'>
        Out[45]: 64

.. nextslide:: Alternate Constructors

Because of this friendliness to subclassing, class methods are often used to
build alternate constructors.

Consider the case of wanting to build a dictionary with a given iterable of
keys:

.. code-block:: ipython

    In [57]: d = dict([1,2,3])
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-57-50c56a77d95f> in <module>()
    ----> 1 d = dict([1,2,3])

    TypeError: cannot convert dictionary update sequence element #0 to a sequence


.. nextslide:: ``dict.fromkeys()``

The stock constructor for a dictionary won't work this way. So the dict object
implements an alternate constructor that *can*.

.. code-block:: python

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.
        '''
        self = cls()
        for key in iterable:
            self[key] = value
        return self

(this is actually from the OrderedDict implementation in ``collections.py``)

See also datetime.datetime.now(), etc....

.. nextslide:: Curious?

Properties, Static Methods and Class Methods are powerful features of Pythons
OO model.

They are implemented using an underlying structure called *descriptors*

`Here is a low level look`_ at how the descriptor protocol works.

The cool part is that this mechanism is available to you, the programmer, as
well.

.. _Here is a low level look: https://docs.python.org/2/howto/descriptor.html


Extra Credit: use a class method to make an alternate constructor that takes
the diameter instead.

===============
Special Methods
===============

.. rst-class:: left
.. container::

    Special methods (also called *magic* methods) are the secret sauce to Python's
    Duck typing.

    Defining the appropriate special methods in your classes is how you make your
    class act like standard classes.

What's in a Name?
-----------------

We've seen at least one special method so far::

    __init__

It's all in the double underscores...

Pronounced "dunder" (or "under-under")

try: ``dir(2)``  or ``dir(list)``

.. nextslide:: Generally Useful Special Methods

Most classes should at lest have these special methods:

``object.__str__``:
  Called by the str() built-in function and by the print function to compute
  the *informal* string representation of an object.

``object.__unicode__``:
  Called by the unicode() built-in function.  This converts an object to an
  *informal* unicode representation.

  (more on Unicode later....)

``object.__repr__``:
  Called by the repr() built-in function and by string conversions (reverse
  quotes) to compute the *official* string representation of an object.

  (ideally: ``eval( repr(something) ) == something``)


Protocols
----------

.. rst-class:: build
.. container::

    The set of special methods needed to emulate a particular type of Python object
    is called a *protocol*.

    Your classes can "become" like Python built-in classes by implementing the
    methods in a given protocol.

    Remember, these are more *guidelines* than laws.  Implement what you need.


.. nextslide:: The Numerics Protocol

Do you want your class to behave like a number? Implement these methods:

.. code-block:: python

    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)

.. nextslide:: The Container Protocol

Want to make a container type? Here's what you need:

.. code-block:: python

    object.__len__(self)
    object.__getitem__(self, key)
    object.__setitem__(self, key, value)
    object.__delitem__(self, key)
    object.__iter__(self)
    object.__reversed__(self)
    object.__contains__(self, item)
    object.__getslice__(self, i, j)
    object.__setslice__(self, i, j, sequence)
    object.__delslice__(self, i, j)


.. nextslide:: An Example

Each of these methods supports a common Python operation.

For example, to make '+' work with a sequence type in a vector-like fashion,
implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])

.. rst-class:: centered

[a more complete example may be seen :download:`here <./supplements/vector.py>`]



.. nextslide:: Summary

Use special methods when you want your class to act like a "standard" class in
some way.

Look up the special methods you need and define them.

There's more to read about the details of implementing these methods:

* https://docs.python.org/2/reference/datamodel.html#special-method-names
* http://www.rafekettler.com/magicmethods.html


Lightning Talks
----------------

.. rst-class:: medium

|
| Ousmane Conde
|
| Salim Hassan Hamed
|

LAB
----

Let's complete our nifty Circle class:

Steps 5-8 of:

:ref:`exercise_circle_class`


========
Homework
========

Complete the Circle class

Decide what you are going to do for your proejct, and send me a simple proposal.


