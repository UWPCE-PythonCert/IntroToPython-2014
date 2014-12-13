.. _virtualenv_section:

***********************
Working with Virtualenv
***********************

.. rst-class:: medium

    "For every non-standard package installed in a system Python, the gods kill a
    kitten"

    - me

============
Reasons Why
============
.. rst-class:: left

    * As a working developer you will need to install packages that aren't in the
      Python standard Library
    * As a working developer you often need to install *different* versions of the
      *same* library for different projects
    * Conflicts arising from having the wrong version of a dependency installed can
      cause long-term nightmares
    * Use `virtualenv`_ ...
    * **Always**


Installing Virtualenv
---------------------

The best way is to install directly in your system Python (one exception to the
rule).

To do so you will have to have `pip`_ installed.

Try the following command:

.. code-block:: bash

    $ which pip
    /usr/local/bin/pip

If the ``which`` command returns no value for you, then ``pip`` is not
installed in your system. To fix this, follow `the instructions here`_.

Once you have ``pip`` installed in your system, you can use it to install
`virtualenv`_. Because you are installing it into your system python, you will
most likely need ``superuser`` privileges to do so:

.. code-block:: bash

    $ sudo pip install virtualenv
    Downloading/unpacking virtualenv
      Downloading virtualenv-1.11.2-py2.py3-none-any.whl (2.8MB): 2.8MB downloaded
    Installing collected packages: virtualenv
    Successfully installed virtualenv
    Cleaning up...

Great.  Once that's done, you should find that you have a ``virtualenv``
command available to you from your shell:

.. code-block:: bash

    $ virtualenv --help
    Usage: virtualenv [OPTIONS] DEST_DIR

    Options:
      --version             show program's version number and exit
      -h, --help            ...


.. _pip: http://www.pip-installer.org
.. _the instructions here: http://www.pip-installer.org/en/latest/installing.html

================
Using Virtualenv
================

.. rst-class:: left

    Creating a new virtualenv is very very simple:

    .. code-block:: bash

        $ virtualenv [options] <ENV>


    ``<ENV>`` is just the name of the environment you want to create. It's
    arbitrary. Let's make one for demonstration purposes:

    .. code-block:: bash

        $ virtualenv demoenv
        New python executable in demoenv/bin/python
        Installing setuptools, pip...done.

What Happened?
--------------

When you ran that command, a couple of things took place:

* A new directory with your requested name was created
* A new Python executable was created in <ENV>/bin (<ENV>/Scripts on Windows)
* The new Python was cloned from your system Python (where virtualenv was
  installed)
* The new Python was isolated from any libraries installed in the old Python
* Setuptools was installed so you have ``easy_install`` for this new python
* Pip was installed so you have ``pip`` for this new python

Activation
----------

The virtual environment you just created, ``demoenv`` contains an executable
Python command, but if you do a quick check to see which Python executable is
found by your terminal, you'll see that it is not the one:

.. code-block:: bash

    $ which python
    /usr/bin/python

You can execute the new Python by explicitly pointing to it:

.. code-block:: bash

    $ ./demoenv/bin/python -V
    Python 2.7.5

but that's tedious and hard to remember. Instead, ``activate`` your virtualenv
using the ``source`` command:

.. code-block:: bash

    $ source demoenv/bin/activate
    (demoenv)$ which python
    /Users/cewing/demoenv/bin/python

There.  That's better. Now whenever you run the ``python`` command, the
executable that will be used will be the new one in your ``demoenv``.

Notice also that the your shell prompt has changed. It indicates which
``virtualenv`` is currently active. Little clues like that really help you to
keep things straight when you've got a lot of projects going on, so it's nice
the makers of virtualenv thought of it.

Installing Packages
-------------------

Now that your virtualenv is active, not only has your ``python`` executable been
hijacked, so have ``pip`` and ``easy_install``:

.. code-block:: bash

    (demoenv)$ which pip
    /Users/cewing/demoenv/bin/pip
    (demoenv)$ which easy_install
    /Users/cewing/demoenv/bin/easy_install

This means that using these tools to install packages will install them *into
your virtual environment only* and not into the system Python.  Let's see this
in action. We'll install a package called ``docutils`` that provides support
for converting ReStructuredText documents into other formats like HTML, LaTeX
and more:

.. code-block:: bash

    (demoenv)$ pip install docutils
    Downloading/unpacking docutils
      Downloading docutils-0.11.tar.gz (1.6MB): 1.6MB downloaded
      Running setup.py (path:/Users/cewing/demoenv/build/docutils/setup.py) egg_info for package docutils
        ...
        changing mode of /Users/cewing/demoenv/bin/rst2xml.py to 755
        changing mode of /Users/cewing/demoenv/bin/rstpep2html.py to 755
    Successfully installed docutils
    Cleaning up...

And now, when we fire up our Python interpreter, the docutils package is
available to us:

.. code-block:: pycon

    (demoenv)$ python
    Python 2.7.5 (default, Aug 25 2013, 00:04:04)
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import docutils
    >>> docutils.__path__
    ['/Users/cewing/demoenv/lib/python2.7/site-packages/docutils']
    >>> ^d
    (demoenv)$

There's one other interesting side-effect of installing software with
``virtualenv``. The ``docutils`` package provides a number of executable
scripts when it is installed: ``rst2html.py``, ``rst2latex.py`` and so on.
These scripts are set up to execute using the Python with which they were
built.  What this means is that running these scripts will use the Python
executable in your virtualenv, *even if that virtualenv is not active*!

Deactivation
------------

So you've got a virtual environment created.  And you've activated it so that
you can install packages and use them. Eventually you'll need to move on to
some other project. This likely means that you'll need to stop working with
this ``virtualenv`` and switch to another (it's a good idea to keep a separate
``virtualenv`` for every project you work on).

When a ``virtualenv`` is active, all you have to do is use the ``deactivate``
command:

.. code-block:: bash

    (demoenv)$ deactivate
    $ which python
    /usr/bin/python

Note that your shell prompt returns to normal, and now the executable Python
found when you check ``python`` is the system one again.

Cleaning Up
-----------

The final great advantage that ``virtualenv`` confers on you as a developer is
the ability to easily remove a batch of installed Python software from your
system. Consider a situation where you installed a library that breaks your
Python (it happens).  If you are working in your system Python, you now have to
figure out what that package installed, where, and go clean it out manually.
With ``virtualenv`` the process is as simple as removing the directory that
virtualenv created when you started out. Let's do that with our ``demoenv``:

.. code-block:: bash

    $ rm -rf demoenv

And that's it.  The entire environment and all the packages you installed into
it are now gone. There's no traces left to pollute your world.

VirtualenvWrapper
=================

So you have this great tool that allows you to build isolated environments in
which you can install Python software. Several questions arise when considering
this.

* Where should such environments be placed?
* How can the environments be tied to the projects you are working on?
* Once you have more than a trivial number of projects, how can you keep track
  of all these virtualenvs?

Like any good tool, ``virtualenv`` does not impose on you any particular way of
working. You can place your environments into the directories where you are
building the project to which they apply. You can keep them all in a single
global location. You can build a random path generator that drops them
wherever.

But any of these methods lead inevetably to chaos. They require too much from
you. It would be better if you could manage your virtual environments easily
and intuitively.

With `virtualenvwrapper`_ you can.

Installation
------------

