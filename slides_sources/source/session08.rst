**************************************************************************
Session Eight: More OO: Multiple inheritance, Properties, Special methods.
**************************************************************************

.. rst-class:: large centered

The tools of Pythonicity


================
Review/Questions
================

Review of Previous Class
------------------------

* Basic OO Concepts

  * Classes
  * class vs. instance attributes
  * subclassing
  * overriding methods / attributes


Lightning Talks Today:
-----------------------

.. rst-class:: medium

  Robert Ryan Leslie

  Ryan Morin


Personal Project
-----------------

The bulk of the homework for the rest of the class will be a personal project:

* It can be for fun, or something you need for your job.
* It should be large enough to take a few weeks homework time to do.
* **It should demostrate that you can do something useful with python.**
* It should follow PEP8 (https://www.python.org/dev/peps/pep-0008)
* It should have unit tests!
* Ideally, it will be in version control (gitHub)
* I don't require any specific python features (i.e. classes): use
  what is appropriate for your project

* Due the Friday after the last class (December 11)

|
|  By next week, send me a project proposal: short and sweet.
|

Homework review
---------------

* html renderer
* Test-driven development

Homework Notes:
---------------

``**kwargs`` will always define a ``kwargs`` dict: it just may be empty.

And there is no need to check if it's empty before trying to loop through it.

.. code-block:: python

    if self.attributes != {}:
        for key, value in self.attributes.items():
            self.atts += ' {}="{}"'.format(key, value)

no need for ``!= {}`` -- an empty dict is "Falsey"

**but** no need for that check at all. If the dict (or ist, or tuple) is
empty, then the loop is a do-nothing operation:

* notes on Duck Typing: :ref:`exercise_html_renderer` and  code review

==========
Properties
==========

.. rst-class:: left
.. container::

    One of the strengths of Python is lack of clutter.

    Attributes are simple and concise:

    .. code-block:: ipython

        In [5]: class C:
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

    In [5]: class C:
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

    class C:
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

"Read Only" Attributes
----------------------

You do not need to define a setter. If you don't, you get a "read only" attribute:

.. code-block:: ipython

    In [11]: class D():
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

Deleters
---------

If you want to do something special when a property is deleted, you can define
a deleter is well:

.. code-block:: ipython

    In [11]: class D():
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

[demo: :download:`properties_example.py <../../Examples/Session08/properties_example.py>`]


===
LAB
===

Let's use some of this to build a nice class to represent a Circle.

For now, Let's do steps 1-4 of:

:ref:`exercise_circle_class`


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

    In [36]: class StaticAdder:

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

        class TarInfo:
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

    In [41]: class Classy:
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


Why?
----

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

Alternate Constructors
-----------------------

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

* https://docs.python.org/3.5/reference/datamodel.html#special-method-names
* http://www.rafekettler.com/magicmethods.html

===
LAB
===

Let's complete our nifty Circle class:

Steps 5-8 of:

:ref:`exercise_circle_class`






=========================
Emulating Standard types
=========================

.. rst-class:: medium

  Making your classes behave like the built-ins


Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)

.. nextslide::

But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable:
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)


Writing your own sequence type
-------------------------------

Python has a handful of nifty sequence types built in:

 * lists
 * tuples
 * strings
 * ...

But what if you need a sequence that isn't built in?

A Sparse array
--------------

Example: Sparse Array

Sometimes we have data sets that are "sparse" -- i.e. most of the values are zero.

So you may not want to store a huge bunch of zeros.

But you do want the array to look like a regular old sequence.

So how do you do that?

The Sequence protocol
----------------------

You can make your class look like a regular python sequence by defining
the set of special methods you need:

https://docs.python.org/2/reference/datamodel.html#emulating-container-types

and

http://www.rafekettler.com/magicmethods.html#sequence

The key ones are:

+-------------------+-----------------------+
|  ``__len__``      | for ``len(sequence)`` |
+-------------------+-----------------------+
|  ``__getitem__``  | for  ``x = seq[i]``   |
+-------------------+-----------------------+
|  ``__setitem__``  | for ``seq[i] = x``    |
+-------------------+-----------------------+
|  ``__delitem__``  | for ``del seq[i]``    |
+-------------------+-----------------------+
|  ``__contains__`` | for ``x in seq``      |
+-------------------+-----------------------+

