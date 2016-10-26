.. include:: include.rst

****************************************
Session Five: Exceptions, Comprehensions
****************************************

======================
Lightning Talks Today:
======================

.. rst-class:: medium

    Alexander C Truong

    Darryl Wong

    Madhumita Acharya

    Matthew T Weidner

================
Review/Questions
================

Review of Previous Class
------------------------

  * Dictionaries
  * Sets
  * File processing, etc.

.. nextslide::

.. rst-class:: center large

  How many of you finished ALL the homework?

.. nextslide::

.. rst-class:: center large

  Sorry about that!

.. nextslide::

.. rst-class:: medium

    * That was a lot.

.. rst-class:: medium

.. rst-class:: build

    * But it's all good stuff.

    * I'll take time to go over it in class.

    * And this week is a light load, so you can catch up.


Homework review
---------------

My Solutions to all the exercises in the class repo in:

``Solutions/Session04``

A few tidbits, then I'll take specific questions.


The count() method
------------------

All Python sequences (including strings) have a ``count()`` method:

.. code-block:: ipython

    In [1]: s = "This is an arbitrary string"

    In [2]: s.count('t')
    Out[2]: 2

What if you want a case-insensitive count?

.. code-block:: ipython

    In [3]: s.lower().count('t')
    Out[3]: 3



Sorting stuff in dictionaries:
-------------------------------

dicts aren't sorted, so what if you want to do something in a sorted way?

The "standard" way:

.. code-block:: python

  for key in sorted(d.keys()):
      ...

Another option:

.. code-block:: python

    collections.OrderedDict

Also other nifty stuff in the ``collections`` module:

https://docs.python.org/3.5/library/collections.html

Using files and "with"
-----------------------

Sorry for the confusion, but I'll be more clear now.

When working with files, unless you have a good reason not to, use ``with``:

.. code-block:: python

  with open(the_filename, 'w') as outfile:
      outfile.write(something)
      do_some_more...
  # now done with out file -- it will be closed, regardless of errors, etc.
  do_other_stuff

``with`` invokes a context manager -- which can be confusing, but for now,
just follow this pattern -- it really is more robust.

And you can even do two at once:

.. code-block:: python

    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())


Binary files
------------

Python can open files in one of two modes:

 * Text
 * Binary

This is just what you'd think -- if the file contains text, you want text mode. If the file contains arbitrary binary data, you want binary mode.

All data in all files is binary -- that's how computers work. So in Python3, "text" actually means Unicode -- which is a particular system for matching characters to binary data.

But this too is complicated -- there are multiple ways that binary data can be mapped to Unicode text, known as "encodings". In Python, text files are by default opened with the "utf-8" encoding. These days, that mostly "just works".

.. nextslide::

But if you read a binary file as text, then Python will try to interpret the bytes as utf-8 encoded text -- and this will likely fail:

.. code-block:: ipython

    In [13]: open("a_photo.jpg").read()
    ---------------------------------------------------------------------------
    UnicodeDecodeError                        Traceback (most recent call last)
    <ipython-input-13-5c699bc20e80> in <module>()
    ----> 1 open("PassportPhoto.JPG").read()

    /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/codecs.py in decode(self, input, final)
        319         # decode input (taking the buffer into account)
        320         data = self.buffer + input
    --> 321         (result, consumed) = self._buffer_decode(data, self.errors, final)
        322         # keep undecoded input until the next call
        323         self.buffer = data[consumed:]

    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

.. nextslide::

In Python2, it's less likely that you'll get an error like this -- it doesn't try to decode the file as it's read -- even for text files -- so it's a bit tricky and more error prone.

**NOTE:** If you want to actually DO anything with a binary file, other than passing it around, then you'll need to know a lot about how the details of what the bytes in the file mean -- and most likely, you'll use a library for that -- like an image processing library for the jpeg example above.


PEP 8 reminder
--------------

PEP 8 (Python Enhancement Proposal 8): https://www.python.org/dev/peps/pep-0008/

