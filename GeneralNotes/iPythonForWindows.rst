Installing and Running IPython for Windows:
###############################

It turns out that iPython works best when there are few other packages installed that it depends on, so it'snot quite as easy as simply instaling the one package.

these re some note put together by Dick Smith -- as he took the time to figure it out, We asked him to write up these notes:


Preconditions:
===================

(see: https://github.com/UWPCE-PythonCert/IntroToPython/blob/master/GeneralNotes/PythonOnWindows.rst for more detail)

Python Interpreter:
--------------------
32 or 64 bit version of Python for Windows 2.7 installed in C:\Python27\ 
(the version found at python.org)

PATH set:
-------------
MyComputer -> Properties -> Advanced System Settings -> System Variables
set up appropriately to modify PATH or path and create PYTHONPATH,
per install instructions.,

Getting packages:
===================
Use your web browser to navigate to this URL for downloadable
Python Windows extension installers recommended by the instructor:

"Unofficial Windows Binaries for Python Extension Packages
by Christoph Gohlke, Laboratory for Fluorescence Dynamics,
University of California, Irvine".

http://www.lfd.uci.edu/~gohlke/pythonlibs/

This is not a Git repository.  These are Windows-executable installers
which should be pulled to your PC's download directory.

Single-clicking will start the download process, then executed with a double-click.

NOTE: This repository containt both 32bit and 64bit pacakges -- make sure to get the ones that match the python installed.

Download and run these three installers, in this order:

SetupTools:  -- Required by the IPython install script.

setuptools-1.1.6.win32-py2.7.exe

PyReadline: -- Windows extension for adding color (and other nifty features) to the interactive
presentation.

pyreadline-2.0.win32-py2.7.exe

IPython itself:

ipython-1.1.0.win32-py2.7.exe

Run it by double-clicking on C:\Python27\Scripts\ipython.exe

or typing ``ipython`` on the command line (DOS box)

I recommend making a desktop shortcut and putting that in the target line.

It brings up a commandline console with some initial text about
resources available via commands, and the Ipython prompt:

  IN [1]:


