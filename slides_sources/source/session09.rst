
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.


******************************************************************
Session Nine: Decorators, Context Managers, Packages and packaging
******************************************************************

======================
Lightning Talks Today:
======================

.. rst-class:: medium

  person 1

  person 2

  person 3

  person 4

================
Review/Questions
================


Decorators
==========

**A Short Digression**

.. rst-class:: left build
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

There are many things you can do with a simple pattern like this one.  So many,
that we give it a special name:

.. rst-class:: centered

**Decorator**

.. rst-class:: build
.. container::

    A decorator is a function that takes a function as an argument and
    returns a function as a return value.

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

    You want to see when each function is called, with what arguments and with what
    result. So you rewrite each function as follows:

    .. code-block:: python

        def add(a, b):
            print "Function 'add' called with args: %r" % locals()
            result = a + b
            print "\tResult --> %r" % result
            return result

.. nextslide::

That's not particularly nice, especially if you have lots of functions in your
module.

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

In python a *callable* is a function, a method on a class, or even a class that
implements the ``__call__`` special method.

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

Let's see a few that might help you with work you've been doing recently.

For example, a ``staticmethod()`` can be implemented with a decorator
expression:

.. code-block:: python

    # the way we saw last week:
    class C(object):
        def add(a, b):
            return a + b
        add = staticmethod(add)

    # and the decorator form
    class C(object):
        @staticmethod
        def add(a, b):
            return a + b

.. nextslide::

The ``classmethod()`` builtin can do the same thing:

.. code-block:: python

    # in imperative style:
    class C(object):
        def from_iterable(cls, seq):
            # method body
        from_iterable = classmethod(from_iterable)

    # and in declarative style
    class C(object):
        @classmethod
        def from_iterable(cls, seq):
            # method body

.. nextslide::

Perhaps most commonly, you'll see the ``property()`` builtin used this way.

Last week we saw this code:

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

Used in a decorator statement, it looks like this:

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

Note that in this case, the decorator object returned by the property decorator
itself implements additional decorators as attributes on the returned method
object.

Context Managers
================

**A Short Digression**

.. rst-class:: left build
.. container::

    Repetition in code stinks.

    A large source of repetition in code deals with the handling of externals
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
remember all that **every** time you open a resource?

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

.. rst-class:: build

* ``open`` and ``codecs.open`` both work as context managers
* networks connections via ``socket`` do as well.
* most implementations of database wrappers can open connections or cursors as
  context managers.
* ...

But what if you are working with a library that doesn't support this
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

But what if the thing doesn't have a ``close()`` method, or you're creating the thing and it shouldn't?

.. nextslide:: Do It Yourself

You can also define a context manager of your own.

The interface is simple.  It must be a class that implements these two *special
methods*:

``__enter__(self)``:
  Called when the ``with`` statement is run, it should return something to work
  with in the created context.

``__exit__(self, e_type, e_val, e_traceback)``:
  Clean-up that needs to happen is implemented here.

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
        print '__exit__(%s, %s, %s)' % (exc_type, exc_val, exc_tb)
        return self.handle_error

.. nextslide::

This class doesn't do much of anything, but playing with it can help clarify
the order in which things happen:

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

``contextlib.contextmanager`` turns generator functions into context managers

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

Homework
========

Python Power


Assignments
-----------

Task 1: Timing Context Manager

Create a context manager that will print to stdout the elapsed time taken to
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


.. nextslide::

Task 2: ``p-wrapper`` Decorator

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

.. nextslide::

Task 3: Generator Homework (documented above)

Task 4: Iterator Homework (documented above)


