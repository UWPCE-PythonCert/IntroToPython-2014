
********************************************************************
Session Six: Advanced Argument Passing, lambda, functions as objects
********************************************************************

.. rst-class:: left medium

    Advanced Argument passing

    Lambda

    Functions as objects

======================
Lightning Talks Today:
======================

.. rst-class:: medium

    Gabriel Meringolo

    Joseph Cardenas

    Marc Teale

================
Review/Questions
================

Review of Previous Class
------------------------

* Exceptions

* Comprehensions

* Testing (a bit more on that soon)

===============
Homework review
===============

Homework Questions?

Notes from Homework:
--------------------

Comparing to "singletons":

Use:

``if something is None``

Not:

``if something == None``

(also ``True`` and ``False``)

rich comparisons: numpy

(demo)

.. nextslide::

Binary mode for files:

.. code-block:: python

    infile = open(infilename, 'rb')
    outfile = open(outfilename, 'wb')

|
|

You don't actually need to use the result of a list comp:

.. code-block:: python

    for i, st in zip( divisors, sets):
        [ st.add(j) for j in range(21) if not j%i ]


The collections module
-----------------------

The collections module has a number of handy special purpose
collections:

 * defautltdict
 * namedtuple
 * deque
 * Counter

https://docs.python.org/3/library/collections.html

Did you all explore that a bit?

============================
Test Driven development demo
============================

In ``Examples/Session06/``

=========================
Advanced Argument Passing
=========================

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x,y=0,z=0):
            print(x,y,z)
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(1, z=3, y=2)
    1 2 3


.. nextslide::


A Common Idiom:

.. code-block:: python

    def fun(x, y=None):
        if y is None:
            do_something_different
        go_on_here



.. nextslide::

Can set defaults to variables

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4


.. nextslide::

Defaults are evaluated when the function is defined

.. code-block:: ipython

    In [156]: y = 4
    In [157]: def fun(x=y):
        print("x is:", x)
       .....:
    In [158]: fun()
    x is: 4
    In [159]: y = 6
    In [160]: fun()
    x is: 4


Function arguments in variables
-------------------------------

function arguments are really just

* a tuple (positional arguments)
* a dict (keyword arguments)

.. code-block:: python

    def f(x, y, w=0, h=0):
        print("position: {}, {} -- shape: {}, {}".format(x, y, w, h))

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f(*position, **size)
    position: 3, 4 -- shape: 20, 10



Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print("the positional arguments are:", args)
        print("the keyword arguments are:", kwargs)

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}

This can be very powerful...

Passing a dict to str.format()
-------------------------------

Now that you know that keyword args are really a dict,
you can do this nifty trick:

The string ``format()`` method takes keyword arguments:

.. code-block:: ipython

    In [24]: "My name is {first} {last}".format(last="Barker", first="Chris")
    Out[24]: 'My name is Chris Barker'

Build a dict of the keys and values:

.. code-block:: ipython

    In [25]: d = {"last":"Barker", "first":"Chris"}

And pass to ``format()``with ``**``

.. code-block:: ipython

    In [26]: "My name is {first} {last}".format(**d)
    Out[26]: 'My name is Chris Barker'

=====================================
A bit more on mutability (and copies)
=====================================

mutable objects
----------------

We've talked about this: mutable objects can have their contents changed in place.

Immutable objects can not.

This has implications when you have a container with mutable objects in it:

.. code-block:: ipython

    In [28]: list1 = [ [1,2,3], ['a','b'] ]

one way to make a copy of a list:

.. code-block:: ipython

    In [29]: list2 = list1[:]

    In [30]: list2 is list1
    Out[30]: False

they are different lists.

.. nextslide::

What if we set an element to a new value?

.. code-block:: ipython

    In [31]: list1[0] = [5,6,7]

    In [32]: list1
    Out[32]: [[5, 6, 7], ['a', 'b']]

    In [33]: list2
    Out[33]: [[1, 2, 3], ['a', 'b']]

So they are independent.

.. nextslide::

But what if we mutate an element?

.. code-block:: ipython

    In [34]: list1[1].append('c')

    In [35]: list1
    Out[35]: [[5, 6, 7], ['a', 'b', 'c']]

    In [36]: list2
    Out[36]: [[1, 2, 3], ['a', 'b', 'c']]

uuh oh! mutating an element in one list mutated the one in the other list.

.. nextslide::

Why is that?