Is the "official" style guide for Python code.

Strictly speaking, you only need to follow it for code in the standard library.

But style matters -- consistent style makes your code easier to read and understand.

So **follow PEP 8**

**Exception:** if you have a company style guide -- follow that instead.

Try the "pycodestyle" module on your code::

  $ python3 -m pip install pycodestyle
  $ pycodestyle my_python_file

(demo)

Naming things...
----------------

It matters what names you give your variables.

Python has rules about what it *allows*

PEP8 has rules for style: capitalization, and underscores and all that.

But you still get to decide within those rules.

So use names that make sense to the reader.

Naming Guidelines
-----------------

Only use single-letter names for things with limited scope: indexes and the like:

.. code-block:: python

    for i, item in enumerate(a_sequence):
        do_something(i, item)

**Don't** use a name like "item", when there is a meaning to what the item is:

.. code-block:: python

    for name in all_the_names:
        do_something_with(name)

Use plurals for collections of things:

.. code-block:: python

    names = ['Fred', 'George', ...]

.. nextslide::

**Do** re-use names when the use is essentially the same, and you don't need the old one:

.. code-block:: python

    line = line.strip()
    line = line.replace(",", " ")
    ....

Here's a nice talk about naming:

http://pyvideo.org/video/3792/name-things-once-0


Code Review
------------

.. rst-class:: center medium

Anyone stuck or confused that's willing to volunteer for a live code review?

My Solutions
-------------

Anyone look at my solutions?

(yeah, not much time for that...)

Anything in particular you'd like me to go over?

Lightning Talks
----------------

.. rst-class:: medium

|
| Alexander C Truong
|
|
| Darryl Wong
|

==========
Exceptions
==========

A really nifty python feature -- really handy!

Exceptions
----------

Another Branching structure:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")

Exceptions
----------

Never Do this:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except:
        print "couldn't open missing.txt"

**always** capture the *particular* Exception you know how to handle.


Exceptions
----------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)

It will almost always work -- but the almost will drive you crazy

.. nextslide::

Example from homework

.. code-block:: python

    if num_in.isdigit():
        num_in = int(num_in)

but -- ``int(num_in)`` will only work if the string can be converted to an integer.

So you can do

.. code-block:: python

    try:
        num_in = int(num_in)
    except ValueError:
        print("Input must be an integer, try again.")

Or let the Exception be raised....


EAFP
----


"it's Easier to Ask Forgiveness than Permission"

 -- Grace Hopper


http://www.youtube.com/watch?v=AZDWveIdqjY

(PyCon talk by Alex Martelli)


.. nextslide:: Do you catch all Exceptions?

For simple scripts, let exceptions happen.

Only handle the exception if the code can and will do something about it.

(much better debugging info when an error does occur)


Exceptions -- finally
---------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print("couldn't open missing.txt")
    finally:
        do_some_clean-up

The ``finally:``  clause will always run


Exceptions -- else
-------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError:
        print("couldn't open missing.txt")
    else:
        process(f) # only called if there was no exception

Advantage:

you know where the Exception came from

Exceptions -- using them
------------------------

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
    except IOError as the_error:
        print(the_error)
        the_error.extra_info = "some more information"
        raise


Particularly useful if you catch more than one exception:

.. code-block:: python

    except (IOError, BufferError, OSError) as the_error:
        do_something_with (the_error)


Raising Exceptions
-------------------

.. code-block:: python

    def divide(a,b):
        if b == 0:
            raise ZeroDivisionError("b can not be zero")
        else:
            return a / b


when you call it:

.. code-block:: ipython

    In [515]: divide (12,0)
    ZeroDivisionError: b can not be zero


Built in Exceptions
-------------------

You can create your own custom exceptions

But...

.. code-block:: python

    exp = \
     [name for name in dir(__builtin__) if "Error" in name]
    len(exp)
    32


For the most part, you can/should use a built in one

