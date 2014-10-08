***********************************************************
Setting up Windows for Python and this class
***********************************************************

NOTE: this is from memory: no system to test on right now.

==================
Getting The Tools
==================

Python
-------

There are a number of python distributions available -- many designed for easier support of scientific programming:

Anaconda
Enthought Canopy
Python(x,y)

But for core use, the installer from python.org is the way to go:

https://www.python.org/downloads/

You want the installer for Python 2.7.8 -- probably 64 bit, though if you have a 32 bit sytem, you can get that. There is essentially no difference for the purposes of this course.

Double click and install.


Terminal
---------

You can use the "DOS Box" as a terminal, though the newer "powershell" is a better option.

But to use the Python in the terminal efectively, you need to put a couple paths on your "PATH" environment variable:

http://www.computerhope.com/issues/ch000549.htm

You want to add:

``C:\Python2.7``

and

``C:\Python2.7\Scripts``

to ``PATH``


git
----

Get a git client -- the gitHub GUI client may be nice -- I honestly don't know.

There is also TortoiseGit:

https://code.google.com/p/tortoisegit/

which integrates git with the filemanager. But for the purposes of learning, it may be better to use a command line client:

http://git-scm.com/download/win

I think that gives you a "Git bash shell" -- a command window that gives you a \*nix - like command line shell.


pip
---

``pip`` is the Python package installer. Unfortunately, it doesn't come out of the box with Python2.7, so you need to install it:

https://pip.pypa.io/en/latest/installing.html

download ``get-pip.py`` from that site, and run it with python::

  $ python get-pip.py

It should download and install ``pip`` (and ``setuptools``)

You can now use pip to install other packages.

iPython
--------

One we are going to use in class is ``iPython``::

  $ pip install ipython

You should now be able to run ``iPython``::

    $ ipython
	Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
	Type "copyright", "credits" or "license" for more information.

	IPython 2.0.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.







