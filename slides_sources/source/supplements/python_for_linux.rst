******************************
Setting Up Python For Linux 
******************************


==================================================
Debian and Related Distros (Ubuntu, Linux Mint)
==================================================

Python
-------

Debian distros already have the stable python2 and python3 releases preinstalled [`1 <Debian Wiki>`_]. Try the following commands:

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

That's nice, which one is the default version? Just type ``python`` to see. It's probably python2 still:

.. code-block:: bash

  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32) 
  [GCC 4.9.2 on linux2]
  >>>

If you want to make ``python3.4`` the default version then add the line ``alias python=python3`` to your user's ``/home/{user}/.bashrc`` file like so:

.. code-block:: bash

  $ # before the change
  $ python
  Python 2.7.9 (default, April 2 2015, 15:33:32) 
  [GCC 4.9.2 on linux2]
  >>>
  
  $ echo "alias python=python3" >> ~/.bashrc
  $ source ~/.bashrc 
  
  $ # after the change
  $ python
  Python 3.4.3 (default, March 26 2015, 15:33:32) 
  [GCC 4.9.2 on linux]
  >>>

If you don't have the version you want installed then use the package manager to find and install it:

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

If that doesn't work, then look up the `official manual install notes <https://pip.pypa.io/en/latest/installing.html>`_

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



==================================================
Fedora and Red Hat Related Distros (CentOS)
==================================================

<h4 style="color:red">WARNING:</h4><span>CentOS is probably the most popular distor of these related flavors. However, getting Python3 on it can be a pain. You have been warned</span>
	
Python
-------

Fedora distros already have the stable python2 and python3 releases preinstalled `[2] <Fedora Wiki>`_. However, CentOS, the most popular distro only has the stable python2 release. Try the following commands:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ python2
	Python 2.7.5 (default, Jun 17 2014, 18:11:42) 
	[GCC 4.8.2 20140120 (Red Hat 4.8.2-16)] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> 
	
	[centos@ip-172-31-21-5 ~]$ python3
	-bash: python3: command not found
 

Let's install python3 using the package manager. Step one install `Software Collections` to help us:

.. code-block:: bash

   $ sudo yum -y install scl-utils

Then go to the `software collections listing <https://www.softwarecollections.org/en/scls/>`_ and click on the python collection version you want to install. Note, you also need to know which version of CentOS you are using (probably 6 or 7). For example, we care about `python version 3.4` so let's go the `.rpm` i want to install `here <https://www.softwarecollections.org/repos/rhscl/rh-python34/epel-7-x86_64/noarch/>`_:

.. code-block:: bash
	$ # add this package to the rpm package manager
	$ sudo rpm -Uvh https://www.softwarecollections.org/repos/rhscl/rh-python34/epel-7-x86_64/noarch/rhscl-rh-python34-epel-7-x86_64.noarch.rpm
	
	$ # install the right python version
	$ sudo yum install rh-python34

When you want to use python3 run this command:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ scl enable rh-python34 bash
	

   

Terminal
---------

Every Linux box has a terminal emulator -- find and use it. 


git
----

Git is likely to be there on your system already, but if not:

.. code-block:: bash

    $ sudo yum install git
    
pip
---

``pip`` is the Python package installer.

Many python packages are also available directly from your distro -- but you'll get the latest and greatest if you use ``pip`` to install it instead.

In CentOS, if you used the above technique to install Python3, then it comes with pip. Try:

.. code-block:: bash

	[centos@ip-172-31-21-5 ~]$ pip -V
	pip 1.5.6 from /opt/rh/rh-python34/root/usr/lib/python3.4/site-packages (python 3.4)

iPython
--------

One we are going to use in class is ``iPython``::

  $ sudo pip install ipython[all]

You should now be able to run ``iPython``::

    $ ipython3
	Python 3.4.3 () 
	Type "copyright", "credits" or "license" for more information.

	IPython 2.0.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.


Footnotes:
===========

Debian Wiki
=============
	https://wiki.debian.org/Python

Fedora Wiki
=============
	https://fedoraproject.org/wiki/Packaging:Python
	
