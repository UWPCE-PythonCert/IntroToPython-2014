=========================
Using Python on Windows
=========================

Python itself is very platform independent. The code you write will be exactlty the same regardless of platform you are running, unless you want to acess specific system services. However, the tools required to install and work with python and associated packages are somewhat different. Also, as Python comes from, and is mostly used by, the FOSS world, many instructions you will find online are *nix oriented, and many packages are set up and tested primarily on Linux and/or OS-X.

Nevertheless, Python works just fine on Windows once you get yourself properly set up.

The following are few notes that should help you get running on Windows.

[NOTE: these notes are oriented to supporting the UWPCE Certificate in Python Programming classes]

Installing Python
====================

There are a number of Python distributions out there, some specifically designed to provide a full featured set of packages, often oreinted to scientific programming. These include: Enthought Canopy, Continuum's Anaconda, and Python(xy). However the prome advantage of these sywtems is getting hard-to-build-and-install scientific packages -- they maynot be as useful for the UW certificate program. So we will recommend a more compact route:

python.org binaries
---------------------

We recommend the binary installer available from python.org:

<http://python.org/download/>

We are using VErsion 2.7 for this class. Either 32bit or 64bit is fine, although you may have an easier time finding binary packages (see below) for the 32bit version.

setting up the `PATH`
---------------------------

The installer will install to a stardard location, and set itself up in the registry and Start menu. However, for command line use, you will want to put the appropriate locations on your `PATH`. The `PATH` environemnt variable tells the commadn line shell where to look for executables. by adding teh appropriate directory, you can simply type "`python`" on the command line to run python. You will want to add tow directories to the `PATH`::

    C:\Python27
    C:\Python27\Scripts

The `Scripts` dir is where Python puts scripts installed by python packages -- ti is very handy to have it on your `PATH` as well.

Add `";C:\Python27;C:\Python27\Scripts"` (without the quotes) to the end of your DOS path environment variable by following the instructions (these are copied from here: <http://www.ehow.com/how_7781683_add-path.html> )

Instructions
 1. Click on the Windows "Start" button and then click "Control Panel" from the menu that appears.
 2. Click "System" in the Windows control panel, then click "Advanced system settings" to open the "System Properties" dialog box.

 3. Click the "Environment Variables" button on the "Advanced" tab of the dialog box.

4. Scroll down in the "System variables" box until you see the "Path" variable. Click on the "Path" entry to highlight, then click the "Edit" button underneath the box.

5. Add a semicolon to the end of the current path line, which is used as a delimiter, and then type the directory path to add. Click "OK" until all the dialog boxes are closed.

6. Restart any open command windows to allow the changeto take effect.

Read more: <http://www.ehow.com/how_7781683_add-path.html#ixzz2evrTwviw>

Opening a command Window ("DOS box")
--------------------------------------
 a) click Start
 b) click Run...
 c) type "cmd" (without the quotes) in the text entry field
 d) click OK

"Command line here"
---------------------
"Command line here" is a utility for the file explorer tht lets you open up a command window already set the the vcurrent directory seen in Windows Explorer. A little googling should find it -- it's very handy. (I think it's built in to Windows 7)


Installing Packages
=====================

While python has a "batteries included" philosphy, and there is a lot of great stuff in the standard library, there will come a time when you'll want to use a thord party package (or many of them...)

Python packages come (more or less) in three flavors, in order of difficulty to install.

    Pure Python
        Packages that contain only python code are pretty easy -- python is very platfrom independt, so the same code runs everywhere, and there is no need for compilation.

    Python and C extension code
        Some packages have some modeuls written in C - known as "extansion modules". These modules need to be compiled for the host system before they can be used.

    Python and Extension code with dependencies
        Some packages include not jsut C code, but that C code depends on other third party libraries that do not come with the operating system. Some of these are designed specifically to give python users access to a C lib, and some simply need a given lib to due its job. Examples of comonl used C libs: libpng, libcurl, libfreetype, etc.

distutils
-----------

The distutils ("distribution utilities") is a pacakge that comes with all recent version of python -- it provides a standrad and robust way to build, install, and distribute packges. IF you encounter a `setup.py` file, you are using distutils.

Installing from source
------------------------

Often you will find a package on the web somewhere, and the develper will provide a zip file or tarball of the package source. In this package, there will most likely be a `setup.py file`. To install the package, you simply run teh command::

  python setup.py install

