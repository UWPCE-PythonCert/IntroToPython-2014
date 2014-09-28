********************************************
Session Two: Functions, Booleans and Modules
********************************************

.. ifslides::

    .. rst-class:: center large

    Oh My!



Review/Questions
================

Review of Previous Session
--------------------------

.. rst-class:: build

  * Values and Types
  * Expressions
  * Intro to functions

Homework Review
---------------

.. rst-class:: center large

Any questions that are nagging?


Git Work
========

.. rst-class:: center large

Let's get to know your fellow students!


Working with an Upstream
------------------------

You've created a fork of the class repository from the ``codefellows`` account
on GitHub.

You've pushed your own changes to that fork, and then issued pull requests to
have that worked merged back to the ``codefellows`` original.

You want to keep your fork up-to-date with that original copy as the class goes
forward.

To do this, you use the git concept of an **upstream** repository.

.. nextslide::

Since ``git`` is a *distributed* versioning system, there is no **central**
repository that serves as the one to rule them all.

Instead, you work with *local* repositories, and *remotes* that they are
connected to.

Cloned repositories get an *origin* remote for free:

.. code-block:: bash

    $ git remote -v
    origin  https://github.com/PythonCHB/sea-f2-python-sept14.git (fetch)
    origin  https://github.com/PythonCHB/sea-f2-python-sept14.git (push)

This shows that the local repo on my machine *originated* from the one in my gitHub account (the one it was cloned from)

.. nextslide:: Adding a Remote

You can add *remotes* at will, to connect your *local* repository to other
copies of it in different remote locations.

This allows you to grab changes made to the repository in these other
locations.

For our class, we will add an *upstream* remote to our local copy that points
to the original copy of the material in the ``codefellows`` account.

.. code-block:: bash

  $ git remote add upstream https://github.com/codefellows/sea-f2-python-sept14.git

  $ git remote -v
  origin  https://github.com/PythonCHB/sea-f2-python-sept14.git (fetch)
  origin  https://github.com/PythonCHB/sea-f2-python-sept14.git (push)
  upstream  https://github.com/codefellows/sea-f2-python-sept14.git (fetch)
  upstream  https://github.com/codefellows/sea-f2-python-sept14.git (push)

.. nextslide:: Fetching Everything.

To get the updates from your new remote, you'll need first to fetch everything:

.. code-block:: bash

    $ git fetch --all
    Fetching origin
    Fetching upstream
    ...

Then you can see the branches you have locally available:

.. code-block:: bash

  $ git branch -a
  * master
    remotes/origin/HEAD -> origin/master
    remotes/origin/gh-pages
    remotes/origin/master
    remotes/upstream/gh-pages
    remotes/upstream/master

(the gh-pages branch is used to publish these notes)

.. nextslide:: Fetching Upstream Changes

Finally, you can fetch and then merge changes from the upstream master.

Start by making sure you are on your own master branch:

.. code-block:: bash

    $ git checkout master

This is **really really** important.  Take the time to ensure you are where you
think you are.

.. nextslide:: Merging Upstream Changes

Then, fetch the upstream master branch and merge it into your master:

.. code-block:: bash

  $ git fetch upstream master
  From https://github.com/codefellows/sea-f2-python-sept14
   * branch            master     -> FETCH_HEAD

  $ git merge upstream/master
  Updating 3239de7..9ddbdbb
  Fast-forward
   Examples/README.rst              |  4 ++++
  ...
   create mode 100644 Examples/README.rst
  ...

NOTE: you can do that in one step with:

.. code-block:: bash

  $ git pull upstream master

.. nextslide:: Pushing to Origin

Now all the changes from *upstream* are present in your local clone.

In order to preserve them in your fork on GitHub, you'll have to push:

.. code-block:: bash

    $ git status
    On branch master
    Your branch is ahead of 'origin/master' by 10 commits.
      (use "git push" to publish your local commits)
    $ git push origin master
    Counting objects: 44, done.
    ...
    $

(A simple ``git push`` will usually do the right thing)

.. nextslide:: Daily Workflow

