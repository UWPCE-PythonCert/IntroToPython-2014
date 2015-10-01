
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.


******************************************************************
Session Nine: Decorators, Context Managers, Packages and packaging
******************************************************************

======================
Lightning Talks Today:
======================

.. rst-class:: medium

  Lou Ascoli

  Ralph  Brand

  Danielle Marcos

  Carolyn  Evans

================
Review/Questions
================

Review of complete sparse array class

==========
Decorators
==========

**A Short Reminder**

.. rst-class:: left
.. container::

    Functions are things that generate values based on input (arguments).

    In Python, functions are first-class objects.

    This means that you can bind symbols to them, pass them around, just like
    other objects.

    Because of this fact, you can write functions that take functions as
    arguments and/or return functions as values:

    .. code-block:: python

        def substitute(a_function):
            def new_function(*args, **kwargs):
                return "I'm not that other function"
            return new_function

A Definition
------------

There are many things you can do with a simple pattern like this one.
So many, that we give it a special name:

.. rst-class:: centered medium

**Decorator**

.. rst-class:: build centered
.. container::

    "A decorator is a function that takes a function as an argument and
    returns a function as a return value.""

    That's nice and all, but why is that useful?

An Example
----------

Imagine you are trying to debug a module with a number of functions like this
one:

.. code-block:: python

    def add(a, b):
        return a + b

.. rst-class:: build
.. container::

    You want to see when each function is called, with what arguments and
    with what result. So you rewrite each function as follows:

    .. code-block:: python

        def add(a, b):
            print "Function 'add' called with args: %r, %r"%(a, b)
            result = a + b
            print "\tResult --> %r" % result
            return result

.. nextslide::

That's not particularly nice, especially if you have lots of functions
in your module.

Now imagine we defined the following, more generic *decorator*:

.. code-block:: python

    def logged_func(func):
        def logged(*args, **kwargs):
            print "Function %r called" % func.__name__
            if args:
                print "\twith args: %r" % args
            if kwargs:
                print "\twith kwargs: %r" % kwargs
            result = func(*args, **kwargs)
            print "\t Result --> %r" % result
            return result
        return logged

.. nextslide::

We could then make logging versions of our module functions:

.. code-block:: python

    logging_add = logged_func(add)

Then, where we want to see the results, we can use the logged version:

.. code-block:: ipython

    In [37]: logging_add(3, 4)
    Function 'add' called
        with args: (3, 4)
         Result --> 7
    Out[37]: 7

.. rst-class:: build
.. container::

    This is nice, but we have to call the new function wherever we originally
    had the old one.

    It'd be nicer if we could just call the old function and have it log.

.. nextslide::

Remembering that you can easily rebind symbols in Python using *assignment
statements* leads you to this form:

.. code-block:: python

    def logged_func(func):
        # implemented above

    def add(a, b):
        return a + b
    add = logged_func(add)

.. rst-class:: build
.. container::

    And now you can simply use the code you've already written and calls to
    ``add`` will be logged:

    .. code-block:: ipython

        In [41]: add(3, 4)
        Function 'add' called
            with args: (3, 4)
             Result --> 7
        Out[41]: 7

Syntax
------

Rebinding the name of a function to the result of calling a decorator on that
function is called **decoration**.

Because this is so common, Python provides a special operator to perform it
more *declaratively*: the ``@`` operator:

(I told you I'd eventually explain what was going on under the hood
with that wierd `@` symbol)

.. code-block:: python

    # this is the imperative version:
    def add(a, b):
        return a + b
    add = logged_func(add)

    # and this declarative form is exactly equal:
    @logged_func
    def add(a, b):
        return a + b

.. rst-class:: build
.. container::

    The declarative form (called a decorator expression) is far more common,
    but both have the identical result, and can be used interchangeably.

Callables
---------

Our original definition of a *decorator* was nice and simple, but a tiny bit
incomplete.

In reality, decorators can be used with anything that is *callable*.