You can also build and install in separate steps::

  python setup.py build
  python setup.py install

If the package is pure python, this should "just work". However, if the package includes a python extension, it will only work if you have a C compiler installed properly. The best option is Microsoft Visual Studio 2008 (the express addtion is fine, and free). Instaling all that is beyond the scope of this note, but once installed, again, running `setup.py install` should work.

However, if the package contains a module that depends on a third-party libary, then you need to figure out how to build and install that first -- this is not for teh faint of heart, and not recommended for people without experience building software on Windows. Which brings us to:


Installing from binaries
--------------------------

As many (most) Windows users do not have (nor know how to use) a compiler, and there is now binary pacakge management system for Windows (like apt-get or rpm for Linux), most pacakge maintainers disribute binaries of their packages for Windows. If they don't, there are often third-party binary packages available. IN this case, they are almost always built for the versions of python available from `python.org`.

At the web site for the pacakge of interest, look for a binary installer (usually a MSI installer). Make sure it is for the python version (2.7) you are running, and (very important!) the bit-depth of your python (32 or 64 bit). For example, wxPython has the following binaries available::

    wxPython2.9-win32-py26	32-bit Python 2.6
    wxPython2.9-win64-py26	64-bit Python 2.6
    wxPython2.9-win32-py27	32-bit Python 2.7
    wxPython2.9-win64-py27	64-bit Python 2.7

Make sure you download the correct version, or you will get a cryptic error message.

Once you get it, you can point-and-click install it and you should be good to go.

Binary Repositories
---------------------

There are few repositories of Windows binary pacakges that may have what you are looking for. Msot notable is the repository maintained by Christoph Gohlke: <http://www.lfd.uci.edu/~gohlke/pythonlibs/>. This is an outstanding resource -- a really remarkable collectin of up to date packages for Windows. Again, be sure to download the version that matches your python installation.


`pip` and `easy_install`
==========================

`pip` and `easy_install` are systems that seek to automatically find a package you are looking for in the python package index (pypi: https://pypi.python.org/pypi) and install them for you. They work great on all systems for pure-python pacakges, but often fail with more complex packages. To install a package::

  pip install package_name

as easy as that. `pip` and 'easy_install` also track pacakge dependencies, and try to install them for you as well. It's great when it works.

installing `pip`
---------------

Installing `pip` requires a bit of a "bootstrap" process. First you need to install `setuptools`:<https://pypi.python.org/pypi/setuptools/1.1.5>. To isntall setuptools, look for the `ez_setup.py` on the setuptools page, download it, and run it::

  python ez_setup.py

That should install the latest setuptools. Once that's done, you should be able install pip with easy_install::

  easy_install pip

whew! that was harder than it should be.



2. Add ";C:\Python27;C:\Python27\Scripts" (without the quotes) to the end of your DOS path environment variable. For instructions try:
     http://www.ehow.com/how_7781683_add-path.html

Note: if you already have a cmd window open, you'll need to close and re-open it after doing step 2.

3. Open a cmd window:
     a) click Start
     b) click Run...
     c) type "cmd" (without the quotes) in the text entry field
     d) click OK

4. In the cmd window type: "easy_install swampy" (without the quotes).


And two more steps to get iPython and pyreadline:

5. In the cmd window type: "easy_install iPython" (without the quotes).

6. In the cmd window type: "easy_install pyreadline" (without the quotes).



- - - - - - - - - - - - Step 4. should look like this: - - - - - - - - - - - - -

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\Python27>easy_install swampy
Searching for swampy
Reading http://pypi.python.org/simple/swampy/
Reading http://allendowney.com/swampy
Best match: swampy 2.1.1
Downloading http://pypi.python.org/packages/source/s/swampy/swampy-2.1.1.tar.gz#
md5=a302348a849da33cb454fde993fb9757
Processing swampy-2.1.1.tar.gz
Running swampy-2.1.1\setup.py -q bdist_egg --dist-dir c:\docume~1\daniel\locals~
1\temp\easy_install-q4vdfv\swampy-2.1.1\egg-dist-tmp-gh3rvr
zip_safe flag not set; analyzing archive contents...
swampy.Lumpy: module MAY be using inspect.stack
Adding swampy 2.1.1 to easy-install.pth file

Installed c:\python27\lib\site-packages\swampy-2.1.1-py2.7.egg
Processing dependencies for swampy
Finished processing dependencies for swampy



