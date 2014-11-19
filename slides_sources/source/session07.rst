
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

***********************
Session Seven: More OO
***********************

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

Have you all got an HTML Renderer working?

Do you have a feel for classes, subclassing, overriding methods, ...?

Personal Project
-----------------

The bulk of the homework for the rest of the class will be a personal project:

* It can be for fun, or something you need for your job.
* It should be large enought to take a few weeks homework time to do.
* It should demostrate that you can do something useful with python.
* It should follow PEP8 (https://www.python.org/dev/peps/pep-0008)
* It should have unit tests!
* Ideally, it will be in version control (gitHub)
* I'm not going to require an specific python features (i.e. classes): use
  what is appropriate for your project

* Due the Friday after the last class (December 12)

|
|  By next week, send me a project proposal: can be short and sweet.
|


Lightning Talks Today:
-----------------------

.. rst-class:: medium

  Andrew P Klock

  Vinay Gupta

  Ousmane Conde

  Salim Hassan Hamed


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
    In [31]: print c.x
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

:ref:`homework_circle_class`

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
       ....:         print "in a class method: ", cls
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
  Called by the str() built-in function and by the print statement to compute
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

:ref:`homework_circle_class`


========
Homework
========

Complete the Circle class

Decide what you are going to do for your proejct, and send me a simple proposal.