Remember from last week, a *callable* is a function, a method on a class,
or a class that implements the ``__call__`` special method.

So in fact the definition should be updated as follows:

.. rst-class:: centered

A decorator is a callable that takes a callable as an argument and
returns a callable as a return value.

An Example
----------

Consider a decorator that would save the results of calling an expensive
function with given arguments:

.. code-block:: python

    class Memoize:
    """
    memoize decorator from avinash.vora
    http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    """
    def __init__(self, function):  # runs when memoize class is called
        self.function = function
        self.memoized = {}

    def __call__(self, *args):  # runs when memoize instance is called
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

.. nextslide::

Let's try that out with a potentially expensive function:

.. code-block:: ipython

    In [56]: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in xrange(n))
       ....:

    In [57]: sum2x(10000000)
    Out[57]: 99999990000000

    In [58]: sum2x(10000000)
    Out[58]: 99999990000000

It's nice to see that in action, but what if we want to know *exactly* how much
difference it made?

Nested Decorators
-----------------

You can stack decorator expressions.  The result is like calling each decorator
in order, from bottom to top:

.. code-block:: python

    @decorator_two
    @decorator_one
    def func(x):
        pass

    # is exactly equal to:
    def func(x):
        pass
    func = decorator_two(decorator_one(func))

.. nextslide::

Let's define another decorator that will time how long a given call takes:

.. code-block:: python

    import time
    def timed_func(func):
        def timed(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print "time expired: %s" % elapsed
            return result
        return timed

.. nextslide::

And now we can use this new decorator stacked along with our memoizing
decorator:

.. code-block:: ipython

    In [71]: @timed_func
       ....: @Memoize
       ....: def sum2x(n):
       ....:     return sum(2 * i for i in xrange(n))
    In [72]: sum2x(10000000)
    time expired: 0.997071027756
    Out[72]: 99999990000000
    In [73]: sum2x(10000000)
    time expired: 4.05311584473e-06
    Out[73]: 99999990000000


Examples from the Standard Library
----------------------------------

It's going to be a lot more common for you to use pre-defined decorators than
for you to be writing your own.

We've seen a few already:

.. nextslide::

For example, ``@staticmethod`` and ``@classmethod`` can also be used as simple
callables, without the nifty decorator expression:

.. code-block:: python

    # the way we saw last week:
    class C(object):
        @staticmethod
        def add(a, b):
            return a + b

Is exactly the same as:

.. code-block:: python

    class C(object):
        def add(a, b):
            return a + b
        add = staticmethod(add)

Note that the "``def``" binds the name ``add``, then the next line
rebinds it.


.. nextslide::

The ``classmethod()`` builtin can do the same thing:

.. code-block:: python

    # in declarative style
    class C(object):
        @classmethod
        def from_iterable(cls, seq):
            # method body

    # in imperative style:
    class C(object):
        def from_iterable(cls, seq):
            # method body
        from_iterable = classmethod(from_iterable)


property()
-----------

Remember the property() built in?

Perhaps most commonly, you'll see the ``property()`` builtin used this way.

Last week we saw this code:

.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        @property
        def x(self):
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x

.. nextslide::

But this could also be accomplished like so:

.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        def getx(self):
            return self._x
        def setx(self, value):
            self._x = value
        def delx(self):
            del self._x
        x = property(getx, setx, delx,
                     "I'm the 'x' property.")

.. nextslide::

Note that in this case, the decorator object returned by the property decorator
itself implements additional decorators as attributes on the returned method
object. So you could actually do this:



.. code-block:: python

    class C(object):
        def __init__(self):
            self._x = None
        def x(self):
            return self._x
        x = property(x)
        def _set_x(self, value):
            self._x = value
        x = x.setter(_set_x)
        def _del_x(self):
            del self._x
        x = x.deleter(_del_x)

But that's getting really ugly!

LAB
----

**p_wrapper Decorator**

Write a simple decorator you can apply to a function that returns a string.

Decorating such a function should result in the original output, wrapped by an
HTML 'p' tag:

.. code-block:: ipython

    In [4]: @p_wrapper
       ...: def return_a_string(string):
       ...:     return string
       ...:

    In [5]: return_a_string("this is a string")
    Out[5]: '<p> this is a string </p>'

simple test code in
:download:`Examples/Session09/test_p_wrapper.py <../../Examples/Session09/test_p_wrapper.py>`


Lightning Talks
----------------

.. rst-class:: medium

|
|  Lou Ascoli
|
|  Ralph  Brand
|


=================
Context Managers
=================

**A Short Digression**

.. rst-class:: left build
.. container::

    Repetition in code stinks (DRY!)

    A large source of repetition in code deals with the handling of external
    resources.

    As an example, how many times do you think you might type the following
    code:

    .. code-block:: python

        file_handle = open('filename.txt', 'r')
        file_content = file_handle.read()
        file_handle.close()
        # do some stuff with the contents

    What happens if you forget to call ``.close()``?

    What happens if reading the file raises an exception?


Resource Handling
-----------------

Leaving an open file handle laying around is bad enough. What if the resource
is a network connection, or a database cursor?

You can write more robust code for handling your resources:

.. code-block:: python

    try:
        file_handle = open('filename.txt', 'r')
        file_content = file_handle.read()
    finally:
        file_handle.close()
    # do something with file_content here

But what exceptions do you want to catch?  And do you really want to have to
remember to type all that **every** time you open a resource?

.. nextslide:: It Gets Better

Starting in version 2.5, Python provides a structure for reducing the
repetition needed to handle resources like this.

.. rst-class:: centered

**Context Managers**

You can encapsulate the setup, error handling and teardown of resources in a
few simple steps.

The key is to use the ``with`` statement.

.. nextslide:: ``with`` a little help

Since the introduction of the ``with`` statement in `pep343`_, the above six
lines of defensive code have been replaced with this simple form:

.. code-block:: python

    with open('filename', 'r') as file_handle:
        file_content = file_handle.read()
    # do something with file_content

``open`` builtin is defined as a *context manager*.

The resource it returnes (``file_handle``) is automatically and reliably closed
when the code block ends.

.. _pep343: http://legacy.python.org/dev/peps/pep-0343/

.. nextslide:: A Growing Trend

At this point in Python history, many functions you might expect to behave this
way do:

* ``open`` and ``io.open`` both work as context managers.
  (``io.open`` is good for working with unicode)
* networks connections via ``socket`` do as well.
* most implementations of database wrappers can open connections or cursors as
  context managers.
* ...

* But what if you are working with a library that doesn't support this
  (``urllib``)?

.. nextslide:: Close It Automatically

There are a couple of ways you can go.

If the resource in questions has a ``.close()`` method, then you can simply use
the ``closing`` context manager from ``contextlib`` to handle the issue:

.. code-block:: python

    import urllib
    from contextlib import closing

    with closing(urllib.urlopen('http://google.com')) as web_connection:
        # do something with the open resource
    # and here, it will be closed automatically

But what if the thing doesn't have a ``close()`` method, or you're creating
the thing and it shouldn't have a close() method?

Do It Yourself
----------------

You can also define a context manager of your own.

The interface is simple.  It must be a class that implements two
more of the nifty python *special methods*

**__enter__(self)**  Called when the ``with`` statement is run, it should return something to work with in the created context.

**__exit__(self, e_type, e_val, e_traceback)**  Clean-up that needs to happen is implemented here.

The arguments will be the exception raised in the context.

If the exception will be handled here, return True. If not, return False.

Let's see this in action to get a sense of what happens.

An Example
----------

Consider this code:

.. code-block:: python

    class Context(object):
    """from Doug Hellmann, PyMOTW
    http://pymotw.com/2/contextlib/#module-contextlib
    """
    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__(%r, %r, %r)' % (exc_type, exc_val, exc_tb)
        return self.handle_error

:download:`Examples/Session09/context_managers.py <../../Examples/Session09/context_managers.py>`


.. nextslide::

This class doesn't do much of anything, but playing with it can help
clarify the order in which things happen:

.. code-block:: ipython

    In [46]: with Context(True) as foo:
       ....:     print 'This is in the context'
       ....:     raise RuntimeError('this is the error message')
    __init__(True)
    __enter__()
    This is in the context
    __exit__(<type 'exceptions.RuntimeError'>, this is the error message, <traceback object at 0x1049cca28>)

.. rst-class:: build
.. container::

    Because the exit method returns True, the raised error is 'handled'.

.. nextslide::

What if we try with ``False``?

.. code-block:: ipython

    In [47]: with Context(False) as foo:
       ....:     print 'This is in the context'
       ....:     raise RuntimeError('this is the error message')
    __init__(False)
    __enter__()
    This is in the context
    __exit__(<type 'exceptions.RuntimeError'>, this is the error message, <traceback object at 0x1049ccb90>)
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    <ipython-input-47-de2c0c873dfc> in <module>()
          1 with Context(False) as foo:
          2     print 'This is in the context'
    ----> 3     raise RuntimeError('this is the error message')
          4
    RuntimeError: this is the error message

.. nextslide:: ``contextmanager`` decorator

``contextlib.contextmanager`` turns generator functions into context managers.
Consider this code:

.. code-block:: python

    from contextlib import contextmanager

    @contextmanager
    def context(boolean):
        print "__init__ code here"
        try:
            print "__enter__ code goes here"
            yield object()
        except Exception as e:
            print "errors handled here"
            if not boolean:
                raise
        finally:
            print "__exit__ cleanup goes here"

.. nextslide::

The code is similar to the class defined previously.

And using it has similar results.  We can handle errors:

.. code-block:: ipython

    In [50]: with context(True):
       ....:     print "in the context"
       ....:     raise RuntimeError("error raised")
    __init__ code here
    __enter__ code goes here
    in the context
    errors handled here
    __exit__ cleanup goes here

.. nextslide::

Or, we can allow them to propagate:

.. code-block:: ipython

    In [51]: with context(False):
       ....: print "in the context"
       ....: raise RuntimeError("error raised")
    __init__ code here
    __enter__ code goes here
    in the context
    errors handled here
    __exit__ cleanup goes here
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    <ipython-input-51-641528ffa695> in <module>()
          1 with context(False):
          2     print "in the context"
    ----> 3     raise RuntimeError("error raised")
          4
    RuntimeError: error raised


LAB
----
**Timing Context Manager**

Create a context manager that will print the elapsed time taken to
run all the code inside the context:

.. code-block:: ipython

    In [3]: with Timer() as t:
       ...:     for i in range(100000):
       ...:         i = i ** 20
       ...:
    this code took 0.206805 seconds

**Extra Credit**: allow the ``Timer`` context manager to take a file-like
object as an argument (the default should be sys.stdout). The results of the
timing should be printed to the file-like object.


Lightning Talks
----------------

.. rst-class:: medium

|
|  Danielle Marcos
|
|  Carolyn Evans
|


======================
Packages and Packaging
======================

Modules and Packages
--------------------

A module is a file (``something.py``) with python code in it

A package is a directory with an ``__init__.py``  file in it

And usually other modules, packages, etc...

::

    my_package
        __init__.py
        module_a.py
        module_b.py


.. code-block:: python

    import my_package


runs the code ``my_package/__init__.py`` (if there is any)

Modules and Packages
--------------------

.. code-block:: python

    import sys
    for p in sys.path:
        print p

(demo)

Installing Python
-----------------

Linux:

Usually part of the system -- just use it.

Windows:

Use the python.org version:

* System Wide

* Can install multiple versions if need be

* Third party binaries for it.

Installing Python
-----------------
OS-X:

Comes with the system, but:

    * Apple has never upgraded within a release
    * There are non-open source components
    * Third party packages may or may not support it
    * Apple does use it -- so don't mess with it
    * I usually recommend the ``python.org`` version

(Also Macports, Fink, Home Brew...)


Distributions
-------------

There are also a few "curated" distributions:

These provide python and a package management system for hard-to-buid packages.

Widely used by the scipy community
(lots of hard to build stuff that needs to work together...)

  * Anaconda (https://store.continuum.io/cshop/anaconda/)
  * Canopy (https://www.enthought.com/products/canopy/)
  * ActivePython (http://www.activestate.com/activepython)


Installing Packages
-------------------
Every Python installation has its own stdlib and ``site-packages`` folder

``site-packages``  is the default place for third-party packages

Finding Packages
----------------
The Python Package Index:

**PyPi**

http://pypi.python.org/pypi

Installing Packages
-------------------
.. rst-class:: medium

    **From source**

* (``setup.py install`` )

* With the system installer (apt-get, yum, etc...)

.. rst-class:: medium

    **From binaries:**

* Windows: MSI installers

* OS-X: dmg installers (make sure to get compatible packages)

* And now: binary wheels -- (More and more of those available)

* ``pip`` should find appropriate binary wheels if they are there.


.. nextslide::

In the beginning, there was the ``distutils``:

But ``distutils``  is missing some key features:

* package versioning
* package discovery
* auto-install

- And then came ``PyPi``

- And then came ``setuptools``

- But that wasn't well maintained...

- Then there was ``distribute/pip``

- Which has now been merged back into ``setuptools``

Now it's pretty stable: pip+setuptools: use them.

Installing Packages
-------------------

Actually, it's still a bit of a mess

But getting better, and the mess is *almost* cleaned up.

Current State of Packaging
--------------------------

To build packages: distutils

  * http://docs.python.org/2/distutils/

For more features: setuptools

  * https://pythonhosted.org/setuptools/

To install packages: pip

  * https://pip.pypa.io/en/latest/installing.html

For binary packages: wheels

  * http://www.python.org/dev/peps/pep-0427/

(installable by pip)

Compiled Packages
-----------------

Biggest issue is with compiled extensions:

  * (C/C++, Fortran, etc.)

  * You need the right compiler set up

Dependencies:

  * Here's were it gets really ugly

  * Particularly on Windows

.. nextslide::

**Linux**

Pretty straightforward:

1. Is there a system package?

  * use it (apt-get install the_package)

2. Try ``pip install``: it may just work!

3. Install the dependencies, build from source::

    python setup.py build

    python setup.py install

(may need "something-devel" packages)


.. nextslide::

**Windows**

Sometimes simpler:

1) A lot of packages have Windows binaries:

  - Usually for python.org builds
  - Excellent source: http://www.lfd.uci.edu/~gohlke/pythonlibs/
  - Make sure you get 32 or 64 bit consistent

2) But if no binaries:

  - Hope the dependencies are available!
  - Set up the compiler

MS now has a compiler just for python!

http://www.microsoft.com/en-us/download/details.aspx?id=44266

.. nextslide::

**OS-X**

Lots of Python versions:
  - Apple's built-in (different for each version of OS)
  - python.org builds
  - 32+64 bit Intel (and even PPC still kicking around)
  - Macports
  - Homebrew

Binary Installers (dmg or wheel) have to match python version

.. nextslide::

**OS-X**

If you have to build it yourself

Xcode compiler (the right version)

  - Version 3.* for 32 bit PPC+Intel

  - Version > 4.* for 32+64 bit Intel

(make sure to get the SDKs for older versions)

If extra dependencies:

  - macports or homebrew often easiest way to build them


Final Recommendations
---------------------

First try: ``pip install``

If that doesn't work:

Read the docs of the package you want to install

Do what they say

(Or use Anaconda or Canopy)

virtualenv
----------

``virtualenv`` is a tool to create isolated Python environments.

Very useful for developing multiple apps

Or deploying more than one app on one system

http://www.virtualenv.org/en/latest/index.html}

Remember the notes from the beginning of class? :ref:`virtualenv_section`

(Cris will probably make you do this next class)

============
Distributing
============

Distributing
------------
What if you need to distribute you own:

Scripts

Libraries

Applications


Scripts
-------

Often you can just copy, share, or check in the script to source
control and call it good.

But only if it's a single file, and doesn't need anything non-standard

When the script needs more than just the stdlib

(or your company standard environment)

You have an application, not a script


Libraries
---------

When you read the distutils docs, it's usually libraries they're talking about

Scripts + library is the same...

(http://docs.python.org/distutils/)

distutils
---------

``distutils``  makes it easy to do the easy stuff:

Distribute and install to multiple platforms, etc.

Even binaries, installers and compiled packages

(Except dependencies)

(http://docs.python.org/distutils/)

distutils basics
----------------

It's all in the ``setup.py file``:

.. code-block::python

    from distutils.core import setup
    setup(name='Distutils',
          version='1.0',
          description='Python Distribution Utilities',
          author='Greg Ward',
          author_email='gward@python.net',
          url='http://www.python.org/sigs/distutils-sig/',
          packages=['distutils', 'distutils.command'],
         )

(http://docs.python.org/distutils/)

distutils basics
----------------

Once your setup.py is written, you can:

::

    python setup.py ...
    build         build everything needed to install
    install       install everything from build directory
    sdist         create a source distribution
                  (tarball, zip file, etc.)
    bdist         create a built (binary) distribution
    bdist_rpm     create an RPM distribution
    bdist_wininst create an executable installer for MS Windows
    upload        upload binary package to PyPI

wheels
------

"wheels" are the "new" package format for python.

A wheel is essentially a zip file of the entire package, ready to be
unpacked in the right place on installation.

``pip`` will look for wheels for OS-X and Windows on PyPi, and auto-install
them if they exist

This is particularly nice for packages with non-python dependencies.


More complex packaging
----------------------

For a complex package:

You want to use a well structured setup:

http://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/

develop mode
------------

While you are developing your package, Installing it is a pain.

But you want your code to be able to import, etc. as though it were installed

``setup.py develop``  installs links to your code, rather than copies
-- so it looks like it's installed, but it's using the original source

``python setup.py develop``

You need ``setuptools`` and a setup.py  to use it.


Applications
------------

For a complete application:

  * Web apps
  * GUI apps

Multiple options:

  * Virtualenv + VCS
  * zc.buildout ( http://www.buildout.org/}
  * System packages (rpm, deb, ...)
  * Bundles...


Bundles
-------

Bundles are Python + all your code + plus all the dependencies --
all in one single "bundle"

Most popular on Windows and OS-X

::

     py2exe
     py2app
     pyinstaller
     ...


User doesn't even have to know it's python

Examples:

 http://www.bitpim.org/

 http://response.restoration.noaa.gov/nucos

LAB
---

Write a setup.py for a script of yours

  * Ideally, your script relies on at least one other module
  * At a minimum, you'll need to specify ``scripts``
  * and probably ``py_modules``
  * try:

    * ``python setup.py build``
    * ``python setup.py install``
    * ``python setup.py sdist``

  * EXTRA: install ``setuptools``

    * use: ``from setuptools import setup``
    * try: `` python setup.py develop``

  * EXTRA2: install ``wheel``

    * ``python setup.py bdist_wheel``


(my example: ``Examples/Session09/capitalize``)

==========
Next Week
==========

We'll be talking about Unicode. Read:

.. rst-class:: medium centered

  The Absolute Minimum Every Software Developer Absolutely, Positively
  Must Know About Unicode and Character Sets (No Excuses!)

http://www.joelonsoftware.com/articles/Unicode.html

Also: Cris Ewing will come by to talk about the second quarter
web development class

Homework
---------

Finish up the labs

Work on your project

And *do* let me know what you're doing if you haven't yet!
