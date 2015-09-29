***********************************************************
Setting up Linux for Python and this class
***********************************************************


===============================================
Debian and Related Distros( Ubuntu, Mint )
===============================================

Python
-------

Ubuntu probably already has python2.7 and python3.4 both installed. Try the following commands:

.. code-block:: bash

  $ python2
  Python 2.7.9 (default, April 2 2015, 15:33:32) 
  [GCC 4.9.2 on linux2]
  >>>
  
.. code-block:: bash

  $ python3
  Python 3.4.3 (default, March 26 2015, 15:33:32) 
  [GCC 4.9.2 on linux]
  >>>

That's nice, which one is the default version? Just type ``python`` to see:

.. code-block:: bash

  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32) 
  [GCC 4.9.2 on linux2]
  >>>

If you want to make ``python3.4`` the default version then add the line ``alias python=python3`` to your user's ``/home/{user}/.bashrc`` file like so:

.. code-block:: bash

  $ # before
  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32) 
  [GCC 4.9.2 on linux2]
  >>>
  
  $ echo "alias python=python3" >> ~/.bashrc
  $ source ~/.bashrc 
  
  $ # after
  $ python
  Python 3.4.3 (default, March 26 2015, 15:33:32) 
  [GCC 4.9.2 on linux]
  >>>

If you don't have the version you want installed then use the package manager to find and install them:

.. code-block:: bash

   $ # search the package manager for it
   $ sudo apt-cache search python | grep '^python3.4\ -'
   python3.4 - Interactive high-level object-oriented language (version 3.4)
   $ # install it
   $ sudo apt-get install python3.4
   

Terminal
---------

Every Linux box has a terminal emulator -- find and use it. 


git
----

Git is likely to be there on your system already, but if not:

.. code-block:: bash

    $ sudo apt-get install git

pip
---

``pip`` is the Python package installer.

Many python packages are also available directly from your distro -- but you'll get the latest and greatest if you use ``pip`` to install it instead.

To get pip, the first option is to use your system package manager, something like:

.. code-block:: bash

    $ sudo apt-get install python3-pip

If that doesn't work, then look up the [official install notes](https://pip.pypa.io/en/latest/installing.html)

iPython
--------

One we are going to use in class is ``iPython``::

  $ sudo pip3 install ipython[all]

You should now be able to run ``iPython``::

    $ ipython3
	Python 3.4.3 () 
	Type "copyright", "credits" or "license" for more information.

	IPython 2.0.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.







