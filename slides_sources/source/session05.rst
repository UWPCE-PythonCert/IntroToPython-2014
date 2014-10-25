
.. Foundations 2: Python slides file, created by
   hieroglyph-quickstart on Wed Apr  2 18:42:06 2014.


********************************************************************************************************
Session Five: Advanced Argument passing, List and Dict Comprehensions, Lambda and Functional programming
********************************************************************************************************


================
Review/Questions
================

Review of Previous Class
------------------------

  * Dictionaries
  * Exceptions
  * Files, etc.


Homework review
---------------

Homework Questions?

My Solutions to the dict/set lab, and some others in the class repo in:
``Solutions/Session04``

A few tidbits:

.. nextslide:: Sorting stuff in dictionaries:

dicts aren't sorted, so what if you want to do something in a sorted way?

The "old" way:

.. code-block:: python

  keys = d.keys()
  keys.sort()
  for key in keys:
      ...

Other options:

.. code-block:: python

    collections.OrderedDict

    sorted()

(demo)

=======
Unicode
=======

A quick run-down of Unicode, its use in Python 2, and some of the
gotchas that arise.


History
=======

.. rst-class:: left

    I hope you all read this:

    The Absolute Minimum Every Software Developer Absolutely,
    Positively Must Know About Unicode and Character Sets (No Excuses!)

    http://www.joelonsoftware.com/articles/Unicode.html

    If not -- go read it!

Fact number 1:
--------------

.. rst-class:: center large

    Everything is made up of bytes

If it's on disk or transmitted over a network, it's bytes

Python provides some abstractions to make it easier to deal with bytes

Unicode is a biggie

Actually, dealing with numbers rather than bytes is big
  -- but we take that for granted


What the heck is Unicode anyway?
---------------------------------

* First there was chaos...

  * Different machines used different encodings

* Then there was ASCII -- and all was good (7 bit), 127 characters

  * (for English speakers, anyway)

* But each vendor used the top half (127-255) for different things.

  * macroman, Windows 1252, etc...

  * There is now "latin-1", but still a lot of old files around

* Non Western-European languages required totally incompatible 1-byte
  encodings

* No way to mix languages with different alphabets.


Enter Unicode
--------------

The Unicode idea is pretty simple:
* one "code point" for all characters in all languages

But how do you express that in bytes?
  * Early days: we can fit all the code points in a two byte integer (65536 characters)

  * Turns out that didn't work -- now need 32 bit integer to hold all of unicode "raw" (UTC-4)

Enter "encodings":
  * An encoding is a way to map specific bytes to a code point.

  * Each code point can have one or more bytes.


Unicode
--------

A good start:

The Absolute Minimum Every Software Developer Absolutely,
Positively Must Know About Unicode and Character Sets (No Excuses!)

http://www.joelonsoftware.com/articles/Unicode.html


.. nextslide::

**Everything is Bytes**

* If it's on disk or on a network, it's bytes

* Python provides some abstractions to make it easier to deal with bytes

Unicode is a biggie

(actually, dealing with numbers rather than bytes is big -- but we take that
for granted)


Mechanics
=========

What are strings?
-----------------

Py2 strings are sequences of bytes

Unicode strings are sequences of platonic characters

It's almost one code point per character -- but there are complications
with combined characters: accents, etc.

Platonic characters cannot be written to disk or network!

(ANSI: one character == one byte -- so easy!)


Strings vs unicode
-------------------

Python 2 has two types that let you work with text:

* ``str``

* ``unicode``

And two ways to work with binary data:

* ``str``

* ``bytes()``  (and ``bytearray``)

**but:**

.. code-block:: ipython

   In [86]: str is bytes
   Out[86]: True

``bytes`` is there for py3 compatibility - -but it's good for making your
intentions clear, too.


Unicode
--------

The ``unicode`` object lets you work with characters

It has all the same methods as the string object.

"encoding" is converting from a unicode object to bytes

"decoding" is converting from bytes to a unicode object

(sometimes this feels backwards...)

Using unicode in Py2
---------------------

Built in functions

.. code-block:: python

  ord()
  chr()
  unichr()
  str()
  unicode()

The codecs module

.. code-block:: python

  import codecs
  codecs.encode()
  codecs.decode()
  codecs.open() # better to use ``io.open``


