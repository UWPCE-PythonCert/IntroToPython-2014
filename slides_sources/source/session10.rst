*************************************************
Session Ten: Unicode, Persistence/Serialization
*************************************************

=====================
Web Development Class
=====================

.. rst-class:: large centered

  Internet Programming in Python

  Cris Ewing

================
Review/Questions
================

Review of Previous Class
------------------------


  * Decorators
  * Context Managers
  * Packaging




Projects
--------

Due Dec Friday, Dec 12th, 11:59pm PST

.. rst-class:: centered medium

  (that's three days!)

Push to github or email them to me.

Lightning Talks Today
---------------------

.. rst-class:: medium

  | Danielle G Marcos
  |
  | Carolyn Evans
  |
  | Bryan L Davis
  |
  | Changqing Zhu
  |
  | Alexandra N Kazakova
  |

(first three go now!)

========
Unicode
========

.. rst-class:: left

    I hope you all read this:

    The Absolute Minimum Every Software Developer Absolutely,
    Positively Must Know About Unicode and Character Sets (No Excuses!)

    http://www.joelonsoftware.com/articles/Unicode.html

    If not -- go read it!

Fact number 1:
--------------

.. rst-class:: centered medium

    Everything is made up of bytes

If it's on disk or transmitted over a network, it's bytes

Python provides some abstractions to make it easier to deal with bytes

Unicode is a biggie

Actually, dealing with numbers rather than bytes is big -- but we take that for granted


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

Fact number 2:
--------------

.. rst-class:: centered medium

    The world needs more than 255 charactors.

.. rst-class:: centered

  Hello, world!   •   Здравствуй, мир!

  Բարեւ, աշխարհի!   •   !مرحبا ، العالم

  !שלום, עולם   •   여보세요 세계!

  नमस्ते, दुनिया!   •   你好，世界！


Enter Unicode
--------------

The Unicode idea is pretty simple:

  * one "code point" for all characters in all languages

But how do you express that in bytes?
  * Early days: we can fit all the code points in a two byte integer (65536 characters)

  * Turns out that didn't work -- we now need 32 bit integer to hold all of unicode
    "raw" (UTC-4) -- well we dopnt need that many, but common machines don't have
    24 bit integers.

Enter "encodings":
  * An encoding is a way to map specific bytes to a code point.

  * Each code point can have one or more bytes.


=========
Mechanics
=========

What are strings?
-----------------

Py2 strings are sequences of bytes

Unicode strings are sequences of platonic characters

It's almost one code point per character -- but there are complications
with combined characters: accents, etc. (we can ignore those most of the time)

Platonic characters cannot be written to disk or network!

(ANSI: one character == one byte -- so easy!)


str vs unicode
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

``bytes`` is there for py3 compatibility -- but it's good for making your
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

:download:`hello_unicode.py  <../../Examples/Session10/hello_unicode.py>`.


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

And of course, still the one-bytes ones.

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

But it still needs more than two bytes for some code points, so you still can't assume two byte per character.

In C/C++ held in a "wide char" or "wide string".

MS Windows uses UTF-16, as does (I think) Java.

UTF-16 criticism
-----------------

There is a lot of criticism on the net about UTF-16 -- it's kind of the worst of both worlds:

* You can't assume every character is the same number of bytes
* It takes up more memory than UTF-8

`UTF-16 Considered Harmful <http://programmers.stackexchange.com/questions/102205/should-utf-16-be-considered-harmful>`_

But to be fair:

Early versions of Unicode: everything fit into two bytes (65536 code points).

MS and Java were fairly early adopters, and it seemed simple enough to just use 2 bytes per character.

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

:download:`latin1_test.py  <../../Examples/Session10/latin1_test.py>`.


Unicode Docs
--------------

Python Docs Unicode HowTo:

http://docs.python.org/howto/unicode.html

"Reading Unicode from a file is therefore simple"

.. code-block:: python

  import io
  f = io.open('hello_unicode.py', encoding='utf-8')
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

:download:`unicode_exception_test.py  <../../Examples/Session10/unicode_exception_test.py>`.

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


=================
Basic Unicode LAB
=================


* Find some nifty non-ascii characters you might use.

  - Create a unicode object with them in two different ways.
  - :download:`here  <../../Examples/Session10/hello_unicode.py>` is one example

* Read the contents into unicode objects:

 - :download:`ICanEatGlass.utf8.txt <../../Examples/Session10/ICanEatGlass.utf8.txt>`
 - :download:`ICanEatGlass.utf16.txt <../../Examples/Session10/ICanEatGlass.utf16.txt>`

and/ or

 - :download:`text.utf8 <../../Examples/Session10/text.utf8>`
 - :download:`text.utf16 <../../Examples/Session10/text.utf16>`
 - :download:`text.utf32 <../../Examples/Session10/text.utf32>`

* write some of the text from the first exercise to file -- read that
  file back in.

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

But what if someone passes one into a function of yours that's expecting
a py2 string?

Type checking and converting -- yeach!

Read:

http://axialcorps.com/2014/03/20/unicode-str/

See if you can figure out the decorators:

:download:`unicodify.py  <../../Examples/Session10/unicodify.py>`.


(This is advanced Python JuJu: Aren't you glad I didn't ask you to write
that yourself?)

Lightning Talks
-----------------
.. rst-class:: medium

|
| Changqing Zhu
|
| Alexandra N Kazakova
|

============
Code Review?
============

.. rst-class:: left

  Options:

    1) Look at someone's code.

    2) Do a bit with persistance / serialization

  (pickle, json, csv, ini files, xml...)