Let's start by installing the package in our system Python, alongside
``virtualenv`` (again, you'll need ``superuser`` to do this):

.. code-block:: bash

    $ sudo pip install virtualenvwrapper
    Downloading/unpacking virtualenvwrapper
      Downloading virtualenvwrapper-4.2.tar.gz (125kB): 125kB downloaded
      Running setup.py (path:/private/tmp/pip_build_root/virtualenvwrapper/setup.py) egg_info for package virtualenvwrapper
      ...
    Successfully installed virtualenvwrapper virtualenv-clone stevedore
    Cleaning up...
    $

Once that's finished, you'll need to wire the system up by letting your shell
know that the commands it provides are present. Add the following lines to your
shell startup file (``.profile``, ``.bash-profile``, ...):

.. code-block:: bash

    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

This will create a new environmental variable, ``WORKON_HOME``, that determines
where new virtual environments will be created. The actual name is completely
arbitrary.

You'll need to be sure that the location you set exists:

.. code-block:: bash

    $ mkdir ~/.virtualenvs

Using ``mkvirtualenv``
----------------------

When you've done that, start a new terminal and you'll have access to the
``mkvirtualenv`` command:

.. code-block:: bash

    $ mkvirtualenv testenv
    New python executable in testenv/bin/python
    Installing setuptools, pip...done.
    (testenv)$ ls ~/.virtualenvs
    testenv
    (testenv)$ which python
    /Users/cewing/.virtualenvs/testenv/bin/python
    (testenv)$

Notice a couple of things:

* The new environment you asked for was created in ``WORKON_HOME``
* The new environment was *immedately* activated for you

That's a nice feature, eh? No more needing to remember to ``activate`` the env
you just created to install packages.

Using ``workon``
----------------

In addition to this nice little feature, you can also use the ``workon``
command to see which environments you have, and to switch from one to another:

.. code-block:: bash

    (testenv)$ workon
    testenv
    (testenv)$ mkvirtualenv number2
    New python executable in number2/bin/python
    Installing setuptools, pip...done.
    (number2)$ workon
    number2
    testenv
    (number2)$ workon testenv
    (testenv)$

Sweet!

The same ``deactivate`` command can get you back to your system environment:

.. code-block:: bash

    (testenv)$ deactivate
    $

Using ``mkproject``
-------------------

That takes care of deciding where to put new environments. It also clears up
the question of how to remember which ones you have and how to start them up
and switch between them. But we still have to figure out how to remember which
environment goes with which project.

That's what the ``mkproject`` command is for.

First, go back to your shell startup file and add a new environmental variable:

.. code-block:: bash

    export PROJECT_HOME=~/projects #<- this line here is new
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

Then, make sure the directory you named exists:

.. code-block:: bash

    $ mkdir ~/projects

After all that, fire up a new shell to pick up the changes and try this:

.. code-block:: bash

    $ mkproject foo
    New python executable in foo/bin/python
    Installing setuptools, pip...done.
    Creating /Users/cewing/projects/foo
    Setting project for foo to /Users/cewing/projects/foo
    (foo)$ which python
    /Users/cewing/.virtualenvs/foo/bin/python
    (foo)$ pwd
    /Users/cewing/projects/foo
    (foo)$ ls -a $VIRTUAL_ENV
    .       .Python     bin     lib
    ..      .project    include
    (foo)$ more $VIRTUAL_ENV/.project
    /Users/cewing/projects/foo

Whoa! That command did a lot:

* Created a new ``virtualenv`` in your ``$WORKON_HOME``
* Created a new project directory in your ``$PROJECT_HOME``
* Placed a ``.project`` file in your home directory with a path leading to the
  associated project directory
* Activated the new virtualenv for you
* Automatically moved your present working directory to the new project
  directory.

And now, you can begin working on your ``foo`` project, secure that you will be
installing packages into the right environment.

A Few Last Words
================

This quick introduction is **by no means** an exhaustive manual for either of
the packages we've talked about. There is a great deal more that they can do.
In particular, ``virtualenvwrapper`` is highly customizable, with support for
custom scripts to be hooked into every stage of the ``virtualenv`` workflow.

I urge you to read the documentation for `virtualenv`_ and `virtualenvwrapper`_
yourself to find out more.

.. _virtualenv: http://www.virtualenv.org/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org
