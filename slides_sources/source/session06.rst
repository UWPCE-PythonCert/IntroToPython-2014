.. include:: include.rst

***********************************************
Session Six: Testing, Advanced Argument Passing
***********************************************

======================
Lightning Talks Today:
======================

.. rst-class:: medium

    Adam Hollis

    Nachiket Galande

    Paul A Casey

================
Review/Questions
================

Review of Previous Class
------------------------

* Exceptions

* Comprehensions


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

You don't actually need to use the result of a list comp:

.. code-block:: python

    for i, st in zip( divisors, sets):
        [ st.add(j) for j in range(21) if not j%i ]

.. nextslide::

Python functions are objects, so if you don't call them, you don't get an error, you just get the function object, usually not what you want::

        elif donor_name.lower == "exit":

this is comparing the string ``lower`` method to the string "exit" and they are never going to be equal!

That should be::

    elif donor_name.lower() == "exit":

This is actually a pretty common typo -- keep an eye out for it when you get strange errors, or something just doesn't seem to be getting triggered.

long strings
------------

if you need to do along string literal, sometimes a triple quoted string is perfect::

  """this is a long string.
  I want it to hvae multiple lines.
  so having the line endings automatic is great.
  """

But you don't always want the line endings quite like that. And you may not want all that whitespace when fitting it into indented code.

It turns out that when you put a multiple strings together with no commas or anythign in between -- python will join them:

.. code-block:: ipython

  In [81]: "this is " "a string " "built up of parts"
  Out[81]: 'this is a string built up of parts'

.. nextslide::

If it's in parentheses, you can put the next chunk on the next line:

.. code-block:: python

  print("{} is from {}, and he likes "
        "{} cake, {} fruit, {} salad, "
        "and {} pasta.".format(food_prefs["name"],
                               food_prefs["city"],
                               food_prefs["cake"],
                               food_prefs["fruit"],
                               food_prefs["salad"],
                               food_prefs["pasta"]))

pretty print
------------

If you need to print our nested (or large) data structure in a more readable fashion, the "pretty print" module is handy:

.. code-block:: ipython

  from pprint import pprint

    In [28]: print(food_prefs)
    {'pasta': 'lasagna', 'cake': 'chocolate', 'salad': 'greek', 'fruit': 'mango', 'name': 'Chris', 'city': 'Seattle'}

    In [29]: pprint(food_prefs)
    {'cake': 'chocolate',
     'city': 'Seattle',
     'fruit': 'mango',
     'name': 'Chris',
     'pasta': 'lasagna',
     'salad': 'greek'}

Exceptions
----------

Adding stuff to an Exception:

Example from slack


Anything else?
--------------

.. rst-class:: center medium

   Anything else you want me to go over?


Lightning Talks
----------------

.. rst-class:: medium

|
| Adam Hollis
|
| Nachiket Galande
|

=======
Testing
=======

.. rst-class:: build left
.. container::

    You've already seen a very basic testing strategy.

    You've written some tests using that strategy.

    These tests were pretty basic, and a bit awkward in places (testing error
    conditions in particular).

    .. rst-class:: centered large

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


Standard Library: ``unittest``
-------------------------------

The original testing system in Python.

``import unittest``

More or less a port of ``Junit`` from Java

A bit verbose: you have to write classes & methods

(And we haven't covered that yet!)


Using ``unittest``
-------------------

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

    The ``unittest`` module is pretty full featured

    It comes with the standard Python distribution, no installation required.

    It provides a wide variety of assertions for testing all sorts of situations.

    It allows for a setup and tear down workflow both before and after all tests and before and after each test.

    It's well known and well understood.

.. nextslide:: Disadvantages:

.. rst-class:: build
.. container::


    It's Object Oriented, and quite "heavyweight".

      - modeled after Java's ``junit`` and it shows...

    It uses the framework design pattern, so knowing how to use the features
    means learning what to override.

    Needing to override means you have to be cautious.

    Test discovery is both inflexible and brittle.

    And there is no built-in parameterized testing.

Other Options
-------------

There are several other options for running tests in Python.

* `Nose`: https://nose.readthedocs.org/

* `pytest`: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. django)

Both are very capable and widely used. I have a personal preference for pytest

-- so we'll use it for this class

Installing ``pytest``
---------------------

The first step is to install the package:

.. code-block:: bash

    $ python3 -m pip install pytest

