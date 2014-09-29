.. Foundations 2: Python slides file, created by
   Chris Barker: May 12, 2014.

*******************************************************
Session Four: Dictionaries, Sets, Exceptions, and Files
*******************************************************



================
Review/Questions
================

Review of Previous Classes
--------------------------

  * Sequences

    - Slicing
    - Lists
    - Tuples
    - tuple vs lists - which to use?

  * interating

    - for
    - while

      - break and continue

    - else with loops

Any questions?

.. nextslide::

A couple other nifty utilties with for loops:

**tuple unpacking:**

remember this?

.. code-block:: python

    x, y = 3, 4

You can do that in a for loop, also:

.. code-block:: ipython

  In [4]: l = [(1, 2), (3, 4), (5, 6)]

  In [5]: for i, j in l:
              print "i:%i, j:%i"%(i, j)

  i:1, j:2
  i:3, j:4
  i:5, j:6

Looping through two loops at once:
----------------------------------

**zip:**

.. code-block:: ipython

    In [10]: l1 = [1, 2, 3]

    In [11]: l2 = [3, 4, 5]

    In [12]: for i, j in zip(l1, l2):
       ....:     print "i:%i, j:%i"%(i, j)
       ....:
    i:1, j:3
    i:2, j:4
    i:3, j:5



Homework comments
-----------------

Building up a long string.

The obvious thing to do is something like::

  msg = u""
  for piece in list_of_stuff:
      msg += piece

But: strings are immutable -- python needs to create a new string each time you add a piece -- not efficient::

   msg = []
   for piece in list_of_stuff:
       msg.append(piece)
   u" ".join(msg)

appending to lists is efficient -- and so is the join() method of strings.


.. nextslide::

What is ``assert`` for?

Testing -- NOT for issues expected to happen operationally::

    assert m >= 0

in operational code should be::

    if m < 0:
        raise ValueError

I'll cover Exceptions later this class...

(Asserts get ignored if optimization is turned on!)


=================
A little warm up
=================

Fun with strings
------------------

* Rewrite: ``the first 3 numbers are: %i, %i, %i"%(1,2,3)``

    - for an arbitrary number of numbers...

* Write a format string that will take:

    -  ``( 2, 123.4567, 10000)``

    -       and produce:

    - `` "file_002 :   123.46, 1e+04" ``

=====================
Dictionaries and Sets
=====================

Dictionary
----------
Python calls it a ``dict``

Other languages call it:

  * dictionary
  * associative array
  * map
  * hash table
  * hash
  * key-value pair


Dictionary Constructors
-----------------------
.. code-block:: python

    >>> {'key1': 3, 'key2': 5}
    {'key1': 3, 'key2': 5}

    >>> dict([('key1', 3),('key2', 5)])
    {'key1': 3, 'key2': 5}

    >>> dict(key1=3, key2= 5)
    {'key1': 3, 'key2': 5}

    >>> d = {}
    >>> d['key1'] = 3
    >>> d['key2'] = 5
    >>> d
    {'key1': 3, 'key2': 5}

Dictionary Indexing
-------------------
::
    
    >>> d = {'name': 'Brian', 'score': 42}

    >>> d['score']
    42

    >>> d = {1: 'one', 0: 'zero'}

    >>> d[0]
    'zero'

    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'


.. nextslide::

Keys can be any immutable:

  * number
  * string
  * tuple

.. code-block:: ipython

    In [325]: d[3] = 'string'
    In [326]: d[3.14] = 'pi'
    In [327]: d['pi'] = 3.14
    In [328]: d[ (1,2,3) ] = 'a tuple key'
    In [329]: d[ [1,2,3] ] = 'a list key'
       TypeError: unhashable type: 'list'


Actually -- any "hashable" type.


.. nextslide:: Hashing

Hash functions convert arbitrarily large data to a small proxy (usually int)

Always return the same proxy for the same input

MD5, SHA, etc

Dictionaries hash the key to an integer proxy and use it to find the key and value.

Key lookup is efficient because the hash function leads directly to a bucket with very few keys (often just one)

What would happen if the proxy changed after storing a key?

Hashability requires immutability

Key lookup is very efficient

Same average time regardless of size


.. nextslide:: Dictionary indexing


Note: Python name look-ups are implemented with dict -- it's highly optimized

Key to value:

 * lookup is one way

Value to key:

 * requires visiting the whole dict

If you need to check dict values often, create another dict or set

(up to you to keep them in sync)


Dictionary Ordering (not)
-------------------------


Dictionaries have no defined order

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: d
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: ['three', 'two', 'one']

Dictionary Iterating
--------------------

``for``  iterates over the keys

