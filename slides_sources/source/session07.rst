
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.

*******************************
Session Seven: Testing, More OO
*******************************

.. rst-class:: large centered

| Testing,
| Multiple Inheritance,
| Properties,
| Class and Static Methods,
| Special (Magic) Methods


Review/Questions
================

Review of Previous Class
------------------------

* Unicode

* Object Oriented Programming


Homework review
---------------

Homework Questions?

How is progress going on the HTML Renderer?


Testing
=======

.. rst-class:: build left
.. container::

    You've already seen some a very basic testing strategy.

    You've written some tests using that strategy.

    These tests were pretty basic, and a bit awkward in places (testing error
    conditions in particular).

    .. rst-class:: centered

    **It gets better**

Test Runners
------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.

.. rst-class:: build

* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.

.. rst-class:: build
.. container::

    This is not optimal.

    Python provides testing systems to help.


.. nextslide:: Standard Library: ``unittest``

The original testing system in Python.

You write subclasses of the ``unittest.TestCase`` class:

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):
        def test_tautology(self):
            self.assertEquals(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Testing Your Code

This way, you can write your code in one file and test it from another:

.. code-block:: python

    # in my_mod.py
    def my_func(val1, val2):
        return val1 * val2

    # in test_my_mod.py
    import unittest
    from my_mod import my_func

    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = reduce(lambda x, y: x * y, test_vals)
            actual = my_func(*test_vals)
            self.assertEquals(expected, actual)

    if __name__ == '__main__':
        unittest.main()

.. nextslide:: Advantages of ``unittest``

.. rst-class:: build
.. container::

    The ``unittest`` module is great.

    It comes with the standard Python distribution, no installation required.

    It provides a wide variety of assertions for testing all sorts of situations.

    It allows for a setup and tear down workflow both before and after all tests
    and before and after each test.

    It's well known and well understood.

.. nextslide:: Disadvantages:

.. rst-class:: build
.. container::


    It's Object Oriented, and quite heavy.

    It uses the framework design pattern, so knowing how to use the features
    means learning what to override.

    Needing to override means you have to be cautious.

    Test discovery is both inflexible and brittle.

.. nextslide:: Other Options

There are several other options for running tests in Python.


* `Nose`_
* `pytest`_
* ... (many frameworks supply their own test runners)

We are going to play today with pytest

.. _Nose: https://nose.readthedocs.org/
.. _pytest: http://pytest.org/latest/


.. nextslide:: Installing ``pytest``

The first step is to install the package:

.. code-block:: bash

    $ workon cff2py
    (cff2py)$ pip install pytest

Once this is complete, you should have a ``py.test`` command you can run at the
command line:

.. code-block:: bash

    (cff2py)$ py.test

If you have any tests in your repository, that will find and run them.

.. rst-class:: build
.. container::

    **Do you?**

.. nextslide:: Pre-existing Tests

I've added two files to the ``code/session07`` folder, along with a python
source code file called ``circle.py``.

The results you should have seen when you ran ``py.test`` above come partly
from these files.

Let's take a few minutes to look these files over.

[demo]

.. nextslide:: What's Happening Here.

When you run the ``py.test`` command, ``pytest`` starts in your current working
directory and searches the filesystem for things that might be tests.

It follows some simple rules:

.. rst-class:: build

* Any python file that starts with ``test_`` or ``_test`` is imported.
* Any functions in them that start with ``test_`` are run as tests.
* Any classes that start with ``Test`` are treated similarly, with methods that
  begin with ``test_`` treated as tests.


.. nextslide::

This test running framework is simple, flexible and configurable.

`Read the documentation`_ for more information.

.. _Read the documentation: http://pytest.org/latest/getting-started.html#getstarted

.. nextslide:: Test Driven Development

What we've just done here is the first step in what is called **Test Driven
Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red we see in the terminal when we run our tests is a goad to us to write
the code that fixes these tests.

Let's do that next!


More on Subclassing
===================

Watch This Video:

http://pyvideo.org/video/879/the-art-of-subclassing

.. rst-class:: left

Seriously, well worth the time.

What's a Subclass For?
----------------------

The most salient points from that video are as follows:

**Subclassing is not for Specialization**

**Subclassing is for Reusing Code**

**Bear in mind that the subclass is in charge**


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

  * is the it an attribute of the left-most superclass?
  * is the it an attribute of the next superclass?
  * and so on up the hierarchy...

* Is it a super-superclass attribute ?
* ... also left to right ...

http://python-history.blogspot.com/2010/06/method-resolution-order.html

.. nextslide:: Mix-ins

Provides an subset of expected functionality in a re-usable package.

Why would you want to do this?

Hierarchies are not always simple:

* Animal

  * Mammal

    * GiveBirth()
    
  * Bird
    
    * LayEggs()
    
Where do you put a Platypus?

Real World Example: `FloatCanvas`_

.. _FloatCanvas: https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L485

**Careful About This Pattern**


.. nextslide:: New-Style Classes

All the class definitions we've been showing inherit from ``object``.

This is referred to as a "new style" class.

They were introduced in python2.2 to better merge types and classes, and clean
up a few things.

There are differences in method resolution order and properties.

**Always Make New-Style Classes.**

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


.. nextslide:: Background

Two seminal articles about ``super()``:

"Super Considered Harmful" -- James Knight

https://fuhm.net/super-harmful/

"super() considered super!"  --  Raymond Hettinger

http://rhettinger.wordpress.com/2011/05/26/super-considered-super/}

(Both worth reading....)


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

.. nextslide:: properties

When (and if) you need them:

.. code-block:: python

    class C(object):
        def __init__(self, x=5):
            self._x = x
        def _getx(self):
            return self._x
        def _setx(self, value):
            self._x = value
        def _delx(self):
            del self._x
        x = property(_getx, _setx, _delx, doc="docstring")

Now the interface is still like simple attribute access!

.. rst-class:: centered small

[demo: :download:`properties_example.py <./supplements/properties_example.py>`]


.. nextslide:: "Read Only" Attributes

Not all the arguments to ``property`` are required.

You can use this to create attributes that are "read only":

.. code-block:: ipython

    In [11]: class D(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = 5
       ....:     def getx(self):
       ....:         return self._x
       ....:     x = property(getx, doc="I am read only")
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


.. nextslide:: Syntactic Sugar

This *imperative* style of adding a ``property`` to you class is clear, but
it's still a little verbose.

It also has the effect of leaving all those defined method objects laying
around:

.. code-block:: ipython

    In [19]: d.x
    Out[19]: 5
    In [20]: d.getx
    Out[20]: <bound method D.getx of <__main__.D object at 0x1043a4a10>>
    In [21]: d.getx()
    Out[21]: 5

.. nextslide::

Python provides us with a way to solve both these issues at once, using a
syntactic feature called **decorators** (more about these next session):

.. code-block:: ipython

    In [22]: class E(object):
       ....:     def __init__(self, x=5):
       ....:         self._x = x
       ....:     @property
       ....:     def x(self):
       ....:         return self._x
       ....:     @x.setter
       ....:     def x(self, value):
       ....:         self._x = value
       ....:
    In [23]: e = E()
    In [24]: e.x
    Out[24]: 5
    In [25]: e.x = 6
    In [26]: e.x
    Out[26]: 6


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
       ....:     def add(a, b):
       ....:         return a + b
       ....:     add = staticmethod(add)
       ....:

    In [37]: StaticAdder.add(3, 6)
    Out[37]: 9

.. rst-class:: centered

[demo: :download:`static_method.py <./supplements/static_method.py>`]


.. nextslide:: Syntactic Sugar

Like ``properties``, static methods can be written *declaratively* using the
``staticmethod`` built-in as a *decorator*:

.. code-block:: python

    class StaticAdder(object):
        @staticmethod
        def add(a, b):
            return a + b

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
       ....:     def a_class_method(cls, y):
       ....:         print "in a class method: ", cls
       ....:         return y ** cls.x
       ....:     a_class_method = classmethod(a_class_method)
       ....:
    In [42]: Classy.a_class_method(4)
    in a class method:  <class '__main__.Classy'>
    Out[42]: 16

.. rst-class:: centered

[demo: :download:`class_method.py <./supplements/class_method.py>`]

.. nextslide:: Syntactic Sugar

Once again, the ``classmethod`` built-in can be used as a *decorator* for a
more declarative style of programming:

.. code-block:: python

    class Classy(object):
        x = 2
        @classmethod
        def a_class_method(cls, y):
            print "in a class method: ", cls
            return y ** cls.x

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


Kicking the Tires
-----------------

Copy the file ``code/session07/circly.py`` to your student folder.

In it, write a simple "Circle" class:

.. code-block:: ipython

    In [13]: c = Circle(3)
    In [15]: c.diameter
    Out[15]: 6.0
    In [16]: c.diameter = 8
    In [17]: c.radius
    Out[17]: 4.0
    In [18]: c.area
    Out[18]: 50.26548245743669


Use ``properties`` so you can keep the radius and diameter in sync, and the
area computed on the fly.

Extra Credit: use a class method to make an alternate constructor that takes
the diameter instead.


.. nextslide::

Also copy the file ``test_circle1.py`` to your student folder.

As you work, run the tests:

.. code-block:: bash

    (cff2py)$ py.test test_circle1.py

As each of the requirements from above are fulfilled, you'll see tests 'turn
green'.

When all your tests are passing, you've completed the job.

(This clear finish line is another of the advantages of TDD)


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

.. nextslide:: Protocols

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

For example, to make '+' work with a sequence type in a vector-like fashion, implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])