====
LAB
====

.. rst-class:: medium

    Let's do the previous motivating examples.

Callables:
-----------

Write a class for a quadratic equation.

* The initializer for that class should take the parameters: ``a, b, c``

* It should store those parameters as attributes.

* The resulting instance should evaluate the function when called, and return the result:


.. code-block:: python

    my_quad = Quadratic(a=2, b=3, c=1)

    my_quad(0)

Sparse Array:
-------------

Write a class for a sparse array

* Internally, it can store the values in a dict, with the index as the keys)

* It should take a sequence of values as an initializer

* you should be able to tell how long it is: ``len(my_array)``

* It should support getting and setting particular elements via indexing.

* It should support deleting an element by index.

* It should raise an ``IndexError`` if you try to access an index beyond the end.

* Can you make it support slicing?

* How else can you  make it like a list?

.. code-block:: ipython

    In [10]: my_array = SparseArray( (1,0,0,0,2,0,0,0,5) )
    In [11]: my_array[4]
    Out[11]: 2
    In [12]: my_array[2]
    Out[12]: 0

Lightning Talks
----------------

.. rst-class:: medium

|
| Alireza Hashemloo
|
| Arielle R Simmons
|


=========================
Iterators and Generators
=========================

.. rst-class:: medium

    What goes on in those for loops?

Iterators
---------

Iterators are one of the main reasons Python code is so readable:

.. code-block:: python

    for x in just_about_anything:
        do_stuff(x)

It does not have to be a "sequence": list, tuple, etc.

Rather: you can loop through anything that satisfies the "iterator protocol"

http://docs.python.org/library/stdtypes.html#iterator-types

The Iterator Protocol
----------------------

An iterator must have the following methods:

.. code-block:: python

    an_iterator.__iter__()

Returns the iterator object itself. This is required to allow both containers
and iterators to be used with the ``for`` and ``in`` statements.

.. code-block:: python

    an_iterator.next()

Returns the next item from the container. If there are no further items,
raises the ``StopIteration`` exception.

List as an Iterator:
--------------------

.. code-block:: ipython

    In [10]: a_list = [1,2,3]

    In [11]: list_iter = a_list.__iter__()

    In [12]: list_iter.next()
    Out[12]: 1

    In [13]: list_iter.next()
    Out[13]: 2

    In [14]: list_iter.next()
    Out[14]: 3

    In [15]: list_iter.next()
    --------------------------------------------------
    StopIteration     Traceback (most recent call last)
    <ipython-input-15-1a7db9b70878> in <module>()
    ----> 1 list_iter.next()
    StopIteration:

Making an Iterator
-------------------

A simple version of ``xrange()``

.. code-block:: python

    class IterateMe_1:
        def __init__(self, stop=5):
            self.current = 0
            self.stop = stop
        def __iter__(self):
            return self
        def next(self):
            if self.current < self.stop:
                self.current += 1
                return self.current
            else:
                raise StopIteration

(demo: :download:`iterator_1.py <../../Examples/Session08/iterator_1.py>`)

``iter()``
-----------

How do you get the iterator object (the thing with the next() method) from an "iterable"?

The ``iter()`` function:

.. code-block:: ipython

    In [20]: iter([2,3,4])
    Out[20]: <listiterator at 0x101e01350>

    In [21]: iter("a string")
    Out[21]: <iterator at 0x101e01090>

    In [22]: iter( ('a', 'tuple') )
    Out[22]: <tupleiterator at 0x101e01710>

for an arbitrary object, ``iter()`` calls the ``__iter__`` method. But it knows about some objects (``str``, for instance) that don't have a ``__iter__`` method.


What does ``for`` do?
----------------------

Now that we know the iterator protocol, we can write something like a for loop:


:download:`my_for.py <../../Examples/Session08/my_for.py>`

.. code-block:: python

    def my_for(an_iterable, func):
        """
        Emulation of a for loop.

        func() will be called with each item in an_iterable
        """
        # equiv of "for i in l:"
        iterator = iter(an_iterable)
        while True:
            try:
                i = iterator.next()
            except StopIteration:
                break
            func(i)


Itertools
---------

``itertools``  is a collection of utilities that make it easy to
build an iterator that iterates over sequences in various common ways