Serialization
-------------

Today is less about concepts

More about learning to use a given module

So less talk, more coding

.. nextslide::

I'm focusing on methods available in the Python standard library

Serialization is the process of putting your potentially complex
(and nested) python data structures into a linear (serial) form .. i.e. a string of bytes.

The serial form can be saved to a file, pushed over the wire, etc.

Persistence
-----------

Persistence is saving your python data structure(s) to disk -- so they
will persist once the python process is finished.

Any serial form can provide persistence (by dumping/loading it to/from
a file), but not all persistence mechanisms are serial (i.e RDBMS)

http://wiki.python.org/moin/PersistenceTools

=======================
Python Specific Formats
=======================

Python Literals
---------------

Putting plain old python literals in your file

Gives a nice, human-editable form for config files, etc.

Don't use for untrusted sources!!!

Python Literals
---------------

Good for basic python types.
(can work for your own classes, too -- if you write a good ``__repr__`` )

In theory, ``repr()``  always gives a form that can be re-constructed.

Often ``str()``  form works too.

``pprint``  (pretty print) module can make it easier to read.

Python Literal Example
----------------------

.. code-block:: ipython

    # a list of dicts
    data = [{'this':5, 'that':4}, {'spam':7, 'eggs':3.4}]
    In [51]: s = repr(data) # save a string version:
    In [52]: data2 = eval(s) # re-construct with eval:
    In [53]: data2 == data # they are equal
    Out[53]: True
    In [54]: data is data2 # but not the same object
    Out[54]: False


You can save the string to a file and even use ``import``

(NOTE: ``ast.literal_eval`` is safer than eval)

pretty print
------------

.. code-block:: ipython

    In [69]: import pprint
    In [71]: repr(data)
    Out[71]: "[{'this': 5, 'that': 4}, {'eggs': 3.4, 'spam': 7}, {'foo': 86, 'bar': 4.5}, {'fun': 43, 'baz': 6.5}]"
    In [72]: s = pprint.pformat(data)
    In [73]: print s
    [{'that': 4, 'this': 5},
     {'eggs': 3.4, 'spam': 7},
     {'bar': 4.5, 'foo': 86},
     {'baz': 6.5, 'fun': 43}]


Pickle
------

Pickle is a binary format for python objects