- - - - - - - - - - - - Step 5. should look like this: - - - - - - - - - - - - -

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\Documents and Settings\Daniel>easy_install iPython
Searching for iPython
Reading http://pypi.python.org/simple/iPython/
Reading http://ipython.scipy.org
Reading http://ipython.scipy.org/dist
Reading http://ipython.scipy.org/dist/0.8.4
Reading http://ipython.scipy.org/dist/0.9.1
Reading http://ipython.org
Reading http://archive.ipython.org/release/0.12.1
Reading https://github.com/ipython/ipython/downloads
Reading http://ipython.scipy.org/dist/old/0.9
Reading http://ipython.scipy.org/dist/0.10
Reading http://archive.ipython.org/release/0.11/
Reading http://archive.ipython.org/release/0.12
Best match: ipython 0.13
Downloading http://pypi.python.org/packages/2.7/i/ipython/ipython-0.13-py2.7.egg
#md5=694ce5981bf163922bd09617a4742a61
Processing ipython-0.13-py2.7.egg
creating c:\python27\lib\site-packages\ipython-0.13-py2.7.egg
Extracting ipython-0.13-py2.7.egg to c:\python27\lib\site-packages
Adding ipython 0.13 to easy-install.pth file
Installing ipcontroller-script.py script to C:\Python27\Scripts
Installing ipcontroller.exe script to C:\Python27\Scripts
Installing ipcontroller.exe.manifest script to C:\Python27\Scripts
Installing iptest-script.py script to C:\Python27\Scripts
Installing iptest.exe script to C:\Python27\Scripts
Installing iptest.exe.manifest script to C:\Python27\Scripts
Installing ipcluster-script.py script to C:\Python27\Scripts
Installing ipcluster.exe script to C:\Python27\Scripts
Installing ipcluster.exe.manifest script to C:\Python27\Scripts
Installing ipython-script.py script to C:\Python27\Scripts
Installing ipython.exe script to C:\Python27\Scripts
Installing ipython.exe.manifest script to C:\Python27\Scripts
Installing pycolor-script.py script to C:\Python27\Scripts
Installing pycolor.exe script to C:\Python27\Scripts
Installing pycolor.exe.manifest script to C:\Python27\Scripts
Installing iplogger-script.py script to C:\Python27\Scripts
Installing iplogger.exe script to C:\Python27\Scripts
Installing iplogger.exe.manifest script to C:\Python27\Scripts
Installing irunner-script.py script to C:\Python27\Scripts
Installing irunner.exe script to C:\Python27\Scripts
Installing irunner.exe.manifest script to C:\Python27\Scripts
Installing ipengine-script.py script to C:\Python27\Scripts
Installing ipengine.exe script to C:\Python27\Scripts
Installing ipengine.exe.manifest script to C:\Python27\Scripts

Installed c:\python27\lib\site-packages\ipython-0.13-py2.7.egg
Processing dependencies for iPython
Finished processing dependencies for iPython



- - - - - - - - - - - - Step 6. should look like this: - - - - - - - - - - - - -

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\Documents and Settings\Daniel>easy_install pyreadline
Searching for pyreadline
Reading http://pypi.python.org/simple/pyreadline/
Reading http://ipython.scipy.org/moin/PyReadline/Intro
Reading https://launchpad.net/pyreadline/+download
Reading http://projects.scipy.org/ipython/ipython/wiki/PyReadline/Intro
Best match: pyreadline 2.0-dev1
Downloading https://launchpad.net/pyreadline/2.0/pyreadline-2.0-prerelease/+down
load/pyreadline-2.0-dev1.win32.exe
Processing pyreadline-2.0-dev1.win32.exe
creating 'c:\docume~1\daniel\locals~1\temp\easy_install-ndbace\pyreadline-2.0_de
v1-py2.7-win32.egg' and adding 'c:\docume~1\daniel\locals~1\temp\easy_install-nd
bace\pyreadline-2.0_dev1-py2.7-win32.egg.tmp' to it
Moving pyreadline-2.0_dev1-py2.7-win32.egg to c:\python27\lib\site-packages
Adding pyreadline 2.0-dev1 to easy-install.pth file

Installed c:\python27\lib\site-packages\pyreadline-2.0_dev1-py2.7-win32.egg
Processing dependencies for pyreadline
Finished processing dependencies for pyreadline