.. code-block:: ipython

    In [38]: list1[1] is list2[1]
    Out[38]: True

The elements are the same object!

This is known as a "shallow" copy -- Python doesn't want to copy more than it needs to, so in this case, it makes a new list, but does not make copies of the contents.

Same for dicts (and any container type -- even tuples!)

If the elements are immutable, it doesn't really make a differnce -- but be very careful with mutable elements.


The copy module
----------------

most objects have a way to make copies (``dict.copy()`` for instance).

but if not, you can use the ``copy`` module to make a copy:

.. code-block:: ipython

    In [39]: import copy

    In [40]: list3 = copy.copy(list2)

    In [41]: list3
    Out[41]: [[1, 2, 3], ['a', 'b', 'c']]

This is also a shallow copy.

.. nextslide::

But there is another option:

.. code-block:: ipython

    In [3]: list1
    Out[3]: [[1, 2, 3], ['a', 'b', 'c']]

    In [4]: list2 = copy.deepcopy(list1)

    In [5]: list1[0].append(4)

    In [6]: list1
    Out[6]: [[1, 2, 3, 4], ['a', 'b', 'c']]

    In [7]: list2
    Out[7]: [[1, 2, 3], ['a', 'b', 'c']]

``deepcopy`` recurses through the object, making copies of everything as it goes.

.. nextslide::


I happened on this thread on stack overflow:

http://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep

The OP is pretty confused -- can you sort it out?

Make sure you understand the difference between a reference, a shallow copy, and a deep copy.

Mutables as default arguments:
------------------------------

Another "gotcha" is using mutables as default arguments:

.. code-block:: ipython

    In [11]: def fun(x, a=[]):
       ....:     a.append(x)
       ....:     print(a)
       ....:

This makes sense: maybe you'd pass in a specific list, but if not, the default is an empty list.

But:

.. code-block:: ipython

    In [12]: fun(3)
    [3]

    In [13]: fun(4)
    [3, 4]

Huh?!

.. nextslide::

Remember that that default argument is defined when the function is created: there will be only one list, and every time the function is called, that same list is used.


The solution:

The standard practice for such a mutable default argument:

.. code-block:: ipython

    In [15]: def fun(x, a=None):
       ....:     if a is None:
       ....:         a = []
       ....:     a.append(x)
       ....:     print(a)
    In [16]: fun(3)
    [3]
    In [17]: fun(4)
    [4]

You get a new list every time the function is called


LAB
----

.. rst-class:: medium

  keyword arguments:

* Write a function that has four optional parameters (with defaults):

  - fore_color
  - back_color
  - link_color
  - visited_color

* Have it print the colors (use strings for the colors)
* Call it with a couple different parameters set
* Have it pull the parameters out with ``*args, **kwargs``
  - and print those


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

Called "Anonymous": it doesn't need a name.

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
It keeps only those for which the function is True

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

Can also use keyword arguments

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

lambda and keyword argument magic
-----------------------------------

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increasing number.

Use a for loop, ``lambda``, and a keyword argument

( Extra credit ):

Do it with a list comprehension, instead of a for loop

Not clear? here's what you should get

.. nextslide:: Example calling code

.. code-block:: ipython

    In [96]: the_list = function_builder(4)
    ### so the_list should contain n functions (callables)
    In [97]: the_list[0](2)
    Out[97]: 2
    ## the zeroth element of the list is a function that add 0
    ## to the input, hence called with 2, returns 2
    In [98]: the_list[1](2)
    Out[98]: 3
    ## the 1st element of the list is a function that adds 1
    ## to the input value, thus called with 2, returns 3
    In [100]: for f in the_list:
        print(f(5))
       .....:
    5
    6
    7
    8
    ### If you loop through them all, and call them, each one adds one more
    to the input, 5... i.e. the nth function in the list adds n to the input.



Lightning Talks
----------------

.. rst-class:: medium

|
| Aleksey Kramer
|
| Alexander R Galvin
|


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

        In [4]: class C(object):
            pass
           ...:
        In [5]: type(C)
        Out[5]: type

    A class is a type -- interesting!

    It is created when the statement is run -- much like ``def``

    You don't *have* to subclass from ``object``, but you *should*

    (note on "new style" classes)

Python Classes
--------------

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
    print("p.x is:", p.x)
    print("p.y is:", p.y)


see: ``Examples/Session06/simple_classes.py``

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