Encoding and Decoding
----------------------

Encoding

.. code-block:: ipython

  In [17]: u"this".encode('utf-8')
  Out[17]: 'this'

  In [18]: u"this".encode('utf-16')
  Out[18]: '\xff\xfet\x00h\x00i\x00s\x00'

Decoding

.. code-block:: ipython

    In [99]: print '\xff\xfe."+"x\x00\xb2\x00'.decode('utf-16')
    ∮∫x²



Unicode Literals
------------------

1) Use unicode in your source files:

.. code-block:: python

    # -*- coding: utf-8 -*-

2) escape the unicode characters:

.. code-block:: python

  print u"The integral sign: \u222B"
  print u"The integral sign: \N{integral}"

Lots of tables of code points online:

One example:
  http://inamidst.com/stuff/unidata/

:download:`hello_unicode.py  <./hello_unicode.py>`.


Using Unicode
--------------

Use ``unicode`` objects in all your code

Decode on input

Encode on output

Many packages do this for you: *XML processing, databases, ...*

**Gotcha:**

Python has a default encoding (usually ascii)

.. code-block:: ipython

  In [2]: sys.getdefaultencoding()
  Out[2]: 'ascii'

The default encoding will get used in unexpected places!

Using unicode everywhere
-------------------------

Python 2.6 and above have a nice feature to make it easier to use unicode everywhere

.. code-block:: python

    from __future__ import unicode_literals

After running that line, the ``u''`` is assumed
    
.. code-block:: ipython

    In [1]: s = "this is a regular py2 string"
    In [2]: print type(s)
    <type 'str'>

    In [3]: from __future__ import unicode_literals
    In [4]: s = "this is now a unicode string"
    In [5]: type(s)
    Out[5]: unicode

NOTE: You can still get py2 strings from other sources!


Encodings
----------

What encoding should I use???

There are a lot:

http://en.wikipedia.org/wiki/Comparison_of_Unicode_encodings

But only a couple you are likely to need:

* utf-8  (``*nix``)
* utf-16  (Windows)

and of course, still the one-bytes ones.

* ASCII
* Latin-1

UTF-8
-------

Probably the one you'll use most -- most common in Internet protocols (xml, JSON, etc.)

Nice properties:

* ASCII compatible: first 127 characters are the same

* Any ascii string is a utf-8 string

* compact for mostly-english text.

Gotchas:

* "higher" code points may use more than one byte: up to 4 for one character

* ASCII compatible means in may work with default encoding in tests -- but then blow up with real data...

UTF-16
--------

Kind of like UTF-8, except it uses at least 16bits (2 bytes) for each character: not ASCII compatible.

But is still needs more than two bytes for some code points, so you still can't process

In C/C++ held in a "wide char" or "wide string".

MS Windows uses UTF-16, as does (I think) Java.

UTF-16 criticism
-----------------

There is a lot of criticism on the net about UTF-16 -- it's kind of the worst of both worlds:

* You can't assume every character is the same number of bytes
* It takes up more memory than UTF-8

`UTF Considered Harmful <http://programmers.stackexchange.com/questions/102205/should-utf-16-be-considered-harmful>`_

But to be fair:

Early versions of Unicode: everything fit into two bytes (65536 code points). MS and Java were fairly early adopters, and it seemed simple enough to just use 2 bytes per character.

When it turned out that 4 bytes were really needed, they were kind of stuck in the middle.

Latin-1
--------

**NOT Unicode**:

a 1-byte per char encoding.

* Superset of ASCII suitable for Western European languages.

* The most common one-byte per char encoding for European text.

* Nice property -- every byte value from 0 to 255 is a valid character ( at least in Python )

.. nextslide::

* You will never get an UnicodeDecodeError if you try to decode arbitrary bytes with latin-1.

* And it can "round-trip" through a unicode object.

* Useful if you don't know the encoding -- at least it won't raise an Exception

* Useful if you need to work with combined text+binary data.

:download:`latin1_test.py  <./latin1_test.py>`.


Unicode Docs
--------------

Python Docs Unicode HowTo:

http://docs.python.org/howto/unicode.html

"Reading Unicode from a file is therefore simple"

.. code-block:: python

  import codecs
  f = codecs.open('unicode.rst', encoding='utf-8')
  for line in f:
      print repr(line)