.. rst-class:: centered

[a more complete example may be seen :download:`here <./supplements/vector.py>`]


.. nextslide:: Generally Useful Special Methods

You only *need* to define the special methods that will be used by your class.

However, even in the absence of wanting to duck-type, you should almost always
define these:

``object.__str__``:
  Called by the str() built-in function and by the print statement to compute
  the *informal* string representation of an object.

``object.__unicode__``:
  Called by the unicode() built-in function.  This converts an object to an
  *informal* unicode representation.

``object.__repr__``:
  Called by the repr() built-in function and by string conversions (reverse
  quotes) to compute the *official* string representation of an object.

  (ideally: ``eval( repr(something) ) == something``)

.. nextslide:: Summary

Use special methods when you want your class to act like a "standard" class in
some way.

Look up the special methods you need and define them.

There's more to read about the details of implementing these methods:

* https://docs.python.org/2/reference/datamodel.html#special-method-names
* http://www.rafekettler.com/magicmethods.html

Be a bit cautious about the code examples in that last one. It uses quite a bit
of old-style class definitions, which should not be emulated.


Kicking the Tires
-----------------

Extend your "Circle" class:

* Add ``__str__``  and ``__repr__``  methods
* Write an ``__add__``  method so you can add two circles
* Make it so you can multiply a circle by a number....

.. code-block:: ipython

    In [22]: c1 = Circle(3)
    In [23]: c2 = Circle(4)
    In [24]: c3 = c1+c2
    In [25]: c3.radius
    Out[25]: 7
    In [26]: c1*3
    Out[26]: Circle(9)

If you have time: compare them... (``c1 > c2`` , etc)


.. nextslide::

As you work, run the tests in ``test_circle2.py``:

.. code-block:: bash

    (cff2py)$ py.test test_circle2.py

As each of the requirements from above are fulfilled, you'll see tests 'turn
green'.

When all your tests are passing, you've completed the job.


Homework
========

.. rst-class:: centered large

Testing, Testing, 1 2 3


Assignment
----------

If you are not yet done, complete the ``Circle`` class so that all tests in
``test_circle2.py`` pass.

Go back over some of your assignments from the last weeks.

Convert tests that are currently in the ``if __name__ == '__main__':`` blocks
into standalone pytest files.

Name each test file so that it is clear with which source file it belongs::

    test_rot13.py -> rot13.py

Add unit tests for the HTML Renderer that you are currently constructing.

Create at least 4 test files with tests that well exercise the features built
in each source file.

