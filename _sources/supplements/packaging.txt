======================
Packages and Packaging
======================

Modules and Packages
--------------------

A module is a file (``something.py``) with python code in it

A package is a directory with an ``__init__.py``  file in it

And usually other modules, packages, etc...

::

    my_package
        __init__.py
        module_a.py
        module_b.py


.. code-block:: python

    import my_package


runs the code ``my_package/__init__.py`` (if there is any)

Modules and Packages
--------------------

.. code-block:: python

    import sys
    for p in sys.path:
        print p

(demo)

Installing Python
-----------------

Linux:

Usually part of the system -- just use it.

Windows:

Use the python.org version:

* System Wide

* Can install multiple versions if need be

* Third party binaries for it.

Installing Python
-----------------
OS-X:

Comes with the system, but:

    * Apple has never upgraded within a release
    * There are non-open source components
    * Third party packages may or may not support it
    * Apple does use it -- so don't mess with it
    * I usually recommend the ``python.org`` version

(Also Macports, Fink, Home Brew...)


Distributions
-------------

There are also a few "curated" distributions:

These provide python and a package management system for hard-to-buid packages.

Widely used by the scipy community
(lots of hard to build stuff that needs to work together...)

  * Anaconda (https://store.continuum.io/cshop/anaconda/)
  * Canopy (https://www.enthought.com/products/canopy/)
  * ActivePython (http://www.activestate.com/activepython)


Installing Packages
-------------------
Every Python installation has its own stdlib and ``site-packages`` folder

``site-packages``  is the default place for third-party packages

Finding Packages
----------------
The Python Package Index:

**PyPi**

http://pypi.python.org/pypi

Installing Packages
-------------------
.. rst-class:: medium

    **From source**

* (``setup.py install`` )

* With the system installer (apt-get, yum, etc...)

.. rst-class:: medium

    **From binaries:**

* Windows: MSI installers

* OS-X: dmg installers (make sure to get compatible packages)

* And now: binary wheels -- (More and more of those available)

* ``pip`` should find appropriate binary wheels if they are there.


.. nextslide::

In the beginning, there was the ``distutils``:

But ``distutils``  is missing some key features:

* package versioning
* package discovery
* auto-install

- And then came ``PyPi``

- And then came ``setuptools``

- But that wasn't well maintained...

- Then there was ``distribute/pip``

- Which has now been merged back into ``setuptools``

Now it's pretty stable: pip+setuptools: use them.

Installing Packages
-------------------

Actually, it's still a bit of a mess

But getting better, and the mess is *almost* cleaned up.

Current State of Packaging
--------------------------

To build packages: distutils

  * http://docs.python.org/2/distutils/

For more features: setuptools

  * https://pythonhosted.org/setuptools/

To install packages: pip

  * https://pip.pypa.io/en/latest/installing.html

For binary packages: wheels

  * http://www.python.org/dev/peps/pep-0427/

(installable by pip)

Compiled Packages
-----------------

Biggest issue is with compiled extensions:

  * (C/C++, Fortran, etc.)

  * You need the right compiler set up

Dependencies:

  * Here's were it gets really ugly

  * Particularly on Windows

.. nextslide::

**Linux**

Pretty straightforward:

1. Is there a system package?

  * use it (apt-get install the_package)

2. Try ``pip install``: it may just work!

3. Install the dependencies, build from source::

    python setup.py build

    python setup.py install

(may need "something-devel" packages)


.. nextslide::

**Windows**

Sometimes simpler:

1) A lot of packages have Windows binaries:

  - Usually for python.org builds
  - Excellent source: http://www.lfd.uci.edu/~gohlke/pythonlibs/
  - Make sure you get 32 or 64 bit consistent

2) But if no binaries:

  - Hope the dependencies are available!
  - Set up the compiler

MS now has a compiler just for python!

http://www.microsoft.com/en-us/download/details.aspx?id=44266

.. nextslide::

**OS-X**

Lots of Python versions:
  - Apple's built-in (different for each version of OS)
  - python.org builds
  - 32+64 bit Intel (and even PPC still kicking around)
  - Macports
  - Homebrew

Binary Installers (dmg or wheel) have to match python version

.. nextslide::

**OS-X**

If you have to build it yourself

Xcode compiler (the right version)

  - Version 3.* for 32 bit PPC+Intel

  - Version > 4.* for 32+64 bit Intel

(make sure to get the SDKs for older versions)

If extra dependencies:

  - macports or homebrew often easiest way to build them


Final Recommendations
---------------------

First try: ``pip install``

If that doesn't work:

Read the docs of the package you want to install

Do what they say

(Or use Anaconda or Canopy)

virtualenv
----------

``virtualenv`` is a tool to create isolated Python environments.

Very useful for developing multiple apps

Or deploying more than one app on one system

http://www.virtualenv.org/en/latest/index.html}

Remember the notes from the beginning of class? :ref:`virtualenv_section`

(Cris will probably make you do this next class)

============
Distributing
============

Distributing
------------
What if you need to distribute you own:

Scripts

Libraries

Applications


Scripts
-------

Often you can just copy, share, or check in the script to source
control and call it good.

But only if it's a single file, and doesn't need anything non-standard

When the script needs more than just the stdlib

(or your company standard environment)

You have an application, not a script


Libraries
---------

When you read the distutils docs, it's usually libraries they're talking about

Scripts + library is the same...

(http://docs.python.org/distutils/)

distutils
---------

``distutils``  makes it easy to do the easy stuff:

Distribute and install to multiple platforms, etc.

Even binaries, installers and compiled packages

(Except dependencies)

(http://docs.python.org/distutils/)

distutils basics
----------------

It's all in the ``setup.py file``:

.. code-block::python

    from distutils.core import setup
    setup(name='Distutils',
          version='1.0',
          description='Python Distribution Utilities',
          author='Greg Ward',
          author_email='gward@python.net',
          url='http://www.python.org/sigs/distutils-sig/',
          packages=['distutils', 'distutils.command'],
         )

(http://docs.python.org/distutils/)

distutils basics
----------------

Once your setup.py is written, you can:

::

    python setup.py ...
    build         build everything needed to install
    install       install everything from build directory
    sdist         create a source distribution
                  (tarball, zip file, etc.)
    bdist         create a built (binary) distribution
    bdist_rpm     create an RPM distribution
    bdist_wininst create an executable installer for MS Windows
    upload        upload binary package to PyPI

wheels
------

"wheels" are the "new" package format for python.

A wheel is essentially a zip file of the entire package, ready to be
unpacked in the right place on installation.

``pip`` will look for wheels for OS-X and Windows on PyPi, and auto-install
them if they exist

This is particularly nice for packages with non-python dependencies.


More complex packaging
----------------------

For a complex package:

You want to use a well structured setup:

http://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/

develop mode
------------

While you are developing your package, Installing it is a pain.

But you want your code to be able to import, etc. as though it were installed

``setup.py develop``  installs links to your code, rather than copies
-- so it looks like it's installed, but it's using the original source

``python setup.py develop``

You need ``setuptools`` and a setup.py  to use it.


Applications
------------

For a complete application:

  * Web apps
  * GUI apps

Multiple options:

  * Virtualenv + VCS
  * zc.buildout ( http://www.buildout.org/}
  * System packages (rpm, deb, ...)
  * Bundles...


Bundles
-------

Bundles are Python + all your code + plus all the dependencies --
all in one single "bundle"

Most popular on Windows and OS-X

::

     py2exe
     py2app
     pyinstaller
     ...


User doesn't even have to know it's python

Examples:

 http://www.bitpim.org/

 http://response.restoration.noaa.gov/nucos

LAB
---

Write a setup.py for a script of yours

  * Ideally, your script relies on at least one other module
  * At a minimum, you'll need to specify ``scripts``
  * and probably ``py_modules``
  * try:

    * ``python setup.py build``
    * ``python setup.py install``
    * ``python setup.py sdist``

  * EXTRA: install ``setuptools``

    * use: ``from setuptools import setup``
    * try: `` python setup.py develop``

  * EXTRA2: install ``wheel``

    * ``python setup.py bdist_wheel``


(my example: ``Examples/Session09/capitalize``)
