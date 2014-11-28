
.. _unicode_supplement:


===================
Unicode in Python 2
===================

A quick run-down of Unicode, its use in Python 2, and some of the gotchas that arise.

 - Chris Barker

History
=======


What the heck is Unicode anyway?
---------------------------------

* First there was chaos...

  * Different machines used different encodings

* Then there was ASCII -- and all was good (7 bit), 127 characters

  * (for English speakers, anyway)

* But each vendor used the top half (127-255) for different things.

  * MacRoman, Windows 1252, etc... 

  * There is now "latin-1", but still a lot of old files around

* Non-Western European languages required totally incompatible 1-byte encodings

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

