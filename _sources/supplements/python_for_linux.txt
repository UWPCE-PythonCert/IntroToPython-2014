***********************************************************
Setting up Linux for Python and this class
***********************************************************

NOTE: this is from memory: no system to test on right now.

==================
Getting The Tools
==================

Python
-------

You probably already have python. But most distributions as of this date use python2 as the default. So you need to type ``python3`` to get version 3. Try:

.. code-block:: bash

  $ python3
  Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)
  Type "help", "copyright", "credits" or "license" for more information.

You can see what version you've got. If you don't have 3.4 or above, then you'll need to go try to find a newer version -- your distribution may have a package named something like:

.. code-block:: bash

   $ apt-get install python3.4

Or ``yum install`` or ???


Terminal
---------

Every Linux box has a terminal emulator -- find and use it.

git
----

git is likely to be there on your system already, but if not:

.. code-block:: bash

    $apt-get install git

or the equivalent for your system.

pip
---

``pip`` is the Python package installer. It is updated faster than python itself, so once you have python, you want to get the latest version of pip working::

  $ python3 -m ensurepip --upgrade

[first make sure that ``python`` gives you the one you want. You may need to call ``python3`` instead]

It should download and install the latest ``pip``.

You can now use pip to install other packages.


iPython
--------

One we are going to use in class is ``iPython``::

  $ python3 -m pip install ipython

You should now be able to run ``iPython``::

  $ ipython
  Python 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)
  Type "copyright", "credits" or "license" for more information.

  IPython 4.0.0 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object', use 'object??' for extra details.