http://docs.python.org/library/itertools.html

NOTE:

iterators are not *only* for ``for``

They can be used with anything that expects an iterator:

``sum``, ``tuple``, ``sorted``, and ``list``

For example.

LAB
-----

In the ``Examples/session08`` dir, you will find:
:download:`iterator_1.py <../../Examples/Session08/iterator_1.py>`

* Extend (``iterator_1.py`` ) to be more like ``xrange()`` -- add three input parameters: ``iterator_2(start, stop, step=1)``

* See what happens if you break out in the middle of the loop:

.. code-block:: python

    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print i

And then pick up again:

.. code-block:: python

    for i in it:
        print i

* Does ``xrange()``  behave the same?

  - make yours match ``xrange()``

LAB2
-----

Make the SparseArray class from the previous lab an iterator, so you can do:

.. code-block:: python

    for i in my_sparse_array:
        do_something_with(i)




Generators
----------

Generators give you the iterator immediately:

* no access to the underlying data ... if it even exists


Conceptually:
  Iterators are about various ways to loop over data, generators generate the data on the fly.

Practically:
  You can use either one either way (and a generator is one type of iterator)

  Generators do some of the book-keeping for you -- simpler syntax.

yield
------

``yield``  is a way to make a quickie generator with a function:

.. code-block:: python

    def a_generator_function(params):
        some_stuff
        yield something

Generator functions "yield" a value, rather than returning a value.

State is preserved in between yields.


.. nextslide:: generator functions

A function with ``yield``  in it is a "factory" for a generator

Each time you call it, you get a new generator:

.. code-block:: python

    gen_a = a_generator()
    gen_b = a_generator()

Each instance keeps its own state.

Really just a shorthand for an iterator class that does the book keeping for you.

.. nextslide::

An example: like ``xrange()``

.. code-block:: python

    def y_xrange(start, stop, step=1):
        i = start
        while i < stop:
            yield i
            i += step

Real World Example from FloatCanvas:

https://github.com/svn2github/wxPython/blob/master/3rdParty/FloatCanvas/floatcanvas/FloatCanvas.py#L100


.. nextslide::

Note:

.. code-block:: ipython

    In [164]: gen = y_xrange(2,6)
    In [165]: type(gen)
    Out[165]: generator
    In [166]: dir(gen)
    Out[166]:
    ...
     '__iter__',
    ...
     'next',


So the generator **is** an iterator

Note: A generator function can also be a method in a class


.. More about iterators and generators:

.. http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/

:download:`yield_example.py <../../Examples/Session08/yield_example.py>`

generator comprehension
-----------------------

yet another way to make a generator:

.. code-block:: python

    ￼>>> [x * 2 for x in [1, 2, 3]]
    [2, 4, 6]
    >>> (x * 2 for x in [1, 2, 3])
    <generator object <genexpr> at 0x10911bf50>
    >>> for n in (x * 2 for x in [1, 2, 3]):
    ...   print n
    ... 2 4 6


More interesting if [1, 2, 3] is also a generator

LAB
----

Write a few generators:

* Sum of integers
* Doubler
* Fibonacci sequence
* Prime numbers

(test code in
:download:`test_generator.py <../../Examples/Session08/test_generator.py>`)

Descriptions:

Sum of the integers:
  keep adding the next integer

  0 + 1 + 2 + 3 + 4 + 5 + ...

  so the sequence is:

  0, 1, 3, 6, 10, 15 .....

.. nextslide::

Doubler:
  Each value is double the previous value:

  1, 2, 4, 8, 16, 32,

Fibonacci sequence:
  The fibonacci sequence as a generator:

  f(n) = f(n-1) + f(n-2)

  1, 1, 2, 3, 5, 8, 13, 21, 34...

Prime numbers:
  Generate the prime numbers (numbers only divisible by them self and 1):

  2, 3, 5, 7, 11, 13, 17, 19, 23...

Others to try:
  Try x^2, x^3, counting by threes, x^e, counting by minus seven, ...


========
Homework
========

Complete the Circle class

Decide what you are going to do for your proejct, and send me a simple proposal.


========
Homework
========

.. rst-class:: left medium

    Finish up the Labs from class

    Get started on your project!

    (Send me a proposal if you haven't already)
