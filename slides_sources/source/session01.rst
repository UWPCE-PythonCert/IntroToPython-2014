.. include:: include.rst

**************************
Session One: Introductions
**************************

Introductions
=============

In which you are introduced to this class, your instructors, your environment,
and your new best friend, Python.

|

.. image:: /_static/python.png
    :align: center
    :width: 38%

.. rst-class:: credit

`xkcd.com/353`_

.. _xkcd.com/353: http://xkcd.com/353

Goals for Session One:
======================

* Meet each other, set expectations for the class.

* Schedule lightning talks.

* Get you all up and running with Python

* Start having fun with Python with a quick tutorial

Introductions
=============

.. rst-class:: center large

In which we meet each-other


Your instructors
----------------

.. rst-class:: center medium

| |instructor_1_name|
| |instructor_1_email|
|

.. nextslide::

.. rst-class:: center medium

| |instructor_2_name|
| |instructor_2_email|
|

Who are you?
-------------

.. rst-class:: center medium

  Tell us a tiny bit about yourself:

* name
* programming background: what languages have you used?
* neighbor's name
* neighbor's favorite coffee shop or bar


Introduction to This Class
==========================

.. rst-class:: center large

  Introduction to Python


Course Materials Online
-----------------------

A rendered HTML copy of the slides for this course may be found online at:

http://uwpce-pythoncert.github.io/IntroToPython

Also there are some exercise descriptions and supplemental materials.

The source of these materials are in the class gitHub repo:

https://github.com/UWPCE-PythonCert/IntroToPython

We also have a bunch of supplemental resources for the program here:

http://uwpce-pythoncert.github.io/PythonResources/index.html

The source for those is here:

https://github.com/UWPCE-PythonCert/PythonResources

Class Structure
---------------

Class Time:

 * Some lecture -- as little as possible
 * Lots of demos
 * Lab time: lots of hand-on practice
   - Take a break if you need one then...
 * Lather, Rinse, Repeat.....

Interrupt me with questions -- please!

(Some of the best learning prompted by questions)

Homework:
---------

* Homework will be reading, exercises, and the occasional Video

* Exercises will be started in class -- but you can finish them at home.

* You are adults -- it's up to you to do it

* You can do a gitHub "pull request" if you want us to review your work.

    - We'll show you how to do that in the second session


Communication
-------------

**Mailing list:**

We've set up a Google Group for this class:

programming-in-python@googlegroups.com

We will be using this list to communicate with you. You should have (or will soon) received an email invitation to join the mailing list.

Slack: We have set up a slack channel for discussions. Anything python related is fair game.

https://python2016fall.slack.com/

We highly encourage you to work together. You will learn at a much deeper level if you work together,
and it gets you ready to collaborate with colleagues.


Office Hours
------------

We will generally will hold "office hours" at a coffee shop for a couple hours
each weekend.

Please feel free to attend even if you do not have a specific question.
It is an opportunity to work with the instructors and fellow students,
and learn from each other.

What are good times for you?

And what locations?

Lightning Talks
----------------

**Lightning Talks:**

 * 5 minutes each (including setup) - no kidding!
 * Every student will give one
 * Purposes: introduce yourself, share interests, show Python applications
 * Any topic you like that is related to Python -- according to you!


Python Ecosystem
================

What is Python?
---------------

.. rst-class:: build

* Dynamic
* Object oriented
* Byte-compiled
* Interpreted

.. nextslide::

.. rst-class:: center large

But what does that mean?


Python Features
---------------

.. rst-class:: build

* Unlike C, C++, C\#, Java ... More like Ruby, Lisp, Perl, Javascript
  ...

* **Dynamic** -- no type declarations

  * Programs are shorter
  * Programs are more flexible
  * Less code means fewer bugs

* **Interpreted** -- no separate compile, build steps - programming process is
  simpler


What's a Dynamic language
-------------------------

**Dynamic typing**.

* Type checking and dispatch happen at run-time

.. code-block:: ipython

    In [1]: x = a + b

.. rst-class:: build

* What is ``a``?
* What is ``b``?
* What does it mean to add them?
* ``a`` and ``b`` can change at any time before this process

.. nextslide::

**Strong typing**.

.. code-block:: ipython

    In [1]: a = 5

    In [2]: type(a)
    Out[2]: int

    In [3]: b = '5'

    In [4]: type(b)
    Out[4]: str

.. rst-class:: build

* **everything** has a type.
* the *type* of a thing determines what it can do.