You can incorporate this into your daily workflow: ::

    $ git checkout master
    $ git pull upstream master
    $ git push
    [do some work]
    $ git commit -a 
    [add a good commit message]
    $ git push
    [make a pull request]

Quick Intro to Basics
=====================

.. rst-class:: center large

Because there's a few things you just gotta have

Basics
------

It turns out you can't really do much at all without at least a container type,
conditionals and looping...


.. nextslide:: if

``if`` and ``elif`` allow you to make decisions:

.. code-block:: python

    if a:
        print 'a'
    elif b:
        print 'b'
    elif c:
        print 'c'
    else:
        print 'that was unexpected'


.. nextslide:: if

What's the difference between these two:

.. code-block:: python

    if a:
        print 'a'
    elif b:
        print 'b'
    ## versus...
    if a:
        print 'a'
    if b:
        print 'b'


.. nextslide:: switch?

Many languages have a ``switch`` construct:

.. code-block:: js

    switch (expr) {
      case "Oranges":
        document.write("Oranges are $0.59 a pound.<br>");
        break;
      case "Apples":
        document.write("Apples are $0.32 a pound.<br>");
        break;
      case "Mangoes":
      case "Papayas":
        document.write("Mangoes and papayas are $2.79 a pound.<br>");
        break;
      default:
        document.write("Sorry, we are out of " + expr + ".<br>");
    }

.. nextslide:: switch?

**Not Python**

use ``if..elif..elif..else`` 

(or a dictionary, or subclassing....)


.. nextslide:: lists

A way to store a bunch of stuff in order

Pretty much like an "array" or "vector" in other languages

.. code-block:: python

    a_list = [2,3,5,9]
    a_list_of_strings = ['this', 'that', 'the', 'other']


.. nextslide:: tuples

Another way to store an ordered list of things

.. code-block:: python

    a_tuple = (2,3,4,5)
    a_tuple_of_strings = ('this', 'that', 'the', 'other')


Tuples are **not** the same as lists.

The exact difference is a topic for next session.


.. nextslide:: for

Sometimes called a 'determinate' loop

When you need to do something to everything in a sequence

.. code-block:: ipython

    In [10]: a_list = [2,3,4,5]

    In [11]: for item in a_list:
       ....:     print item
       ....:
    2
    3
    4
    5


.. nextslide:: range() and for

Range builds lists of numbers automatically

Use it when you need to do something a set number of times

.. code-block:: ipython

    In [12]: range(6)
    Out[12]: [0, 1, 2, 3, 4, 5]

    In [13]: for i in range(6):
       ....:     print "*",
       ....:
    * * * * * *


.. nextslide:: Intricacies

This is enough to get you started.

Each of these have intricacies special to python

We'll get to those over the next couple of classes


Functions
=========

Review
------

Defining a function:

.. code-block:: python

    def fun(x, y):
        z = x+y
        return z


x, y, z are *local* names


Local vs. Global
----------------

Symbols bound in Python have a *scope*

That *scope* determines where a symbol is visible, or what value it has in a
given block.

.. code-block:: ipython

    In [14]: x = 32
    In [15]: y = 33
    In [16]: z = 34
    In [17]: def fun(y, z):
       ....:     print x, y, z
       ....:
    In [18]: fun(3, 4)
    32 3 4


x is global, y and z local to the function

.. nextslide::

But, did the value of y and z change in the *global* scope?

.. code-block:: ipython

    In [19]: y
    Out[19]: 33

    In [20]: z
    Out[20]: 34

.. nextslide::

In general, you should use global bindings mostly for constants.

In python we designate global constants by typing the symbols we bind to them
in ALL_CAPS

.. code-block:: python

    INSTALLED_APPS = [u'foo', u'bar', u'baz']
    CONFIGURATION_KEY = u'some secret value'
    ...

This is just a convention, but it's a good one to follow.


.. nextslide:: Global Gotcha

Take a look at this function definition:

.. code-block:: ipython

    In [21]: x = 3

    In [22]: def f():
       ....:     y = x
       ....:     x = 5
       ....:     print x
       ....:     print y
       ....:

What is going to happen when we call ``f``

.. nextslide:: Global Gotcha

Try it and see:

.. code-block:: ipython

    In [23]: f()
    ---------------------------------------------------------------------------
    UnboundLocalError                         Traceback (most recent call last)
    <ipython-input-23-0ec059b9bfe1> in <module>()
    ----> 1 f()

    <ipython-input-22-9225fa53a20a> in f()
          1 def f():
    ----> 2     y = x
          3     x = 5
          4     print x
          5     print y

    UnboundLocalError: local variable 'x' referenced before assignment

Because you are binding the symbol ``x`` locally, it becomes a local and masks
the global value already bound.


Parameters
----------

So far we've seen simple parameter lists:

.. code-block:: python

    def fun(x, y, z):
        print x, y, z

These types of parameters are called *positional*

When you call a function, you **must** provide arguments for all *positional*
parameters *in the order they are listed*


.. nextslide::

You can provide *default values* for parameters in a function definition:

.. code-block:: ipython

    In [24]: def fun(x=1, y=2, z=3):
       ....:     print x, y, z
       ....:

When parameters are given with default values, they become *optional*

.. code-block:: ipython

    In [25]: fun()
    1 2 3


.. nextslide::

You can provide arguments to a function call for *optional* parameters
positionally:

.. code-block:: ipython

    In [26]: fun(6)
    6 2 3
    In [27]: fun(6, 7)
    6 7 3
    In [28]: fun(6, 7, 8)
    6 7 8

Or, you can use the parameter name as a *keyword* to indicate which you mean:

.. code-block:: ipython

    In [29]: fun(y=4, x=1)
    1 4 3

.. nextslide::

Once you've provided a *keyword* argument in this way, you can no longer
provide any *positional* arguments:

.. code-block:: ipython

    In [30]: fun(x=5, 6)
      File "<ipython-input-30-4529e5befb95>", line 1
        fun(x=5, 6)
    SyntaxError: non-keyword arg after keyword arg

.. nextslide:: Parameters and Unpacking

This brings us to a fun feature of Python function definitions.

You can define a parameter list that requires an **unspecified** number of
*positional* or *keyword* arguments.

The key is the ``*`` (splat) or ``**`` (double-splat) operator:

.. code-block:: ipython

    In [31]: def fun(*args, **kwargs):
       ....:     print args, kwargs
       ....:
    In [32]: fun(1)
    (1,) {}
    In [33]: fun(1, 2, zombies="brains")
    (1, 2) {'zombies': 'brains'}
    In [34]: fun(1, 2, 3, zombies="brains", vampires="blood")
    (1, 2, 3) {'vampires': 'blood', 'zombies': 'brains'}

**args** and **kwargs** are *conventional* names for these.


Documentation
-------------

It's often helpful to leave information in your code about what you were
thinking when you wrote it.

This can help reduce the number of `WTFs per minute`_ in reading it later.

.. _WTFs per minute: http://www.osnews.com/story/19266/WTFs_m

There are two approaches to this:

.. rst-class:: build

* Comments
* Docstrings

.. nextslide:: Comments

Comments go inline in the body of your code, to explain reasoning:

.. code-block:: python

    if (frobnaglers > whozits):
        # borangas are shermed to ensure frobnagler population
        # does not grow out of control
        sherm_the_boranga()

You can use them to mark places you want to revisit later:

.. code-block:: python

    for partygoer in partygoers:
        for baloon in baloons:
            for cupcake in cupcakes:
                # TODO: Reduce time complexity here.  It's killing us
                #  for large parties.
                resolve_party_favor(partygoer, baloon, cupcake)

.. nextslide:: Comments

Be judicious in your use of comments.

Use them when you need to.

Make them useful.

This is not useful:

.. code-block:: python

    for sponge in sponges:
        # apply soap to each sponge
        worker.apply_soap(sponge)

.. nextslide:: Docstrings

In Python, ``docstrings`` are used to provide in-line documentation in a number
of places.

The first place we will see is in the definition of ``functions``.

To define a function you use the ``def`` keyword.