You can essentially dump any python object to disk (or string, or socket, or...

``cPickle``  is faster than pickle, but
can't be customized -- you usually want ``cPickle``

http://docs.python.org/library/pickle.html


.. nextslide::

.. code-block:: ipython

    In [87]: import cPickle as pickle
    In [83]: data
    Out[83]:
    [{'that': 4, 'this': 5},
     {'eggs': 3.4, 'spam': 7},
     {'bar': 4.5, 'foo': 86},
     {'baz': 6.5, 'fun': 43}]
    In [84]: pickle.dump(data, open('data.pkl', 'wb'))
    In [85]: data2 = pickle.load(open('data.pkl', 'rb'))
    In [86]: data2 == data
    Out[86]: True


http://docs.python.org/library/pickle.html

Shelve
------

A "shelf" is a persistent, dictionary-like object

The values (not the keys!) can be essentially arbitrary Python
objects (anything picklable)

NOTE: will not reflect changes in mutable objects without re-writing them to the db. (or use writeback=True)

If less that 100s of MB -- just use a dict and pickle it.

http://docs.python.org/library/shelve.html


.. nextslide::


``shelve``  presents a ``dict``  interface:

.. code-block:: ipython

    import shelve
    d = shelve.open(filename)
    d[key] = data   # store data at key
    data = d[key]   # retrieve a COPY of data at key
    del d[key]      # delete data stored at key
    flag = d.has_key(key)   # true if the key exists
    d.close()       # close it

http://docs.python.org/library/shelve.html

LAB
---

There are two datasets in the ``Examples\Session10`` dir:

.. code-block:: ipython

    add_book_data.py
    add_book_data_flat.py
    # load with:
    from add_book_data import AddressBook

They have address book data -- one with a nested dict, one "flat"

* Write a module that saves the data as python literals in a file

  - and reads it back in

* Write a module that saves the data as a pickle in a file

  - and reads it back in

* Write a module that saves the data in a shelve

  - and accesses it one by one.


===================
Interchange Formats
===================

INI
---

INI files

(the old Windows config files)

::

    [Section1]
    int = 15
    bool = true
    float = 3.1415
    [Section2]
    int = 32
    ...



Good for configuration data, etc.

ConfigParser
------------

Writing ``ini``  files:

.. code-block:: ipython

    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.add_section('Section1')
    config.set('Section1', 'int', '15')
    config.set('Section1', 'bool', 'true')
    config.set('Section1', 'float', '3.1415')
    # Writing our configuration file to 'example.cfg'
    config.write( open('example.cfg', 'wb') )

Note: all keys and values are strings

.. nextslide::

Reading ``ini``  files:

.. code-block:: ipython

    >>> config = ConfigParser.ConfigParser()
    >>> config.read('example.cfg')
    >>> config.sections()
    ['Section1', 'Section2']
    >>> config.get('Section1', 'float')
    '3.1415'
    >>> config.items('Section1')
    [('int', '15'), ('bool', 'true'), ('float', '3.1415')]


http://docs.python.org/library/configparser.html

CSV
---

CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.

No real standard -- the Python csv package more or less follows MS Excel "standard" (with other "dialects" available)

Can use delimiters other than commas... (I like tabs better)

Most useful for simple tabular data

CSV module
----------

Reading ``CSV``  files:

.. code-block:: python

    >>> import csv
    >>> spamReader = csv.reader( open('eggs.csv', 'rb') )
    >>> for row in spamReader:
    ...     print ', '.join(row)
    Spam, Spam, Spam, Spam, Spam, Baked Beans
    Spam, Lovely Spam, Wonderful Spam



``csv``  module takes care of string quoting, etc. for you

http://docs.python.org/library/csv.html

.. nextslide::

Writing ``CSV``  files:

.. code-block:: python

    >>> import csv
    >>> spamWriter = csv.writer(open('eggs.csv', 'wb'),
                                quoting=csv.QUOTE_MINIMAL)
    >>> spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    >>> spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


``csv``  module takes care of string quoting, etc for you

http://docs.python.org/library/csv.html

JSON
----

JSON (JavaScript Object Notation) is a subset of JavaScript syntax used as a lightweight data interchange format.

Python module has an interface similar to pickle

Can handle the standard Python data types

Specializable encoding/decoding for other types -- but I wouldn't do that!

Presents a similar interface as ``pickle``

http://www.json.org/

http://docs.python.org/library/json.html

Python json module
------------------

.. code-block:: ipython

    In [94]: s = json.dumps(data)
    Out[95]: '[{"this": 5, "that": 4}, {"eggs": 3.4, "spam": 7},
               {"foo": 86, "bar": 4.5}, {"fun": 43, "baz": 6.5}]'
        # looks a lot like python literals...
    In [96]: data2 = json.loads(s)
    Out[97]:
    [{u'that': 4, u'this': 5},
     {u'eggs': 3.4, u'spam': 7},
    ...
    In [98]: data2 == data
    Out[98]: True # they are the same


(also ``json.dump() and json.load()``  for files

http://docs.python.org/library/json.html

XML
---

XML is a standardized version of SGML, designed for use as a data storage / interchange format.

NOTE: HTML is also SGML, and modern versions conform to the XML standard.

XML in the python std lib
-------------------------

``xml.dom``

``xml.sax``

``xml.parsers.expat``

``xml.etree``

http://docs.python.org/library/xml.etree.elementtree.html

elementtree
-----------

The Element type is a flexible container object, designed to store hierarchical data structures in memory.

Essentially an in-memory XML -- can be read from / written-to XML

an ``ElementTree``  is an entire XML doc

an ``Element``  is a node in that tree

http://docs.python.org/library/xml.etree.elementtree.html}

LAB
---

::

    # load with:
    from add_book_data import AddressBook


They have address book data -- one with a nested dict, one "flat"

* Write a module that saves the data as an INI file

   - and reads it back in

* Write a module that saves the data as a CSV file

   - and reads it back in

* Write a module that saves the data in JSON

   - and reads it back in

* Write a module that saves the data in XML

   - and reads it back in

   - this gets ugly!


=========
DataBases
=========

anydbm
------

``anydbm``  is a generic interface to variants of the DBM database

Suitable for storing data that fits well into a python dict with strings as both keys and values

Note: anydbm will use the dbm system that works on your system -- this may be different on different systems -- so the db files may NOT be compatible! ``whichdb``  will try to figure it out, but it's not guaranteed

http://docs.python.org/library/anydbm.html

anydbm module
-------------
Writing data:

::

    #creating a dbm file:
    anydbm.open(filename, 'n')


flag options are:

* 'r' --  Open existing database for reading only (default)
* 'w' -- Open existing database for reading and writing
* 'c' --  Open database for reading and writing, creating it if it doesn’t exist
* 'n' -- Always create a new, empty database, open for reading and writing

http://docs.python.org/library/anydbm.html

anydbm module
-------------

``dbm``  provides dict-like interface:

::

    db = dbm.open("dbm", "c")
    db["first"] = "bruce"
    db["second"] = "micheal"
    db["third"] = "fred"
    db["second"] = "john" #overwrite
    db.close()
    # read it:
    db = dbm.open("dbm", "r")
    for key in db.keys():
        print key, db[key]



http://docs.python.org/library/anydbm.html


sqlite
------

SQLite: C library provides a lightweight disk-based single-file database

Nonstandard variant of the SQL query language

Very broadly used as as an embedded databases for storing application-specific data etc.

Firefox plug-in:

https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/


python sqlite module
--------------------

``sqlite3``  Python module wraps C lib -- provides standard DB-API interface

Allows (and requires) SQL queries

Can provide high performance, flexible, portable storage for your app

http://docs.python.org/library/sqlite3.html


.. nextslide::

Example:

::

    import sqlite3
    # open a connection to a db file:
    conn = sqlite3.connect('example.db')
    # or build one in-memory
    conn = sqlite3.connect(':memory:')
    # create a cursor
    c = conn.cursor()

http://docs.python.org/library/sqlite3.html

python sqlite module
--------------------

Execute SQL with the cursor:

::

    # Create table
    c.execute("'CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)"')
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # Save (commit) the changes
    conn.commit()
    # Close the cursor if we are done with it
    c.close()



http://docs.python.org/library/sqlite3.html

python sqlite module
--------------------

``SELECT``  creates an cursor that can be iterated:

::

    >>> for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print row
    (u'2006-01-05', u'BUY', u'RHAT', 100, 35.14)
    (u'2006-03-28', u'BUY', u'IBM', 1000, 45.0)
    ...


Or you can get the rows one by one or in a list:

::

     c.fetchone()
     c.fetchall()


python sqlite module
--------------------

Good idea to use the DB-API’s parameter substitution:

::

    t = (symbol,)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print c.fetchone()
    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)



http://xkcd.com/327/

DB-API
------

The DB-API spec (PEP 249) is a specification for interaction between Python and Relational Databases.}

Support for a large number of third-party Database drivers:

  * MySQL
  * PostgreSQL
  * Oracle
  * MSSQL (?)
  * .....

http://www.python.org/dev/peps/pep-0249}

=============
Other Options
=============

Object-Relation Mappers
-----------------------

Systems for mapping Python objects to tables

Saves you writing that glue code (and the SQL)

Usually deal with mapping to variety of back-ends:
 -- test with SQLite, deploy with PostreSQL

 SQL Alchemy
 -- http://www.sqlalchemy.org/

Django ORM
https://docs.djangoproject.com/en/dev/topics/db/

Object Databases
----------------

Directly store and retrieve Python Objects.

Kind of like ``shelve`` , but more flexible, and give you searching, etc.

ZODB: (http://www.zodb.org/

Durus: (https://www.mems-exchange.org/software/DurusWorks/})

NoSQL
-----
Map-Reduce, etc.

....Big deal for "Big Data": Amazon, Google, etc.

Document-Oriented Storage

* MongoDB (BSON interface, JSON documents)

* CouchDB (Apache):

  *  JSON documents

  *  Javascript querying (MapReduce)

  *  HTTP API


LAB
---

::
    # load with:
    from add_book_data import AddressBook

* Write a module that saves the data in a dbm datbase

  - and reads it back in

* Write a module that saves the data in an SQLItE datbase

  - and reads it back in

  - helps to know SQL here...