Encodings Built-in to Python:
  http://docs.python.org/2/library/codecs.html#standard-encodings


Gotchas in Python 2
--------------------

file names, etc:

If you pass in unicode, you get unicode

.. code-block:: ipython

  In [9]: os.listdir('./')
  Out[9]: ['hello_unicode.py', 'text.utf16', 'text.utf32']

  In [10]: os.listdir(u'./')
  Out[10]: [u'hello_unicode.py', u'text.utf16', u'text.utf32']

Python deals with the file system encoding for you...

But: some more obscure calls don't support unicode filenames:

``os.statvfs()`` (http://bugs.python.org/issue18695)


.. nextslide::

Exception messages:
 
 * Py2 Exceptions use str when they print messages.
 
 * But what if you pass in a unicode object?

   * It is encoded with the default encoding.

 * ``UnicodeDecodeError`` Inside an Exception????

 NOPE: it swallows it instead.

:download:`exception_test.py  <./exception_test.py>`.

Unicode in Python 3
----------------------

The "string" object is unicode.

Py3 has two distinct concepts:

* "text" -- uses the str object (which is always unicode!)
* "binary data" -- uses bytes or bytearray

Everything that's about text is unicode.

Everything that requires binary data uses bytes.

It's all much cleaner.

(by the way, the recent implementations are very efficient...)


Exercises
=========

Basic Unicode LAB
-------------------

* Find some nifty non-ascii characters you might use.

  - Create a unicode object with them in two different ways.
  - :download:`here  <./hello_unicode.py>` is one example

* Read the contents into unicode objects:

 - :download:`ICanEatGlass.utf8.txt <./ICanEatGlass.utf8.txt>`
 - :download:`ICanEatGlass.utf16.txt <./ICanEatGlass.utf16.txt>`

and/ or

 - :download:`text.utf8 <./text.utf8>`
 - :download:`text.utf16 <./text.utf16>`
 - :download:`text.utf32 <./text.utf32>`

* write some of the text from the first exercise to file -- read that file back in.

.. nextslide:: Some Help

reference: http://inamidst.com/stuff/unidata/

NOTE: if your terminal does not support unicode -- you'll get an error trying
to print. Try a different terminal or IDE, or google for a solution.

Challenge Unicode LAB
----------------------

We saw this earlier

.. code-block:: ipython

  In [38]: u'to \N{INFINITY} and beyond!'.decode('utf-8')
  ---------------------------------------------------------------------------
  UnicodeEncodeError                        Traceback (most recent call last)
  <ipython-input-38-7f87d44dfcfa> in <module>()
  ----> 1 u'to \N{INFINITY} and beyond!'.decode('utf-8')

  /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_8.pyc in decode(input, errors)
       14 
       15 def decode(input, errors='strict'):
  ---> 16     return codecs.utf_8_decode(input, errors, True)
       17 
       18 class IncrementalEncoder(codecs.IncrementalEncoder):

  UnicodeEncodeError: 'ascii' codec can't encode character u'\u221e' in position 3: ordinal not in range(128)

.. nextslide::

But why would you **decode** a unicode object?

And it should be a no-op -- why the exception?

And why 'ascii'? I specified 'utf-8'!

It's there for backward compatibility

What's happening under the hood

.. code-block:: python

    u'to \N{INFINITY} and beyond!'.encode().decode('utf-8')

It encodes with the default encoding (ascii), then decodes

In this case, it barfs on attempting to encode to 'ascii'

.. nextslide::

So never call decode on a unicode object!

But what if someone passes one into a function of yours that's expecting a py2 string?

Type checking and converting -- yeach!

Read:

http://axialcorps.com/2014/03/20/unicode-str/

See if you can figure out the decorators:

:download:`unicodify.py  <./unicodify.py>`.


(This is advanced Python JuJu: Aren't you glad I didn't ask you to write that yourself?)



=========================
Advanced Argument Passing
=========================

Keyword arguments
-----------------

When defining a function, you can specify only what you need -- in any order

.. code-block:: ipython

    In [151]: def fun(x,y=0,z=0):
            print x,y,z
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
        print "x is:", x
       .....:
    In [158]: fun()
    x is: 4


.. nextslide::

Defaults are evaluated when the function is defined

.. code-block:: ipython
    
    In [156]: y = 4
    In [157]: def fun(x=y):
        print "x is:", x
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
        print "position: %s, %s -- shape: %s, %s"%(x, y, w, h)

    position = (3,4)
    size = {'h': 10, 'w': 20}

    >>> f( *position, **size)
    position: 3, 4 -- shape: 20, 10



Function parameters in variables
--------------------------------

You can also pull the parameters out in the function as a tuple and a dict:

.. code-block:: ipython

    def f(*args, **kwargs):
        print "the positional arguments are:", args
        print "the keyword arguments are:", kwargs

    In [389]: f(2, 3, this=5, that=7)
    the positional arguments are: (2, 3)
    the keyword arguments are: {'this': 5, 'that': 7}

Passing a dict to the ``string.format()`` method
------------------------------------------------

Now that you know that keyword args are really a dict, you can do this nifty trick:

The ``format`` method takes keyword arguments:

.. code-block:: ipython

    In [24]: u"My name is {first} {last}".format(last=u"Barker", first=u"Chris")
    Out[24]: u'My name is Chris Barker'

Build a dict of the keys and values:

.. code-block:: ipython  

    In [25]: d = {u"last":u"Barker", u"first":u"Chris"}

And pass to ``format()``with ``**``

.. code-block:: ipython  

    In [26]: u"My name is {first} {last}".format(**d)
    Out[26]: u'My name is Chris Barker'




LAB
---

Let's do this right now:

keyword arguments

* Write a function that has four optional parameters (with defaults):
  
  - foreground_color
  - background_color
  - link_color
  - visited_link_color
  
* Have it print the colors (use strings for the colors)
* Call it with a couple different parameters set
* Have it pull the parameters out with ``*args, **kwargs`` 

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

Same for dicts (and any container type)

If the elements are immutable, it doesn't really make a differnce -- but be very careful with mutable elements.


The copy module
--------------------

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
       ....:     print a
       ....: 

This makes sense: maybe you'd pass in a list, but the default is an empty list.

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
       ....:     print a
    In [16]: fun(3)
    [3]
    In [17]: fun(4)
    [4]

You get a new list every time the function is called


============================
List and Dict Comprehensions
============================

List comprehensions
-------------------
A bit of functional programming


consider this common for loop structure:

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

Remember this from last week?

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

    In [21]: { let for let in s if let in vowels }
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


===================
Anonymous functions
===================

lambda
------

.. code-block:: ipython

    In [171]: f = lambda x, y: x+y
    In [172]: f(2,3)
    Out[172]: 5

Content can only be an expression -- not a statement

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


Comprehensions
--------------

Couldn't you do all this with comprehensions?

Yes:

.. code-block:: ipython

    In [33]: [x+2 + 10 for x in l]
    Out[33]: [14, 17, 19, 24, 18, 16]
    In [34]: [x for x in l if not x%2]
    Out[34]: [2, 12, 6, 4]


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

Can also use keyword arguments}

