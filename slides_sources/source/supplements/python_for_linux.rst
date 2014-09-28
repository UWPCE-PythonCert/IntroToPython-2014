***********************************************************
Setting up Linux for Python and this class
***********************************************************

NOTE: this is from memory: no system to test on right now.

==================
Getting The Tools
==================

Python
-------

You probably already have python. Try:

.. code-block:: bash

  $ python
  Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on linux

You can see what version you've got. If you don't have 2.7.*, then you'll need to go try to find a newer version -- your distribution may have a package named something like:

.. code-block:: bash

   $ apt-get install python2.7

Or ``yum install`` or ???


Terminal
---------

Every Linux box has a terminal emulator -- find and use it. 



git
----

git is likely to be there on your system already, but if not:

.. code-block:: bash

    $apt-get install git

pip
---

``pip`` is the Python package installer.

Many python packages are also available directly from your distro -- but you'll get the latest and greatest if you use ``pip`` to install it instead.

To get pip, the first option is to use your system package manager, something like:

.. code-block:: bash

    $apt-get install python-pip

If that doesn't work, you can get it from:

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