If a ``string literal`` is the first thing in the function block following the
header, it is a ``docstring``:

.. code-block:: python

    def complex_function(arg1, arg2, kwarg1=u'bannana'):
        """Return a value resulting from a complex calculation."""
        # code block here

You can then read this in an interpreter as the ``__doc__`` attribute of the
function object.

.. nextslide:: Docstrings

A ``docstring`` should:

.. rst-class:: build

* be a complete sentence in the form of a command describing what the function
  does.

  * """Return a list of values based on blah blah""" is a good docstring
  * """Returns a list of values based on blah blah""" is *not*

* fit onto a single line.

  * If more description is needed, make the first line a complete sentence and
    add more lines below for enhancement.

* be enclosed with triple-quotes.

  * This allows for easy expansion if required at a later date
  * Always close on the same line if the docstring is only one line.

For more information see `PEP 257: Docstring Conventions`_.

.. _PEP 257\: Docstring Conventions: http://legacy.python.org/dev/peps/pep-0257/


Recursion
---------

You've seen functions that call other functions.

If a function calls *itself*, we call that **recursion**

Like with other functions, a call within a call establishes a *call stack*

With recursion, if you are not careful, this stack can get *very* deep.

Python has a maximum limit to how much it can recurse. This is intended to
save your machine from running out of RAM.

.. nextslide:: Recursion can be Useful

Recursion is especially useful for a particular set of problems.

For example, take the case of the *factorial* function.

In mathematics, the *factorial* of an integer is the result of multiplying that
integer by every integer smaller than it down to 1.

::

    5! == 5 * 4 * 3 * 2 * 1

We can use a recursive function nicely to model this mathematical function

.. ifslides::

    .. rst-class:: centered

    [demo]


In-Class Lab:
=============

.. rst-class:: center large

Fun With Functions

Exercises
---------

Try your hand at writing a function that computes the distance between two
points::

    dist = sqrt( (x1-x2)**2 + (y1-y2)**2 )

Experiment with ``locals`` by adding this statement to the function you just
wrote:::

    print locals()


Boolean Expressions
===================

Truthiness
----------

What is true or false in Python?

.. rst-class:: build

* The Booleans: ``True``  and ``False`` 
* "Something or Nothing"
*  http://mail.python.org/pipermail/python-dev/2002-April/022107.html 


.. nextslide::

Determining Truthiness:

.. code-block:: python

    bool(something)


.. nextslide:: What is False?

.. rst-class:: build

* ``None`` 
* ``False`` 
* **Nothing:**

* zero of any numeric type: ``0, 0L, 0.0, 0j``.
* any empty sequence, for example, ``"", (), []``.
* any empty mapping, for example, ``{}`` .
* instances of user-defined classes, if the class defines a ``__nonzero__()``
  or ``__len__()`` method, when that method returns the integer zero or bool
  value ``False``.

* http://docs.python.org/library/stdtypes.html

.. nextslide:: What is True?

.. rst-class:: center large

Everything Else


.. nextslide:: Pythonic Booleans

Any object in Python, when passed to the ``bool()`` type object, will
evaluate to ``True`` or ``False``.

When you use the ``if`` keyword, it automatically does this to the statement provided.

Which means that this is redundant, and not Pythonic:

.. code-block:: python

    if xx == True:
        do_something()
    # or even worse:
    if bool(xx) == True:
        do_something()

Instead, use what Python gives you:

.. code-block:: python

    if xx:
        do_something()


and, or and not
----------------

Python has three boolean keywords, ``and``, ``or`` and ``not``.

``and`` and ``or`` are binary expressions, and evaluate from left to right.

``and`` will return the first operand that evaluates to False, or the last
operand if none are True:

.. code-block:: ipython

    In [35]: 0 and 456
    Out[35]: 0

``or`` will return the first operand that evaluates to True, or the last
operand if none are True:

.. code-block:: ipython

    In [36]: 0 or 456
    Out[36]: 456

.. nextslide::

On the other hand, ``not`` is a unary expression and inverts the boolean value
of its operand:

.. code-block:: ipython

    In [39]: not True
    Out[39]: False

    In [40]: not False
    Out[40]: True

.. nextslide:: Shortcutting

Because of the return value of these keywords, you can write concise
statements:

::

                      if x is false,
    x or y               return y,
                         else return x

                      if x is false,
    x and y               return  x
                          else return y

                      if x is false,
    not x               return True,
                        else return False


.. nextslide:: Chaining

.. code-block:: python

    a or b or c or d
    a and b and c and d


The first value that defines the result is returned

.. ifslides::

    .. rst-class:: centered

    (demo)


.. nextslide:: Ternary Expressions

This is a fairly common idiom:

.. code-block:: python

    if something:
        x = a_value
    else:
        x = another_value

In other languages, this can be compressed with a "ternary operator"::

    result = a > b ? x : y;

In python, the same is accomplished with the ternary expression:

.. code-block:: python

    y = 5 if x > 2 else 3

PEP 308:
(http://www.python.org/dev/peps/pep-0308/)


Boolean Return Values
---------------------

Remember this puzzle from your CodingBat exercises?

.. code-block:: python

    def sleep_in(weekday, vacation):
        if weekday == True and vacation == False:
            return False
        else:
            return True

Though correct, that's not a particularly Pythonic way of solving the problem.

Here's a better solution:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return not (weekday == True and vacation == False)


.. nextslide::

And here's an even better one:

.. code-block:: python

    def sleep_in(weekday, vacation):
        return (not weekday) or vacation


.. nextslide:: bools are integers?

In python, the boolean types are subclasses of integer:

.. code-block:: ipython

    In [1]: True == 1
    Out[1]: True
    In [2]: False == 0
    Out[2]: True


And you can even do math with them (though it's a bit odd to do so):

.. code-block:: ipython

    In [6]: 3 + True
    Out[6]: 4

.. ifslides::

    .. rst-class:: center

    (demo)


In-Class Lab:
=============

.. rst-class:: center large

Better With Booleans

Exercises
---------

  * Look up the ``%``  operator. What do these do?

    * ``10 % 7 == 3``
    * ``14 % 7 == 0``
  *  Write a program that prints the numbers from 1 to 100 inclusive. But for
     multiples of three print "Fizz" instead of the number and for the
     multiples of five print "Buzz". For numbers which are multiples of both
     three and five print "FizzBuzz" instead.
  * Re-write a couple of CodingBat exercises, using a conditional expression
  * Re-write a couple of CodingBat exercises, returning the direct boolean results

use whichever you like, or the ones in:
:download:`codingbat.rst <../code/session02/codingbat.rst>`


Code Structure, Modules, and Namespaces
=======================================

.. rst-class:: center large

How to get what you want when you want it.


Code Structure
--------------

In Python, the structure of your code is determined by whitespace.

How you *indent* your code determines how it is structured

::

    block statement:
        some code body
        some more code body
        another block statement:
            code body in
            that block

The colon that terminates a block statement is also important...

.. nextslide:: One-liners

You can put a one-liner after the colon:

.. code-block:: ipython

    In [167]: x = 12
    In [168]: if x > 4: print x
    12

But this should only be done if it makes your code **more** readable.


.. nextslide:: Spaces vs. Tabs

Whitespace is important in Python.

An indent *could* be:

* Any number of spaces
* A tab
* A mix of tabs and spaces:

If you want anyone to take you seriously as a Python developer:

.. rst-class:: centered

**Always use four spaces -- really!**

`(PEP 8)`_

.. _(PEP 8): http://legacy.python.org/dev/peps/pep-0008/


.. nextslide:: Spaces Elsewhere

Other than indenting -- space doesn't matter, technically.

.. code-block:: python

    x = 3*4+12/func(x,y,z)
    x = 3*4 + 12 /   func (x,   y, z)

But you should strive for proper style.  Read `PEP 8`_ and install a linter in
your editor.

.. _PEP 8: http://legacy.python.org/dev/peps/pep-0008/


Modules and Packages
--------------------

Python is all about *namespaces* --  the "dots"

``name.another_name``

The "dot" indicates that you are looking for a name in the *namespace* of the
given object. It could be:

* name in a module
* module in a package
* attribute of an object
* method of an object


.. nextslide:: Modules

A module is simply a namespace.

It might be a single file, or it could be a collection of files that define a
shared API.

To a first approximation, you can think of the files you write that end in
``.py`` as modules.

.. nextslide:: Packages

A package is a module with other modules in it.

On a filesystem, this is represented as a directory that contains one or more
``.py`` files, one of which **must** be called ``__init__.py``.

When you have a package, you can import the package, or any of the modules
inside it.

.. nextslide:: importing modules

.. code-block:: python

    import modulename
    from modulename import this, that
    import modulename as a_new_name
    from modulename import this as that

.. ifslides::

    .. rst-class:: centered

    (demo)


.. nextslide:: importing from packages

.. code-block:: python

    import packagename.modulename
    from packagename.modulename import this, that
    from package import modulename

.. ifslides::

    .. rst-class:: centered

    (demo)

http://effbot.org/zone/import-confusion.htm

.. nextslide:: importing from packages

.. code-block:: python

    from modulename import *

.. rst-class:: centered large

**Don't do this!**


Import
------

When you import a module, or a symbol from a module, the Python code is
*compiled* to **bytecode**.

The result is a ``module.pyc`` file.

This process **executes all code at the module scope**.

For this reason, it is good to avoid module-scope statements that have global
side-effects.


.. nextslide:: Re-import

The code in a module is NOT re-run when imported again

It must be explicitly reloaded to be re-run

.. code-block:: python

    import modulename
    reload(modulename)

.. ifslides::

    .. rst-class:: centered

    (demo)


.. nextslide:: Running a Module

In addition to importing modules, you can run them.

There are a few ways to do this:

.. rst-class:: build

* ``$ python hello.py``   -- must be in current working directory
* ``$ python -m hello``   -- any module on PYTHONPATH anywhere on the system
* ``$ ./hello.py``        -- put ``#!/usr/env/python``  at top of module (Unix)
* ``In [149]: run hello.py``     -- at the IPython prompt -- running a module brings its names into the interactive namespace


.. nextslide:: Running a Module

Like importing, running a module executes all statements at the module level.

But there's an important difference.

When you *import* a module, the value of the symbol ``__name__`` in the module
is the same as the filename.

When you *run* a module, the value of the symbol ``__name__`` is ``__main__``.

This allows you to create blocks of code that are executed *only when you run a
module*

.. code-block:: python

    if __name__ == '__main__':
        # Do something interesting here
        # It will only happen when the module is run

.. nextslide:: "main" blocks

This is useful in a number of cases.

You can put code here that lets your module be a utility script

You can put code here that demonstrates the functions contained in your module

You can put code here that proves that your module works.

.. ifslides::

    [demo]


.. nextslide:: ``Assert``

Writing ``tests`` that demonstrate that your program works is an important part
of learning to program.

The python ``assert`` statement is useful in writing ``main`` blocks that test
your code.

.. code-block:: ipython

    In [1]: def add(n1, n2):
       ...:     return n1 + n2
       ...:

    In [2]: assert add(3, 4) == 7

    In [3]: assert add(3, 4) == 10
    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    <ipython-input-3-6731d4ac4476> in <module>()
    ----> 1 assert add(3, 4) == 10

    AssertionError:

In-Class Lab
============

Import Interactions

Exercises
---------

Experiment with importing different ways:

.. code-block:: ipython

    In [3]: import math

    In [4]: math.<TAB>
    math.acos       math.degrees    math.fsum       math.pi
    math.acosh      math.e          math.gamma      math.pow
    math.asin       math.erf        math.hypot      math.radians
    math.asinh      math.erfc       math.isinf      math.sin
    math.atan       math.exp        math.isnan      math.sinh
    math.atan2      math.expm1      math.ldexp      math.sqrt
    math.atanh      math.fabs       math.lgamma     math.tan
    math.ceil       math.factorial  math.log        math.tanh
    math.copysign   math.floor      math.log10      math.trunc
    math.cos        math.fmod       math.log1p
    math.cosh       math.frexp      math.modf

.. nextslide::

.. code-block:: ipython

    In [6]: math.sqrt(4)
    Out[6]: 2.0
    In [7]: import math as m
    In [8]: m.sqrt(4)
    Out[8]: 2.0
    In [9]: from math import sqrt
    In [10]: sqrt(4)
    Out[10]: 2.0


.. nextslide::

Experiment with importing different ways:

.. code-block:: python

    import sys
    print sys.path
    import os
    print os.path


You wouldn't want to import * those!

  -- check out

.. code-block:: python

    os.path.split('/foo/bar/baz.txt')
    os.path.join('/foo/bar', 'baz.txt')

Homework
========

You have two tasks to complete by next class:

Task 1
------

The Ackermann function, A(m, n), is defined::

    A(m, n) =
        n+1   if  m = 0
        A(m−1, 1)   if  m > 0  and  n = 0
        A(m−1, A(m, n−1))   if  m > 0  and  n > 0.

See http://en.wikipedia.org/wiki/Ackermann_function.

Create a new module called ``ack.py`` in a ``session02`` folder in your student folder. In that module, write a function named ``ack`` that performs Ackermann's function.

* Write a good ``docstring`` for your function according to PEP 257.
* Ackermann's function is not defined for input values less than 0.  Validate
  inputs to your function and return None if they are negative.

.. nextslide::

The wikipedia page provides a table of output values for inputs between 0 and
4. Using this table, add a ``if __name__ == "__main__":`` block to test your
function.

Test each pair of inputs between 0 and 4 and assert that the result produced by
your function is the result expected by the wikipedia table.

When your module is run from the command line, these tests should be executed.
If they all pass, print "All Tests Pass" as the result.

Add your new module to your git clone and commit frequently while working on
your implementation. Include good commit messages that explain concisely both
*what* you are doing and *why*.

When you are finished, push your changes to your fork of the class repository
in GitHub. Then make a pull request and submit your assignment in Canvas.

::

    - Adapted from "Think Python": Chapter 6, exercise 5.

Task 2
------

The `Fibonacci Series`_ is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us::

    0, 1, 1, 2, 3, 5, 8, 13, ...

Create a new module ``series.py`` in the ``session02`` folder in your student folder. In it, add a function called ``fibonacci``. The function should have one parameter ``n``. The function should return the ``nth`` value in the fibonacci series.

Ensure that your function has a well-formed ``docstring``

.. _Fibonacci Series: http://en.wikipedia.org/wiki/Fibbonaci_Series

.. nextslide::

The `Lucas Numbers`_ are a related series of integers that start with the
values 2 and 1 rather than 0 and 1. The resulting series looks like this::

    2, 1, 3, 4, 7, 11, 18, 29, ...

.. _Lucas Numbers: http://en.wikipedia.org/wiki/Lucas_number

In your ``series.py`` module, add a new function ``lucas`` that returns the
``nth`` value in the *lucas numbers*

Ensure that your function has a well-formed ``docstring``

.. nextslide::

Both the *fibonacci series* and the *lucas numbers* are based on an identical
formula.

Add a third function called ``sum_series`` with one required parameter and two
optional parameters. The required parameter will determine which element in the
series to print. The two optional parameters will have default values of 0 and
1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the
*fibonacci series*.  Calling it with the optional arguments 2 and 1 will
produce values from the *lucas numbers*. Other values for the optional
parameters will produce other series.

Ensure that your function has a well-formed ``docstring``

.. nextslide::

Add an ``if __name__ == "__main__":`` block to the end of your ``series.py``
module. Use the block to write a series of ``assert`` statements that
demonstrate that your three functions work properly.

Use comments in this block to inform the observer what your tests do.

Add your new module to your git clone and commit frequently while working on
your implementation. Include good commit messages that explain concisely both
*what* you are doing and *why*.

When you are finished, push your changes to your fork of the class repository
in GitHub. Then make a pull request and submit your assignment in Canvas.