.. code-block:: ipython
    
    In [186]: l = []
    In [187]: for i in range(3):
        l.append(lambda x, e=i: x**e)
       .....:
    In [189]: for f in l:
        print f(3)
    1
    3
    9

Note when the keyword argument is evaluated: this turns out to be very handy!

=========
Homework
=========


List comprehensions
--------------------

Note: this is a bit of a "backwards" exercise --
we show you code, you figure out what it does.

As a result, not much to submit -- but so we can give you credit, submit
a file with a solution to the final problem.

.. code-block:: python

    >>> feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

    >>> comprehension = [delicacy.capitalize() for delicacy in feast]

What is the output of:

.. code-block:: python

    >>> comprehension[0]
    ???

    >>> comprehension[2]
    ???

(figure it out before you try it)

.. nextslide:: 2. Filtering lists with list comprehensions


.. code-block:: python

    >>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
                'fruit bats']

    >>> comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

What is the output of:

.. code-block:: python

    >>> len(feast)
    ???

    >>> len(comprehension)
    ???

(figure it out first!)

.. nextslide:: 3. Unpacking tuples in list comprehensions


.. code-block:: python

    >>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

    >>> comprehension = [ skit * number for number, skit in list_of_tuples ]

What is the output of:

.. code-block:: python

    >>> comprehension[0]
    ???

    >>> len(comprehension[2])
    ???