Once this is complete, you should have a ``py.test`` command you can run
at the command line:

.. code-block:: bash

    $ py.test

If you have any tests in your repository, that will find and run them.

.. rst-class:: build
.. container::

    **Do you?**

Pre-existing Tests
------------------

Let's take a look at some examples.

in ``IntroPython2016\Examples\Session06``

.. code-block:: bash

  $ py.test

You can also run py.test on a particular test file:

.. code-block:: bash

  $ py.test test_random_unitest.py

The results you should have seen when you ran ``py.test`` above come
partly from these files.

Let's take a few minutes to look these files over.

[demo]

What's Happening Here.
----------------------

When you run the ``py.test`` command, ``pytest`` starts in your current
working directory and searches the filesystem for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

pytest
------

This test running framework is simple, flexible and configurable.

Read the documentation for more information:

http://pytest.org/latest/getting-started.html#getstarted

It will run ``unittest`` tests for you.

But in addition to finding and running tests, it makes writting tests simple, and provides a bunch of nifty utilities to support more complex testing.


Test Driven Development
-----------------------
in the Examples dir, try::

  $ py.test test_cigar_party

What we've just done here is the first step in what is called:

.. rst-class:: centered

  **Test Driven Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write the code that fixes these tests.

Let's do that next!

Test Driven development demo
-----------------------------

Open up:

``Examples/Session06/test_cigar_party.py``

and:

``Examples/Session06/cigar_party.py``

and run::

  $ py.teset test_cigar_party.py

Now go in to ``cigar_party.py`` and let's fix the tests.

Let's play with codingbat.py also...

===
LAB
===

.. rst-class:: left

  Pick an example from codingbat:

  ``http://codingbat.com``

  Do a bit of test-driven development on it:

   * run something on the web site.
   * write a few tests using the examples from the site.
   * then write the function, and fix it 'till it passes the tests.

  Do at least two of these...

Lightning Talk
--------------

.. rst-class:: medium

    |
    | Paul A Casey
    |

=========================
Advanced Argument Passing
=========================

This is a very, very nifty Python feature -- it really lets you write dynamic programs.

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x=0, y=0, z=0):
            print(x,y,z)
       .....:
    In [152]: fun(1,2,3)
    1 2 3
    In [153]: fun(1, z=3)
    1 0 3
    In [154]: fun(z=3, y=2)
    0 2 3


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

This is a **very** important point -- I will repeat it!


Function arguments in variables
-------------------------------

When a function is called, its arguments are really just:

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
you know how this nifty trick works:

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

Kinda handy for the dict lab, eh?

This:

.. code-block:: ipython

  print("{} is from {}, and he likes "
        "{} cake, {} fruit, {} salad, "
        "and {} pasta.".format(food_prefs["name"],
                               food_prefs["city"],
                               food_prefs["cake"],
                               food_prefs["fruit"],
                               food_prefs["salad"],
                               food_prefs["pasta"]))

Becomes:

.. code-block:: ipython

  print("{name} is from {city}, and he likes "
        "{cake} cake, {fruit} fruit, {salad} salad, "
        "and {pasta} pasta.".format(**food_prefs))

LAB
----

Time to play with all this to get a feel for it.

:ref:`exercise_args_kwargs_lab`

This is not all that clearly specified -- the goal is for you to
experiment with various ways to define and call functions, so you
can understand what's possible, and what happens with each call.


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


========
Homework
========

.. rst-class:: left

  Finish up the Labs

  Write a complete set of unit tests for your mailroom program.

   * You will likely find that it is really hard to test without refactoring.

   * This is Good!

   * If code is hard to test -- it probably should be refactored.



Material to review for next week
--------------------------------

Next week, we'll get started on Object Oriented Methods. It's a good idea to read up on it first -- so we can dive right in:

 * Dive into Python3: 7.2 -- 7.3
   http://www.diveintopython3.net/iterators.html#defining-classes

 * Think Python: 15 -- 18
   http://www.greenteapress.com/thinkpython/html/thinkpython016.html

 * LPTHW: 40 -- 44
   http://learnpythonthehardway.org/book/ex40.html

[note that in py3 you don't need to inherit from object]

Talk by Raymond Hettinger:

Video of talk: https://youtu.be/HTLu2DFOdTg

Slides: https://speakerdeck.com/pyconslides/pythons-class-development-toolkit-by-raymond-hettinger