.. code-block:: ipython

	In [15]: d = {'name': 'Brian', 'score': 42}

	In [16]: for x in d:                       
	    print x
	   ....:     
	score
	name


(note the different order...)

dict keys and values
--------------------

.. code-block:: ipython

	In [20]: d = {'name': 'Brian', 'score': 42}

	In [21]: d.keys()
	Out[21]: ['score', 'name']

	In [22]: d.values()
	Out[22]: [42, 'Brian']

	In [23]: d.items()
	Out[23]: [('score', 42), ('name', 'Brian')]


dict keys and values
--------------------

Iterating on everything

.. code-block:: ipython

	In [26]: d = {'name': 'Brian', 'score': 42}

	In [27]: for k, v in d.items():
	    print "%s: %s" % (k,v)
	   ....:     
	score: 42
	name: Brian


Dictionary Performance 
-----------------------

  * indexing is fast and constant time: O(1)

  * ``x in s`` constant time: O(1)

  * visiting all is proportional to n: O(n)

  * inserting is constant time: O(1)

  * deleting is constant time: O(1)


 http://wiki.python.org/moin/TimeComplexity


Other dict operations:
----------------------

See them all here:

https://docs.python.org/2/library/stdtypes.html#mapping-types-dict

Is it in there?

.. code-block:: ipython

  In [5]: d
  Out[5]: {'that': 7, 'this': 5}

  In [6]: 'that' in d
  Out[6]: True

  In [7]: 'this' not in d
  Out[7]: False

Containment is on the keys.

.. nextslide::

Getting something: (like indexing)

.. code-block:: ipython

  In [9]: d.get('this')
  Out[9]: 5

But you can specify a default

.. code-block:: ipython

  In [11]: d.get(u'something', u'a default')
  Out[11]: u'a default'

Never raises an Exception (default default is None)

.. nextslide::

iterating

.. code-block:: ipython

  In [13]: for item in d.iteritems():
     ....:     print item
     ....:     
  ('this', 5)
  ('that', 7)
  In [15]: for key in d.iterkeys():
      print key
     ....:     
  this
  that
  In [16]: for val in d.itervalues():
      print val
     ....:     
  5
  7

the ``iter*`` methods don't actually create the lists.

.. nextslide::

"Popping": getting the value while removing it

pop out a particular key

.. code-block:: ipython

  In [19]: d.pop('this')
  Out[19]: 5

  In [20]: d
  Out[20]: {'that': 7}

pop out an arbitrary key, value pair

.. code-block:: ipython

  In [23]: d.popitem()
  Out[23]: ('that', 7)

  In [24]: d
  Out[24]: {}

.. nextslide::

This one is handy:

``setdefault(key[, default])``

gets the value if it's there, sets it if it's not

.. code-block:: ipython

  In [27]: d.setdefault(u'something', u'a value')
  Out[27]: u'a value'

  In [28]: d
  Out[28]: {u'something': u'a value'}

  In [29]: d.setdefault(u'something', u'a value')
  Out[29]: u'a value'

  In [30]: d
  Out[30]: {u'something': u'a value'}

.. nextslide::

dict View objects:

Like ``keys()``, ``values()``, ``items()``, but maintain a link to the original dict

.. code-block:: ipython

  In [47]: d
  Out[47]: {u'something': u'a value'}

  In [48]: item_view = d.viewitems()

  In [49]: d['something else'] = u'another value'

  In [50]: item_view
  Out[50]: dict_items([('something else', u'another value'), (u'something', u'a value')])



Sets 
-----

``set``  is an unordered collection of distinct values

Essentially a dict with only keys

Set Constructors

.. code-block:: ipython

    >>> set()
    set([])

    >>> set([1, 2, 3])
    set([1, 2, 3])

    >>> {1, 2, 3}
    set([1, 2, 3])

    >>> s = set()

    >>> s.update([1, 2, 3])
    >>> s
    set([1, 2, 3])


Set Properties
---------------

``Set``  members must be hashable

Like dictionary keys -- and for same reason (efficient lookup)

No indexing (unordered)

.. code-block:: ipython

    >>> s[1]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


Set Methods
-----------