Duck Typing
-----------

.. rst-class:: center large

"If it looks like a duck, and quacks like a duck -- it's probably a duck"


.. nextslide::

.. rst-class:: center large

If an object behaves as expected at run-time, it's the right type.


Python Versions
---------------

Python 2.x

.. rst-class:: build

* "Classic" Python
* Evolved from original

Python 3.x ("py3k")

.. rst-class:: build

* Updated version
* Removed the "warts"
* Allowed to break code


.. nextslide::

This class uses Python 3 -- not Python 2

* Adoption of Python 3 is growing fast

  * Almost all key packages now supported (https://python3wos.appspot.com/)
  * But much code in the wild is still 2.x

* If you find yourself needing to work with Python 2 and 3, there are ways to write compatible code:

https://wiki.python.org/moin/PortingPythonToPy3k

* We will cover that more later in the program. Also: a short intro to the differences you really need to know about up front later this session.


Introduction to Your Environment
================================

There are three basic elements to your environment when working with Python:

.. rst-class:: left

.. rst-class:: build

* Your Command Line
* Your Interpreter
* Your Editor


Your Command Line (cli)
-----------------------

Having some facility on the command line is important

We won't cover this much in class, so if you are not comfortable,
please bone up at home.

We have some resources here: `PythonResources--command line <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/command_line.html>`_

**Windows:**

Most of the demos in class, etc, will be done using the "bash" command line shell on OS-X. This is identical to the bash shell on Linux.

Windows provides the "DOS" command line, which is OK, but pretty old and limited, or "Power Shell" -- a more modern, powerful, flexible command shell.

If you are comfortable with either of these -- go for it.

If not, you can use the "git Bash" shell -- which is much like the bash shell on OS-X and Linux. Or, on Windows 10, look into the "bash shell for Windows" otherwise known as the "Linux system" - - more info here: `PythonResources--Windows Bash  <http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/windows_bash.html>`_


LAB: Getting set up
-------------------

Before we move on -- we need to get all of us on the same page, with the tools we need for class.

You will find instructions for how to get python, etc, up and running on your machine here:

**Windows:**

http://uwpce-pythoncert.github.io/PythonResources/Installing/python_for_windows.html

**OS-X:**

http://uwpce-pythoncert.github.io/PythonResources/Installing/python_for_mac.html

**Linux:**

http://uwpce-pythoncert.github.io/PythonResources/Installing/python_for_linux.html

We'll run through some of that together.

If you already have a working environment, please feel free to help your neighbor or look at the Python Resources pages, particularly reviewing/learning the shell and git.

http://uwpce-pythoncert.github.io/PythonResources

Our Class Environment
---------------------

We are going to work from a common environment in this class.

We will take the time here in class to get this going.

This helps to ensure that you will be able to work.


Step 1: Python 3
------------------

.. rst-class:: medium

  Do you already have this??

.. code-block:: bash

  $ python
  Python 3.6.1 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

If not, or you have an older version -- let's install it!

If you're all ready to go -- take this time to get started on a tutorial:

http://uwpce-pythoncert.github.io/PythonResources/GeneralPython/learning.html#getting-started-tutorials


Step 2: Pip
-----------

Python comes with quite a bit ("batteries included").

Sometimes you need a bit more.

Pip allows you to install Python packages to expand your system.

The previous instructions include pip as well - make sure it's working.

Once you've installed pip, you use it to install Python packages by name:

.. code-block:: bash

    $ python -m pip install foobar
    ...

To find packages (and their proper names), you can search the python
package index (PyPI):

https://pypi.python.org/pypi


Step 3: Install iPython
------------------------

As this is an intro class, we are going to use almost entirely features
of the standard library. But there are a couple things you may want:

**iPython** is an "enhanced python shell" -- it make s it easier to work with python interactively.

.. code-block:: bash

  $ python -m pip install ipython[all]


Python in the Interpreter
-------------------------

Try it out:

.. code-block:: python

    >>> print("hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print ("one string" + " plus another")
    one string plus another
    >>>


.. nextslide:: Tools in the Interpreter

When you are in an interpreter, there are a number of tools available to
you.

There is a help system:

.. code-block:: python

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.

.. nextslide:: Tools in the Interpreter

You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: python

    >>> bob = "this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.


.. nextslide:: Advanced Interpreters

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

More on this soon.


Your Editor
-----------

Typing code in an interpreter is great for exploring.

But for anything "real", you'll want to save the work you are doing in a more permanent fashion.

This is where an Editor fits in.

.. nextslide:: Text Editors Only

Any good text editor will do.

MS Word is **not** a text editor.

Nor is *TextEdit* on a Mac.

``Notepad`` on Windows is a text editor -- but a crappy one.

You need a real "programmers text editor"

A text editor saves only what it shows you, with no special formatting
characters hidden behind the scenes.

.. nextslide:: Minimum Requirements

At a minimum, your editor should have:

.. rst-class:: build

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

.. rst-class:: build

* Tab completion
* Code linting

Have an editor that does all this? Feel free to use it.

If not, I suggest ``SublimeText``: http://www.sublimetext.com/

(Use version 3, even though it's "beta")

http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/sublime_as_ide.html

"Atom" is another good open source option.

And, of course, vi or Emacs on Linux, if you are familiar with those.

Why No IDE?
-----------

I am often asked this question.

An IDE does not give you much that you can't get with a good editor plus a good interpreter.

An IDE often weighs a great deal

Setting up IDEs to work with different projects can be challenging and time-consuming.

Particularly when you are first learning, you don't want too much done for you.

.. nextslide::

.. rst-class:: center large

YAGNI



Introduction to iPython
=======================

iPython Overview
------------------

You have installed `iPython`_.

iPython is an advanced Python interpreter that offers enhancements.

You can read more about it in the `official documentation`_.

Specifically, you'll want to pay attention to the information about

`Using iPython for Interactive Work`_.

.. _iPython: http://ipython.org
.. _official documentation: http://ipython.readthedocs.io/en/stable/
.. _Using iPython for Interactive Work: http://ipython.readthedocs.io/en/stable/interactive/index.html

.. ifslides::

    Let's see a quick demo of what it can do for you.


The very basics of iPython
--------------------------

iPython can do a lot for you, but for starters, here are the key pieces
you'll want to know:

Start it up

.. code-block:: bash

  $ ipython
  Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)
  Type "copyright", "credits" or "license" for more information.

  IPython 4.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.

.. ifslides::

    (live demo)


.. nextslide:: iPython basics

This is the stuff I use every day:

* command line recall:

  - hit the "up arrow" key
  - if you have typed a bit, it will find the last command that starts the same way.

* basic shell commands:

  - ``ls``, ``cd``, ``pwd``

* any shell command:

 - ``! the_shell_command``

* pasting from the clipboard:

  - ``%paste`` (this keeps whitespace cleaner for you)


.. nextslide:: iPython basics (cont)

* getting help:

  - ``something?``

* tab completion:

  - ``something.<tab>``

* running a python file:

  - ``run the_name_of_the_file.py``


That's it -- you can get a lot done with those.


How to run a python file
--------------------------

A file with python code in it is a 'module' or 'script'

(more on the distinction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

To run it, you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python the_name_of_the_script.py

2) On *nix (linux, OS-X, Windows bash), you can make the file "executable"::

       chmod +x the_file.py

   And make sur it has a "shebang" line at the top::

       #!/usr/bin/env python

   Then you can run it directly::

       ./the_file.py

3) run ``iPython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

.. ifslides::

    .. rst-class:: centered

        [demo]

Basic Python Syntax
===================

(Follow along in the iPython interpreter...)

.. rst-class:: center mlarge


| Values, Types, and Names
|
| Expressions and Statements


Values
------

All of programming is really about manipulating values.

* Values are pieces of unnamed data: ``42``, ``'Hello, world'``

* In Python, all values are objects

  - Try ``dir(42)``  - lots going on behind the curtain!

* Every value has a type

  - Try ``type(42)`` - the type of a value determines what it can do

.. ifslides::

    .. rst-class:: centered

        [demo]


Literals for the Basic Value types:
------------------------------------

Numbers:
  - floating point: ``3.4``
  - integers: ``456``

Text:
  -  ``"a bit of text"``
  -  ``'a bit of text'``
  - (either single or double quotes work -- why?)

Boolean values:
  -  ``True``
  -  ``False``

The nothing object:
  - ``None``

(There are intricacies to all of these that we'll get into later)

Code structure
--------------

Each line is a piece of code.

Comments:

.. code-block:: ipython

    In [3]: # everything after a '#' is a comment

Expressions:

.. code-block:: ipython

    In [4]: # evaluating an expression results in a value

    In [5]: 3 + 4
    Out[5]: 7

.. nextslide::

Statements:

.. code-block:: ipython

    In [6]: # statements do not return a value, may contain an expression

    In [7]: line_count = 42

    In [8]: return something


.. nextslide:: The Print Function

It's kind of obvious, but handy when playing with code:

.. code-block:: ipython

    In [1]: print("something")
    something

You can print multiple things:

.. code-block:: ipython

    In [2]: print("the value is", 5)
    the value is 5


.. nextslide::

Any python object can be printed (though it might not be pretty...)

.. code-block:: ipython

    In [1]: class bar(object):
       ...:     pass
       ...:

    In [2]: print(bar)
    <class '__main__.bar'>


.. nextslide:: Code Blocks

Blocks of code are delimited by a colon and indentation:

.. code-block:: python

    def a_function():
        a_new_code_block
    end_of_the_block

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    try:
        do_something_bad()
    except:
        fix_the_problem()

.. nextslide::

Python uses indentation to delineate structure.

This means that in Python, whitespace is **significant**.

(but **ONLY** for newlines and indentation)

The standard is to indent with **4 spaces**.

**SPACES ARE NOT TABS**

**TABS ARE NOT SPACES**


.. nextslide::

These two blocks look the same:

.. code-block:: python

    for i in range(100):
        print(i**2)

.. code-block:: python

    for i in range(100):
        print(i**2)


.. nextslide::

But they are not:

.. code-block:: python

    for i in range(100):
    \s\s\s\sprint i**2

.. code-block:: python

    for i in range(100):
    \tprint i**2

**ALWAYS INDENT WITH 4 SPACES**


.. nextslide::

.. rst-class:: center large

NEVER INDENT WITH TABS

Make sure your editor is set to use spaces only --

Even when you hit the <tab> key

[Python itself allows any number of spaces (and tabs), but you are just going to confuse yourself and others if you do anything else]

Expressions
------------

An *expression* is made up of values and operators.

.. rst-class:: build

* An expression is evaluated to produce a new value:  ``2 + 2``

  *  The Python interpreter can be used as a calculator to evaluate expressions

* Integer vs. float arithmetic

  * (Python 3 smooths this out)
  * Always use ``/`` when you want division with float results, ``//`` when you want floored (integer) results (no remainder).

* Type conversions

  * This is the source of many errors, especially in handling text

* Type errors - checked at run time only

.. ifslides::

    .. rst-class:: centered

        [demo]


Names
-------

Names are how we give names to values (objects) -- hence "names"

.. rst-class:: build

* Names must begin with an underscore or letter
* Names can contain any number of underscores, letters and numbers

  * this_is_a_name
  * this_is_2
  * _AsIsThis
  * 1butThisIsNot
  * nor-is-this

* Names don't have a type; values do

  * This is why python is "Dynamic"


Names and Type
----------------

Evaluating the type of a *name* will return the type of the *value* to which
it is bound.

.. code-block:: ipython

    In [19]: type(42)
    Out[19]: int

    In [20]: type(3.14)
    Out[20]: float

    In [21]: a = 42

    In [22]: b = 3.14

    In [23]: type(a)
    Out[23]: int

    In [25]: a = b

    In [26]: type(a)
    Out[26]: float

*wait!* a has a different type?!? -- yes, because it's the type of teh value: "3.14", names don't actually have a type, they can refer to any type.

Assignment
----------

A *name* is **bound** to a *value* with the assignment operator: ``=``

.. rst-class:: build

* This attaches a name to a value
* A value can have many names (or none!)
* Assignment is a statement, it returns no value

.. nextslide::

Evaluating the name will return the value to which it is bound

.. code-block:: ipython

    In [26]: name = "value"

    In [27]: name
    Out[27]: 'value'

    In [28]: an_integer = 42

    In [29]: an_integer
    Out[29]: 42

    In [30]: a_float = 3.14

    In [31]: a_float
    Out[31]: 3.14

Variables?
----------

.. rst-class:: build

* In most languages, what I'm calling names are called "variables".

* In fact, I'll probably call them variables in this class.

* That's because they are used, for the most part, for the same purposes.

* But often a "variable" is defined as something like:
  "a place in memory that can store values"

* That is **NOT** what a name in python is!

* A name can be bound to a value -- but that has nothing to do with a
  location in memory.

In-Place Assignment
-------------------

You can also do "in-place" assignment with ``+=``.

.. code-block:: ipython

    In [32]: a = 1

    In [33]: a
    Out[33]: 1

    In [34]: a = a + 1

    In [35]: a
    Out[35]: 2

    In [36]: a += 1

    In [37]: a
    Out[37]: 3

also: ``-=, *=, /=, **=, \%=``

(not quite -- really in-place assignment for mutables....)


Multiple Assignment
-------------------

You can assign multiple names from multiple expressions in one
statement

.. code-block:: ipython

    In [48]: x = 2

    In [49]: y = 5

    In [50]: i, j = 2 * x, 3 ** y

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243


Python evaluates all the expressions on the right before doing any assignments


Nifty Python Trick
------------------

Using this feature, we can swap values between two names in one statement:

.. code-block:: ipython

    In [51]: i
    Out[51]: 4

    In [52]: j
    Out[52]: 243

    In [53]: i, j = j, i

    In [54]: i
    Out[54]: 243

    In [55]: j
    Out[55]: 4

Multiple assignment and name swapping can be very useful in certain contexts

Deleting
--------

You can't actually directly delete values in python...

``del`` only deletes a name (or "unbinds" the name...)

.. code-block:: ipython

    In [56]: a = 5

    In [57]: b = a

    In [58]: del a

    In [59]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-59-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined

.. nextslide::

The object is still there...python will only delete it if there are no
references to it.

.. code-block:: ipython

    In [15]: a = 5

    In [16]: b = a

    In [17]: del a

    In [18]: a
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-18-60b725f10c9c> in <module>()
    ----> 1 a

    NameError: name 'a' is not defined

    In [19]: b
    Out[19]: 5


Identity
--------

Every value in Python is an object.

Every object is unique and has a unique *identity*, which you can inspect with
the ``id`` *builtin* function:

.. code-block:: ipython

    In [68]: id(i)
    Out[68]: 140553647890984

    In [69]: id(j)
    Out[69]: 140553647884864

    In [70]: new_i = i

    In [71]: id(new_i)
    Out[71]: 140553647890984


Testing Identity
----------------

You can find out if the values bound to two different names are the **same
object** using the ``is`` operator:

.. code-block:: ipython

    In [72]: count = 23

    In [73]: other_count = count

    In [74]: count is other_count
    Out[74]: True

    In [75]: count = 42

    In [76]: other_count is count
    Out[76]: False

.. ifslides::

    .. rst-class:: centered

        [demo]

**NOTE:** checking the id of an object, or using "is" to check if two objects are the same is rarely used except for debugging and understanding what's going on under the hood. They are not used regularly in production code.

Equality
--------

You can test for the equality of certain values with the ``==`` operator

.. code-block:: ipython

    In [77]: val1 = 20 + 30

    In [78]: val2 = 5 * 10

    In [79]: val1 == val2
    Out[79]: True

    In [80]: val3 = '50'

    In [81]: val1 == val3
    Out[84]: False

A string is never equal to a number!

.. ifslides::

    .. rst-class:: centered

        [demo]

For the numerical values, there is also::

    >, <, >=, <=, !=

Singletons
----------

Python has three "singletons" -- value fro which there is only one instance:

  ``True``, ``False``, and ``None``

To check if a name is bound to one of these, you use ``is``::

    a is True

    b is False

    x is None

Note that in contrast to english -- "is" is asking a question, not making an assertion -- ``a is True`` means "is a the True value?"

Operator Precedence
-------------------

Operator Precedence determines what evaluates first:

.. code-block:: python

    4 + 3 * 5 != (4 + 3) * 5

To force statements to be evaluated out of order, use parentheses -- expressions in parentheses are always evaluated first:

   (4 + 3) * 5 != 4 + (3 * 5)

Python follows the "usual" rules of algebra.

Python Operator Precedence
--------------------------

Parentheses and Literals:
  ``(), [], {}``

  ``"", b'', ''``

Function Calls:
  ``f(args)``

Slicing and Subscription:
  ``a[x:y]``

  ``b[0], c['key']``

Attribute Reference:
  ``obj.attribute``

.. nextslide::

Exponentiation:
  ``**``

Bitwise NOT, Unary Signing:
  ``~x``

  ``+x, -x``

Multiplication, Division, Modulus:
  ``*, /, %``

Addition, Subtraction:
  ``+, -``

.. nextslide::

Bitwise operations:
  ``<<, >>,``

  ``&, ^, |``

Comparisons:
  ``<, <=, >, >=, !=, ==``

Membership and Identity:
  ``in, not in, is, is not``

Boolean operations:
  ``or, and, not``

Anonymous Functions:
  ``lambda``


String Literals
---------------

A "string" is a chunk of text.

You define a "string" value by writing a string *literal*:

.. code-block:: ipython

    In [1]: 'a string'
    Out[1]: 'a string'

    In [2]: "also a string"
    Out[2]: 'also a string'

    In [3]: "a string with an apostrophe: isn't it cool?"
    Out[3]: "a string with an apostrophe: isn't it cool?"

    In [4]: 'a string with an embedded "quote"'
    Out[4]: 'a string with an embedded "quote"'


.. nextslide::

.. code-block:: ipython

    In [5]: """a multi-line
       ...: string
       ...: all in one
       ...: """
    Out[5]: 'a multi-line\nstring\nall in one\n'

    In [6]: "a string with an \n escaped character"
    Out[6]: 'a string with an \n escaped character'

    In [7]: r'a "raw" string, the \n comes through as a \n'
    Out[7]: 'a "raw" string, the \\n comes through as a \\n'

Python3 strings are fully support Unicode, which means that it can suport literally all the languages in the world (and then some -- Klingon, anyone?)

Because Unicode is native, you can get very far without even thinking about it. Anything you can type in your editor will work fine.


Keywords
--------

Python defines a number of **keywords**

These are language constructs.

You *cannot* use these words as names.

::

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try

.. nextslide::


If you try to use any of the keywords as names, you will cause a
``SyntaxError``:

.. code-block:: ipython

    In [13]: del = "this will raise an error"
      File "<ipython-input-13-c816927c2fb8>", line 1
        del = "this will raise an error"
            ^
    SyntaxError: invalid syntax

.. code-block:: ipython

    In [14]: def a_function(else='something'):
       ....:     print(else)
       ....:
      File "<ipython-input-14-1dbbea504a9e>", line 1
        def a_function(else='something'):
                          ^
    SyntaxError: invalid syntax


__builtins__
------------

Python also has a number of pre-bound names, called **builtins**

Try this:

.. code-block:: ipython

    In [6]: dir(__builtins__)
    Out[6]:
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BaseException',
     'BufferError',
     ...
     'vars',
     'xrange',
     'zip']

.. nextslide::

You are free to rebind these names:

.. code-block:: ipython

    In [15]: type('a new and exciting string')
    Out[15]: str

    In [16]: type = 'a slightly different string'

    In [17]: type('type is no longer what it was')
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-17-907616e55e2a> in <module>()
    ----> 1 type('type is no longer what it was')

    TypeError: 'str' object is not callable

In general, this is a **BAD IDEA** -- hopefully your editor will warn you.


Exceptions
----------

Notice that the first batch of ``__builtins__`` are all *Exceptions*

Exceptions are how Python tells you that something has gone wrong.

There are several exceptions that you are likely to see a lot of:

.. rst-class:: build

* ``NameError``: indicates that you have tried to use a name that is not bound to a value.

* ``TypeError``: indicates that you have tried to use the wrong kind of object for an operation.

* ``SyntaxError``: indicates that you have mis-typed something.

* ``AttributeError``: indicates that you have tried to access an attribute or
  method that an object does not have (this often means you have a different
  type of object than you expect)


Functions
---------

What is a function?

.. rst-class:: build

A function is a self-contained chunk of code

You use them when you need the same code to run multiple times,
or in multiple parts of the program.

(DRY) -- "Don't Repeat Yourself"

Or just to keep the code clean

Functions can take and return information

.. nextslide::

The minimal Function has at least one statement

.. code-block:: python

    def a_name():
        a_statement

.. nextslide::

Pass Statement does nothing (Note the indentation!)

.. code-block:: python

    def minimal():
        pass

This, or course, is not useful -- you will generally have multiple statements in a function.

Functions: ``def``
------------------

``def``  is a *statement*:

.. rst-class:: build

  * it is executed
  * it creates a local name
  * it does *not* return a value

.. nextslide::

function defs must be executed before the functions can be called:

.. code-block:: ipython

    In [23]: unbound()
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-23-3132459951e4> in <module>()
    ----> 1 unbound()

    NameError: name 'unbound' is not defined

.. code-block:: ipython

    In [18]: def simple():
       ....:     print("I am a simple function")
       ....:

    In [19]: simple()
    I am a simple function


Calling Functions
-----------------

You **call** a function using the function call operator (parens):

.. code-block:: ipython

    In [2]: type(simple)
    Out[2]: function

    In [3]: simple
    Out[3]: <function __main__.simple>

    In [4]: simple()
    I am a simple function

Calling a function is how you run the code in that function.


Functions: Call Stack
---------------------

functions can call other functions -- this makes an execution stack -- that's what a "trace back" is:

.. code-block:: ipython

    In [5]: def exceptional():
       ...:     print("I am exceptional!")
       ...:     print 1/0
       ...:
    In [6]: def passive():
       ...:     pass
       ...:
    In [7]: def doer():
       ...:     passive()
       ...:     exceptional()
       ...:

You've defined three functions, one of which will *call* the other two.


Functions: Tracebacks
---------------------

.. code-block:: ipython

    In [8]: doer()
    I am exceptional!
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-8-685a01a77340> in <module>()
    ----> 1 doer()

    <ipython-input-7-aaadfbdd293e> in doer()
          1 def doer():
          2     passive()
    ----> 3     exceptional()
          4

    <ipython-input-5-d8100c70edef> in exceptional()
          1 def exceptional():
          2     print("I am exceptional!")
    ----> 3     print(1/0)
          4

    ZeroDivisionError: integer division or modulo by zero

The error occurred in the ``doer`` function -- but the traceback shows you where that was called from. In a more complex system, this can be VERY useful -- learn to read tracebacks!

Functions: ``return``
---------------------

Every function ends by returning a value

This is actually the simplest possible function:

.. code-block:: python

    def fun():
        return None

.. nextslide::

if you don't explicitly put ``return``  there, Python will return None for you:

.. code-block:: ipython

    In [9]: def fun():
       ...:     pass
       ...:
    In [10]: fun()
    In [11]: result = fun()
    In [12]: print(result)
    None

note that the interpreter eats ``None`` -- you need to call ``print()`` to see it.


.. nextslide::

Only one return statement in a function will ever be executed.

Ever.

Anything after a executed return statement will never get run.

This is useful when debugging!

.. code-block:: ipython

    In [14]: def no_error():
       ....:     return 'done'
       ....:     # no more will happen
       ....:     print(1/0)
       ....:
    In [15]: no_error()
    Out[15]: 'done'


.. nextslide::

However, functions *can* return multiple results:

.. code-block:: ipython

    In [16]: def fun():
       ....:     return 1, 2, 3
       ....:
    In [17]: fun()
    Out[17]: (1, 2, 3)


.. nextslide::

Remember multiple assignment?

.. code-block:: ipython

    In [18]: x, y, z = fun()
    In [19]: x
    Out[19]: 1
    In [20]: y
    Out[20]: 2
    In [21]: z
    Out[21]: 3


Functions: parameters
---------------------

In a ``def`` statement, the values written *inside* the parens are
**parameters**

.. code-block:: ipython

    In [22]: def fun(x, y, z):
       ....:     q = x + y + z
       ....:     print(x, y, z, q)
       ....:

x, y, z are *local* names -- so is q


Functions: arguments
--------------------

When you call a function, you pass values to the function parameters as
**arguments**

.. code-block:: ipython

    In [23]: fun(3, 4, 5)
    3 4 5 12

The values you pass in are *bound* to the names inside the function and used.

The name used outside the object is separete from the name used inside teh function:

.. code-block:: python

    x = 5

    def fun(a):
        print(a)

    fun(x)

The "a" printed inside the function is the *same* object as the "x" outside the function.

The ``if`` Statement
---------------------

In order to do anything interesting at all, you need to be able to make a decision.

.. nextslide::

.. code-block:: ipython

    In [12]: def test(a):
       ....:     if a == 5:
       ....:         print("that's the value I'm looking for!")
       ....:     elif a == 7:
       ....:         print("that's an OK number")
       ....:     else:
       ....:         print("that number won't do!")

    In [13]: test(5)
    that's the value I'm looking for!

    In [14]: test(7)
    that's an OK number

    In [15]: test(14)
    that number won't do!

There is more to it than that, but this will get you started.


Enough For Now
--------------

That's it for our basic intro to Python

Before next session, you'll use what you've learned here today to do some
exercises in Python programming

Schedule the lightning talks:
-----------------------------

.. rst-class:: build

* We need to schedule your lightning talks.

* **Let's use Python for that !**

[demo]

Python 2-3 Differences
======================

Much of the example code you'll find online is Python2, rather than Python3

For the most part, they are the same -- so you can use those examples to learn from.

There are a lot of subtle differences that you don't need to concern yourself with just yet.

But a couple that you'll need to know right off the bat:

print()
-------

In python2, ``print`` is a "statement", rather than a function. That means it didn't require parentheses around what you want printed::

  print something, something_else

This made it a bit less flexible and powerful.

But -- if you try to use it that way in Python3, you'll get an error::

  In [15]: print "this"
    File "<ipython-input-15-70c8add5d16e>", line 1
      print "this"
                 ^
  SyntaxError: Missing parentheses in call to 'print'

So -- if you get this error, simply add the parentheses::

  In [16]: print ("this")
  this

.. nextslide:: division

In python 3, the division operator is "smart" when you divide integers::

  In [17]: 1 / 2
  Out[17]: 0.5

However in python2, integer division, will give you an integer result::

  In [1]: 1/2
  Out[1]: 0

In both versions, you can get "integer division" if you want it with a double slash::

  In [1]: 1//2
  Out[1]: 0

And in python2, you can get the behavior of py3 with "true division"::

  In [2]: from __future__ import division

  In [3]: 1/2
  Out[3]: 0.5

For the most part, you just need to be a bit careful with the rare cases where py2 code counts on integer division.

Other py2/py3 differences
-------------------------

Most of the other differences are essentially of implementation details, like getting iterators instead of sequences -- we'll talk about that more when it comes up in class.

There are also a few syntax differences with more advances topics: Exceptions, super(), etc.

We'll talk about all that when we cover those topics.


Homework
========

Tasks and reading by next week


Task 1
------

**Set Up a Great Dev Environment**

Make sure you have the basics of command line usage down:

Work through the supplemental tutorials on setting up your
Command Line (http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/shell.html) for good development support.

Make sure you've got your editor set up productively -- at the very very
least, make sure it does Python indentation and syntax coloring well.

.. nextslide::

**Advanced Editor Setup:**

If you are using SublimeText, here are some notes to make it super-nifty:

http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/sublime_as_ide.html

At the end, your editor should support tab completion and pep8 and pyflakes
linting.

If you are not using SublimeText, look for plugins that accomplish the same
goals for your own editor.  If none are available, please consider a change of
editor.

Also make sure you've got iPython working, if you didn't get to that in class.


Task 3
------

**Explore Errors**

* Create a new directory in your working dir for the class::

  $ mkdir session01
  $ cd session01

* Add a new file to it called ``break_me.py``

* In the ``break_me.py`` file write four simple Python functions:

  * Each function, when called, should cause an exception to happen

  * Each function should result in one of the four common exceptions from our
    lecture.

  * for review: ``NameError``, ``TypeError``, ``SyntaxError``, ``AttributeError``

(hint -- the interpreter will quit when it hits a Exception -- so you can comment out all but the one you are testing at the moment)

  * Use the Python standard library reference on `Built In Exceptions`_ as a
    reference

.. _Built In Exceptions: https://docs.python.org/3/library/exceptions.html

Task 2
------

**Python Pushups**

To get a bit of exercise solving some puzzles with Python, work on the Python
exercises at "Coding Bat": http://codingbat.com/python

There are 8 sets of puzzles. Do as many as you can, but try to at least
get all the "Warmups" done.


Reading, etc.
-------------

Every one of you has a different backgrond and learning style.

So take a bit of time to figure out which resource works for you.

http://uwpce-pythoncert.github.io/PythonResources/GeneralPython/learning.html

provides some options. Do look it over.

But here are few to get you started this week:

*Think Python:* Chapters 1–7 (http://greenteapress.com/wp/think-python-2e/)

*Dive Into Python:* Chapters 1–2 (http://www.diveintopython3.net/)

*LPTHW:* ex. 1–10, 18-21 (http://learnpythonthehardway.org/book/)

*NOTE:* LPTHW is python 2 -- you will need to add parentheses to all your print calls!

Or follow this excellent introductory tutorial:

https://www.youtube.com/watch?v=MirG-vJOg04

You should be comfortable with working with variables, numbers, strings, and basic functions.

git
---

We'll be covering the basics of git next week - enough to use for this class. Please read one of these so you'll have a head start:

http://rogerdudler.github.io/git-guide/

or

https://try.github.io/levels/1/challenges/1


Next Class
===========

Next week, we'll:

 * get set up with git and gitHub
 * Some more basic Python
 * More on Functions
 * Boolean Expressions
 * Code Structure, Modules, and Namespaces


Office Hours
------------

We will have office hours on either Saturday or Sunday from 10:00 to noon.

Preferences?

Locations?



