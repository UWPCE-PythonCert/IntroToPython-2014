*****************************
Setting up Windows for Python
*****************************

==================
Getting The Tools
==================

Python
-------

There are a number of python distributions available -- many designed for easier support of scientific programming:

- Anaconda
- Enthought Canopy
- Python(x,y)

But for core use, the installer from python.org is the way to go:

https://www.python.org/downloads/

You want the installer for Python 3.4.3 -- probably 64 bit, though if you have a 32 bit sytem, you can get that. There is essentially no difference for the purposes of this course.

Double click and install.


Terminal
---------

If you are confident in your use of the "DOS Box" or "powershell", feel free to use one of those. However, your life may be easier if you install "Git Bash", as then you can follow unix-style terminal instructions exactly, and do not have to translate. Also, your instructors are more experienced with Bash.

When you install Git Bash, you are installing git (and a git gui) as well, thus killing two birds with one stone, metaphorically speaking.

https://git-for-windows.github.io/

This is actually your best bet for running Python also -- If you use the Git Bash shell, you can use the same commands as Linux and OS-X users. Regardless of which shell you choose, you will need to add Python to your environment. It is possible that this was done during the installation of python. If you type 'which python' into your terminal, and get back the answer '/c/python34/python', then you are good to go, otherwise, follow the instructions here:

http://www.computerhope.com/issues/ch000549.htm

You will want to add:

``C:\Python34``

and

``C:\Python34\Scripts``

to ``PATH``


git
----

If you installed Git Bash, you will already have git, both usable in the terminal and as a gui, and can safely skip this section. If not, you still need a git client. You can use the above link and install git (it will install the bash shell as well, of course, but you can use your shell of choice instead).

There is also TortoiseGit:

https://code.google.com/p/tortoisegit/

which integrates git with the file manager. Feel free to use this if you already have an understanding of how git works, but for the purposes of learning, it may be better to use a command line client (git Bash above).

pip
---

``pip`` is the Python package installer. It is updated faster than python itself, so once you have python you want to get the latest version of pip working::

  $ python -m ensurepip --upgrade

It should download and install the latest ``pip``.

You can now use pip to install other packages.

iPython
--------

One extra package we are going to use in class is ``iPython``::

  $ pip install ipython

You should now be able to run ``iPython`` from the git bash shell::

    $ ipython
	Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35)
	Type "copyright", "credits" or "license" for more information.

	IPython 2.0.0 -- An enhanced Interactive Python.
	?         -> Introduction and overview of IPython's features.
	%quickref -> Quick reference.
	help      -> Python's own help system.
	object?   -> Details about 'object', use 'object??' for extra details.

(or from the DOS box or PowerShell prompt)

We will use this as our default python interpreter.