.. nextslide::  4. Double list comprehensions

.. code-block:: python

    >>> list_of_eggs = ['poached egg', 'fried egg']

    >>> list_of_meats = ['lite spam', 'ham spam', 'fried spam']

    >>> comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

What is the output of:

.. code-block:: python

    >>> len(comprehension)
    ???

    >>> comprehension[0]
    ???

.. nextslide::  5. Set comprehensions


.. code-block:: python

    >>> comprehension = { x for x in 'aabbbcccc'}

What is the output of:

.. code-block:: python

    >>> comprehension
    ???

.. nextslide::  6. Dictionary comprehensions


.. code-block:: python

    >>> dict_of_weapons = {'first': 'fear',
                           'second': 'surprise',
                           'third':'ruthless efficiency',
                           'forth':'fanatical devotion',
                           'fifth': None}
    >>> dict_comprehension = \
    { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

What is the output of:

.. code-block:: python

    >>> 'first' in dict_comprehension
    ???
    >>> 'FIRST' in dict_comprehension
    ???
    >>> len(dict_of_weapons)
    ???
    >>> len(dict_comprehension)
    ???

.. nextslide:: Other resources


See also:

https://github.com/gregmalcolm/python_koans

https://github.com/gregmalcolm/python_koans/blob/master/python2/koans/about_comprehension.py


.. nextslide:: 7. Count even numbers


(submit this one to gitHub for credit on this assignment)

This is from CodingBat "count_evens" (http://codingbat.com/prob/p189616)

*Using a list comprehension*, return the number of even ints in the given array.

Note: the % "mod" operator computes the remainder, e.g. ``5 % 2`` is 1.

.. code-block:: python

    count_evens([2, 1, 2, 3, 4]) == 3

    count_evens([2, 2, 0]) == 3

    count_evens([1, 3, 5]) == 0


.. code-block:: python

    def count_evens(nums):
       one_line_comprehension_here


``dict`` and ``set`` comprehensions
------------------------------------

Let's revisiting the dict/set lab -- see how much you can do with
comprehensions instead.

Specifically,  look at these:

First a slightly bigger, more interesting (or at least bigger..) dict:

.. code-block:: python

    food_prefs = {"name": u"Chris",
                  u"city": u"Seattle",
                  u"cake": u"chocolate",
                  u"fruit": u"mango",
                  u"salad": u"greek",
                  u"pasta": u"lasagna"}

.. nextslide:: Working with this dict:

1. Print the dict by passing it to a string format method, so that you
get something like:

    "Chris is from Seattle, and he likes chocolate cake, mango fruit,
     greek salad, and lasagna pasta"

2. Using a list comprehension, build a dictionary of numbers from zero
to fifteen and the hexadecimal equivalent (string is fine).

3. Do the previous entirely with a dict comprehension -- should be a one-liner

4. Using the dictionary from item 1: Make a dictionary using the same
keys but with the number of 'a's in each value. You can do this either
by editing the dict in place, or making a new one. If you edit in place,
make a copy first!

.. nextslide::

5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible 2, 3 and 4.

    a. Do this with one set comprehension for each set.

    b. What if you had a lot more than 3? -- Don't Repeat Yourself (DRY)

       - create a sequence that holds all three sets

       - loop through that sequence to build the sets up -- so no repeated code.

    c. Extra credit:  do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)


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
        print f(5)
       .....:
    5
    6
    7
    8
    ### If you loop through them all, and call them, each one adds one more
    to the input, 5... i.e. the nth function in the list adds n to the input.




Functional files
-----------------

Write a program that takes a filename and "cleans" the file be removing all the leading and trailing whitespace from each line.

Read in the original file and write out a new one, either creating a new file or overwriting the existing one.

Give your user the option of which to perform.

Use ``map()`` to do the work.

Write a second version using a comprehension.

.. nextslide:: Hint

``sys.argv`` hold the command line arguments the user typed in. If the user types:

.. code-block:: bash

  $ python the_script a_file_name

Then:

.. code-block:: python

    import sys
    filename = sys.argv[1]

will get ``filename == "a_file_name"``


Recommended Reading
---------------------

* LPTHW: Ex 40 - 45

http://learnpythonthehardway.org/book/

* Dive Into Python: chapter 4, 5

http://www.diveintopython.net/toc/index.html