.. code-block:: ipython

    >> s = set([1])
    >>> s.pop() # an arbitrary member
    1
    >>> s.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'pop from an empty set'
    >>> s = set([1, 2, 3])
    >>> s.remove(2)
    >>> s.remove(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2

.. nextslide::

All the "set" operations from math class...

.. code-block:: python

    s.isdisjoint(other)

    s.issubset(other)
    
    s.union(other, ...)
    
    s.intersection(other, ...)
    
    s.difference(other, ...)
    
    s.symmetric_difference( other, ...)

Frozen Set
----------

Another kind of set: ``frozenset``

immutable -- for use as a key in a dict
(or another set...)

.. code-block:: python

    >>> fs = frozenset((3,8,5))
    >>> fs.add(9)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'


==========
Exceptions
==========

Exceptions
----------

Another Branching structure:

.. code-block:: python

    try:
        do_something()
        f = open('missing.txt')
        process(f)   # never called if file missing
    except IOError:
        print "couldn't open missing.txt"

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


Exceptions
----------

Use Exceptions, rather than your own tests:

Don't do this:

.. code-block:: python

    do_something()
    if os.path.exists('missing.txt'):
        f = open('missing.txt')
        process(f)   # never called if file missing

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
        print u"Input must be an integer, try again."

Or let the Exception be raised....


.. nextslide:: EAFP


"it's Easier to Ask Forgiveness than Permission"

 -- Grace Hopper


http://www.youtube.com/watch?v=AZDWveIdqjY

(Pycon talk by Alex Martelli)

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
        print "couldn't open missing.txt"
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
        print "couldn't open missing.txt"
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
        print the_error
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

Example (for last week's ackerman homework)::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise ValueError

Is it the *value* or the input the problem here?

Nope: the *type* is the problem::

  if (not isinstance(m, int)) or (not isinstance(n, int)):
      raise TypeError

but should you be checking type anyway? (EAFP)


========================
File Reading and Writing
========================

Files
-----

Text Files

.. code-block:: python

    import io
    f = io.open('secrets.txt', codec='utf-8')
    secret_data = f.read()
    f.close()

``secret_data`` is a (unicode) string

``codec`` defaults to ``sys.getdefaultencoding()`` -- often NOT what you want.

(There is also the regular ``open()`` built in, but it won't handle Unicode for you...)

.. nextslide::

Binary Files

.. code-block:: python

    f = io.open('secrets.bin', 'rb')
    secret_data = f.read()
    f.close()

``secret_data``  is a byte string

(with arbitrary bytes in it -- well, not arbitrary -- whatever is in the file.)

(See the ``struct``  module to unpack binary data )


.. nextslide::


File Opening Modes

.. code-block:: python

    f = io.open('secrets.txt', [mode])
    'r', 'w', 'a'
    'rb', 'wb', 'ab'
    r+, w+, a+
    r+b, w+b, a+b
    U
    U+

These follow the Unix conventions, and aren't all that well documented on the Python docs. But these BSD docs make it pretty clear:

http://www.manpagez.com/man/3/fopen/

**Gotcha** -- 'w' modes always clear the file

.. nextslide:: Text File Notes

Text is default

  * Newlines are translated: ``\r\n -> \n``
  *   -- reading and writing!
  * Use \*nix-style in your code: ``\n``
  * ``io.open()`` returns various "stream" objects -- but they act like file objects.
  * In text mode, io.open() defaults to "Universal" newline mode.


Gotcha:

  * no difference between text and binary on \*nix
  * breaks on Windows


.. nextslide:: Other parameters to ``io.open()``:

``io.open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True)``

 * ``file`` is generally a file name or full path

 * ``mode`` is the mode for opening: 'r', 'w', etc.

 * ``buffering`` controls the buffering mode (0 for no buffering)

 * ``encoding`` sets the unicode encoding -- only for text files -- when set, you can ONLY write unicode object to the file.

 * ``errors`` sets the encoding error mode: 'strict', 'ignore', 'replace',...

 * ``newline`` controls Universal Newline mode: lets you write DOS-type files on \*nix, for instance (text mode only).

 * ``closedfd`` controls close()  behavior if a file descriptor, rather than a name is passed in (advanced usage!)

(https://docs.python.org/2/library/io.html?highlight=io.open#io.open)


File Reading
------------

Reading part of a file

.. code-block:: python

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

.. nextslide::


Common Idioms

.. code-block:: python

    for line in io.open('secrets.txt'):
        print line

(the file object is an iterator!)

.. code-block:: python

    f = io.open('secrets.txt')
    while True:
        line = f.readline()
        if not line:
            break
        do_something_with_line()


File Writing
------------

.. code-block:: python

    outfile = io.open('output.txt', 'w')
    for i in range(10):
        outfile.write("this is line: %i\n"%i)


File Methods
------------

Commonly Used Methods

.. code-block:: python

    f.read() f.readline()  f.readlines()

    f.write(str) f.writelines(seq)

    f.seek(offset)   f.tell()

    f.flush()

    f.close()


File Like Objects
-----------------


Many classes implement the file interface:

  * loggers
  * ``sys.stdout``
  * ``urllib.open()``
  * pipes, subprocesses
  * StringIO

https://docs.python.org/2/library/stdtypes.html#file-objects

StringIO
--------

.. code-block:: python

    In [417]: import StringIO
    In [420]: f = StringIO.StringIO()
    In [421]: f.write(u"somestuff")
    In [422]: f.seek(0)
    In [423]: f.read()
    Out[423]: 'somestuff'

(handy for testing file handling code...)


=====================
Paths and Directories
=====================

Paths
-----

Paths are generally handled with simple strings (or Unicode strings)

Relative paths:

.. code-block:: python

    u'secret.txt'
    u'./secret.txt'

Absolute paths:

.. code-block:: python

    u'/home/chris/secret.txt'


Either work with ``open()`` , etc.

(working directory only makes sense with command-line programs...)

os module
----------

.. code-block:: python

    os.getcwd() -- os.getcwdu() (u for Unicode)
    chdir(path)
    os.path.abspath()
    os.path.relpath()￼


.. nextslide:: os.path module

.. code-block:: python

    os.path.split()
    os.path.splitext()
    os.path.basename()
    os.path.dirname()
    os.path.join()


(all platform independent)

.. nextslide:: directories

.. code-block:: python

    os.listdir()
    os.mkdir()
    os.walk()

(higher level stuff in ``shutil``  module)

pathlib
-------

``pathlib`` is a new package for handling paths in an OO way:

http://pathlib.readthedocs.org/en/pep428/

It is now part of the Python3 standard library, and has been back-ported for use with Python2:

.. code-block:: bash

    $ pip install pathlib

All the stuff in os.path and more:

.. code-block:: ipython

    In [64]: import pathlib
    In [65]: pth = pathlib.Path('./')
    In [66]: pth.is_dir()
    Out[66]: True
    In [67]: pth.absolute()
    Out[67]: PosixPath('/Users/Chris/PythonStuff/CodeFellowsClass/sea-f2-python-sept14/Examples/Session04')
    In [68]: for f in pth.iterdir():
                 print f
    junk2.txt
    junkfile.txt
    ...

=========
Homework
=========

Recommended Reading:
---------------------
  * Dive Into Python: Chapt. 13,14
  * Unicode: http://www.joelonsoftware.com/articles/Unicode.html

Assignments:
-------------

 * dict/sets lab
 * coding kata: trigrams
 * Exceptions
 * Update mailroom with dicts.


Dictionaries and Sets
---------------------

1.

* Create a dictionary containing "name", "city", and "cake" for "Chris" from "Seattle" who likes "Chocolate".

* Display the dictionary.

* Delete the entry for "cake".

* Display the dictionary.

* Add an entry for "fruit" with "Mango" and display the dictionary.

  - Display the dictionary keys.
  - Display the dictionary values.
  - Display whether or not "cake" is a key in the dictionary (i.e. False) (now).
  - Display whether or not "Mango" is a value in the dictionary.

.. nextslide::

2.

* Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

3.

* Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 'a's in each value.

.. nextslide:: sets

4.

* Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

* Display the sets.

* Display if s3 is a subset of s2 (False)

* and if s4 is a subset of s2 (True).

5.

* Create a set with the letters in 'Python' and add 'i' to the set.

* Create a frozenset with the letters in 'marathon'

* display the union and intersection of the two sets.


Text and files and dicts, and...
---------------------------------

  * Coding Kata 14 - Dave Thomas

    http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

    and in this doc:

    http://codefellows.github.io/sea-c15-python/supplements/kata_fourteen.html

  * Use The Adventures of Sherlock Holmes as input:

        http://codefellows.github.io/sea-c15-python/_downloads/sherlock.txt

  *  This is intentionally open-ended and underspecified. There are many interesting decisions to make.

  * Experiment with different lengths for the lookup key. (3 words, 4 words, 3 letters, etc)

Exceptions
-----------

Improving ``raw_input``

* The ``raw_input()``  function can generate two exceptions: ``EOFError``  or ``KeyboardInterrupt``  on end-of-file(EOF) or canceled input.

* Create a wrapper function, perhaps ``safe_input()``  that returns ``None``  rather rather than raising these exceptions, when the user enters ``^C``  for Keyboard Interrupt, or ``^D`` (``^Z``  on Windows) for End Of File.

* Update your mailroom program to use exceptions (and IBAFP) to handle malformed numeric input


Paths and File Processing
--------------------------

  * write a program which prints the full path to all files in the current directory, one per line

  * write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)

  * update mailroom from last weeks homework to:

    - use dicts where appropriate
    - write a full set of letters to everyone to individual files on disk
    - see if you can use a dict to switch between the users selections
    - Try to use a dict and the .format() method to do the letter as one big template -- rather than building up a big string in parts.