.. nextslide::

Choose the best match you can for the built in Exception you raise.

Example (from last week's exercises)::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise ValueError

Is it the *value* or the input the problem here?

Nope: the *type* is the problem::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise TypeError

but should you be checking type anyway? (EAFP)

===
LAB
===

Exceptions Lab:


:ref:`exercise_exceptions_lab`


Lightning Talks
---------------

.. rst-class:: medium

|
| Madhumita Acharya
|
| Matthew T Weidner



============================
List and Dict Comprehensions
============================

List comprehensions
-------------------

A bit of functional programming

consider this common ``for`` loop structure:

.. code-block:: python

    new_list = []
    for variable in a_list:
        new_list.append(expression)

This can be expressed with a single line using a "list comprehension"

.. code-block:: python

    new_list = [expression for variable in a_list]


.. nextslide::

What about nested for loops?

.. code-block:: python

    new_list = []
    for var in a_list:
        for var2 in a_list2:
            new_list.append(expression)

Can also be expressed in one line:

.. code-block:: python

    new_list =  [exp for var in a_list for var2 in a_list2]

You get the "outer product", i.e. all combinations.

(demo)

.. nextslide::

But usually you at least have a conditional in the loop:

.. code-block:: python

    new_list = []
    for variable in a_list:
        if something_is_true:
            new_list.append(expression)

You can add a conditional to the comprehension:

.. code-block:: python

    new_list = [expr for var in a_list if something_is_true]


(demo)

.. nextslide::

Examples:

.. code-block:: ipython

    In [341]: [x**2 for x in range(3)]
    Out[341]: [0, 1, 4]

    In [342]: [x+y for x in range(3) for y in range(5,7)]
    Out[342]: [5, 6, 6, 7, 7, 8]

    In [343]: [x*2 for x in range(6) if not x%2]
    Out[343]: [0, 4, 8]



.. nextslide::

Remember this from earlier today?

.. code-block:: python

    [name for name in dir(__builtin__) if "Error" in name]
    ['ArithmeticError',
     'AssertionError',
     'AttributeError',
     'BufferError',
     'EOFError',
     ....


Set Comprehensions
------------------

You can do it with sets, too:

.. code-block:: python

    new_set = { value for variable in a_sequence }


same as for loop:

.. code-block:: python

    new_set = set()
    for key in a_list:
        new_set.add(value)


.. nextslide::

Example: finding all the vowels in a string...

.. code-block:: ipython

    In [19]: s = "a not very long string"

    In [20]: vowels = set('aeiou')

    In [21]: { l for l in s if l in vowels }
    Out[21]: {'a', 'e', 'i', 'o'}

Side note: why did I do ``set('aeiou')`` rather than just `aeiou` ?


Dict Comprehensions
-------------------

Also with dictionaries

.. code-block:: python

    new_dict = { key:value for variable in a_sequence}


same as for loop:

.. code-block:: python

    new_dict = {}
    for key in a_list:
        new_dict[key] = value



.. nextslide::

Example

.. code-block:: ipython

    In [22]: { i: "this_%i"%i for i in range(5) }
    Out[22]: {0: 'this_0', 1: 'this_1', 2: 'this_2',
              3: 'this_3', 4: 'this_4'}


(not as useful with the ``dict()``  constructor...)

===
LAB
===

List comps exercises:

:ref:`exercise_comprehensions`





=========
Homework
=========

Catch up!
---------

* Finish the LABs from today
  - Exceptions lab

* Catch up from last week.

  - Add Exception handling to mailroom
  - and list (and dict, and set) comprehensions...

* If you've done all that -- check out the collections module:

  - https://docs.python.org/3.5/library/collections.html
  - here's a good overview: https://pymotw.com/3/collections/

====================================
Material to review before next week:
====================================

Advanced Argument Passing:

https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

Lambda:

http://www.blog.pythonlibrary.org/2015/10/28/python-101-lambda-basics/
https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/
