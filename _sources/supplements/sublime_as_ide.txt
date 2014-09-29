**************************************************
Turning Sublime Text Into a Lightweight Python IDE
**************************************************


A solid text editor is a developer's best friend. You use it constantly and it
becomes like a second pair of hands. The keyboard commands you use daily
become so engrained in your muscle memory that you stop thinking about them
entirely.

With Sublime Text, it's possible to turn your text editor into the functional
equivalent of a Python IDE.  The best part is you don't have to install an IDE
to do it.

Requirements
============

Here are *my* requirements for an 'IDE':

* It should provide excellent, configurable syntax colorization.
* It should allow for robust tab completion.
* It should offer the ability to jump to the definition of symbols in other
  files.
* It should perform automatic code linting to help avoid silly mistakes.
* It should be able to interact with a Python interpreter such that when
  debugging, the editor will follow along with the debugger.


Which Version?
==============

Version 2 will be fine, but I would urge you to consider updating to version 3.
Some of the plugins I recommend are not available for version 2.


Basic Settings
==============

All configuration in Sublime Text is done via `JSON`_. It's simple to learn. go
and read that link then return here.

There are a number of `different levels of configuration`_ in Sublime Text. You
will most often work on settings at the user level.

.. _JSON: http://www.json.org
.. _different levels of configuration: http://www.sublimetext.com/docs/3/settings.html

Open ``Preferences`` -> ``Settings - Default`` to see all the default settings
and choose which to override.

Create your own set of preferences by opening ``Preferences`` -> ``Settings -
User``. This will create an empty file, you can then copy the settings you want
to override from the default set into your personal settings.

Here's a reasonable set of preliminary settings (theme, color scheme and font
are quite personal, find ones that suit you.):

.. code-block:: json

    source

    {
        "color_scheme": "Packages/User/Cobalt (SL).tmTheme",
        "theme": "Soda Light 3.sublime-theme",
        // A font face that helps distinguish between 0 (the number) and 'O' (the letter)
        // among other problem characters.
        "font_face": "DroidSansMonoSlashed",
        // getting older. I wonder if comfy font size increases as a linear
        //  function of age?
        "font_size": 15,
        "ignored_packages":
        [
            // I'm not a vi user, so this is of no use to me.
            "Vintage"
        ],
        "rulers":
        [
            // set text rulers so I can judge line length for pep8
            72, // docstrings
            79, // optimum code line length
            100  // maximum allowable length
        ],
        "word_wrap": false, // I hate auto-wrapped text.
        "wrap_width": 79 // This is used by a plugin elsewhere
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "use_tab_stops": true,
    }


Especially important is the setting ``translate_tabs_to_spaces``, which ensures
that any time you hit a tab key, the single ``\t`` character is replaced by four
``\s`` characters.  In Python this is **vital**!


Extending the Editor
====================

Most of the requirements above go beyond basic editor function. Use Plugins.

Sublime Text comes with a great system for `Package Control`_. It handles
installing and uninstalling plugins, and even updates installed plugins for
you. You can also manually install plugins that haven't made it to the big-time
yet, including `ones you write yourself`_. Happily, the plugin system is
Python!

.. _Package Control: https://sublime.wbond.net
.. _ones you write yourself: http://docs.sublimetext.info/en/latest/extensibility/plugins.html


To install a plugin using Package Control, open the ``command palette`` with
``shift-super-P`` (``ctrl-shift-P`` on Windows/Linux). The ``super`` key is ``command``
or ``⌘`` on OS X. When the palette opens, typing ``install`` will bring up the
``Package Control: Install Package`` command. Hit ``enter`` to select it.

.. image:: /_static/pc_menu.png
    :width: 600px
    :align: center
    :alt: The package control command in the command palette.

After you select the command, Sublime Text fetches an updated list of packages
from the network. It might take a second or two for the list to appear. When it
does, start to type the name of the package you want. Sublime Text filters the
list and shows you what you want to see. To install a plugin, select it with
the mouse, or use arrow keys to navigate the list and hit ``enter`` when your
plugin is highlighted.

.. image:: /_static/plugin_list.png
    :width: 600px
    :align: center

Useful Plugins
==============

Here are the plugins I've installed to achieve the requirements above.

Autocompletion
--------------

By default, Sublime Text will index symbols in open files and projects, but
that doesn't cover installed python packages that may be part of a non-standard
run environment.

There are two to choose from:

1. `SublimeCodeIntel`_ offers strong support for multiple languages through
   it's own plugin system.  It is a bit heavy and requires building an index.
2. `SublimeJedi`_ only supports Python, but is faster and keeps an index on its
   own.

.. _SublimeCodeIntel: https://sublime.wbond.net/packages/SublimeCodeIntel
.. _SublimeJedi: https://sublime.wbond.net/packages/Jedi%20-%20Python%20autocompletion

I've installed ``SublimeJedi``, and used the following settings *per project* to
ensure that all relevant code is found:

.. code-block:: json

    {
        "folders":
        [
            // ...
        ],

        "settings": {
            // ...
            "python_interpreter_path": "/Users/cewing/pythons/python-2.7/bin/python",

            "python_package_paths": [
                "/path/to/project/buildout/parts/omelette"
            ]
        }
    }

The ``python_interpreter_path`` allows me to indicate which Python executable
should be introspected for symbol definitions.

The ``python_package_paths`` setting allows designating additional paths that
will be searched for Python packages containing symbols. 

.. image:: /_static/tab_completion.png
    :width: 600px
    :align: center
    :alt: Tab completion provided by SublimeJedi

Once configured, you should be able to use the ``ctrl-shift-G`` keyboard
shortcut to jump directly to the definition of a symbol. You can also use
``alt-shift-F`` to find other usages of the same symbol elsewhere in your code.

Code Linting
------------

Code linting shows you mistakes you've made in your source *before* you attempt
to run the code. This saves time. Sublime Text has an available plugin for code
linters called `SublimeLinter`_.

.. _SublimeLinter: http://sublimelinter.readthedocs.org/en/latest/


Python has a couple of great tools available for linting, the `pep8`_ and
`pyflakes`_ packages. ``Pep8`` checks for style violations, lines too long,
extra spaces and so on. ``Pyflakes`` checks for syntactic violations, like
using a symbol that isn't defined or importing a symbol you don't use.

Another Python linting package, `flake8`_ combines these two, and adds in
`mccabe`_, a tool to check the `cyclomatic complexity`_ of code you write. This
can be of great help in discovering methods and functions that could be
simplified and thus made easier to understand and more testable.


.. _pep8: https://pypi.python.org/pypi/pep8
.. _pyflakes: https://pypi.python.org/pypi/pyflakes
.. _flake8: https://pypi.python.org/pypi/flake8
.. _mccabe: https://pypi.python.org/pypi/mccabe
.. _cyclomatic complexity: http://en.wikipedia.org/wiki/Cyclomatic_complexity

There is a nice plugin for the SublimeLinter that `utilizes flake8`_. For it to
work, the plugin will need to have a Python executable that has the Python
tools it needs installed.

Use `virtualenv`_ to accomplish this. First, create a virtualenv and activate
it:

.. _utilizes flake8: https://sublime.wbond.net/packages/SublimeLinter-flake8
.. _virtualenv: http://virtualenv.org

.. code-block:: bash

    $ cd /Users/cewing/virtualenvs
    $ virtualenv sublenv
    New python executable in sublenv/bin/python
    Installing setuptools, pip...done.
    $ source sublenv/bin/activate
    (sublenv)$

Then use Python packaging tools to install the required packages:

.. code-block:: bash

    (sublenv)$ pip install flake8
    Downloading/unpacking flake8
    [...]
    Downloading/unpacking pyflakes>=0.7.3 (from flake8)
    [...]
    Downloading/unpacking pep8>=1.4.6 (from flake8)
    [...]
    Downloading/unpacking mccabe>=0.2.1 (from flake8)
    [...]
    Installing collected packages: flake8, pyflakes, pep8, mccabe
    [...]
    Successfully installed flake8 pyflakes pep8 mccabe
    Cleaning up...
    (sublenv)$

The Python executable for this ``virtualenv`` now has the required packages
installed. You can look in ``/path/to/sublenv/bin`` to see the executable
commands for each:

    (sublenv)$ ls sublenv/bin
    activate            easy_install-2.7    pip2.7
    activate.csh        flake8              pyflakes
    activate.fish       pep8                python
    activate_this.py    pip                 python2
    easy_install        pip2                python2.7

Now install SublimeLinter and then SublimeLinter-flake8 using Package Control.

Here are the settings you can add to ``Preferences`` -> ``Package Settings`` ->
``SublimeLinter`` -> ``Settings - User``:

.. code-block:: json

    {
        //...
        "linters": {
            "flake8": {
                "@disable": false,
                "args": [],
                "builtins": "",
                "excludes": [],
                "ignore": "",
                "max-complexity": 10,
                "max-line-length": null,
                "select": ""
            }
        },
        //...
        "paths": {
            "linux": [],
            "osx": [
                "/Users/cewing/virtualenvs/sublenv/bin"
            ],
            "windows": []
        },
        "python_paths": {
            "linux": [],
            "osx": [
                "/Users/cewing/virtualenvs/sublenv/bin"
            ],
            "windows": []
        },
        //...
    }

The ``paths`` key points to the path that contains the ``flake8`` executable
command.

The ``python_paths`` key points to the location of the python executable to be
used.

The settings inside the ``flake8`` object control the performance of the
linter. `Read more about them here`_.

.. _Read more about them here: https://github.com/SublimeLinter/SublimeLinter-flake8#settings

.. image:: /_static/flake8_output.png
    :width: 600px
    :align: center
    :alt: Flake8 shows unused import and trailing whitespace issues.

White Space Management
----------------------

One of the issues highlighted by ``flake8`` is trailing spaces.  Sublime text
provides a setting that allows you to remove them every time you save a file:

.. code-block:: json

    source

    {
        "trim_trailing_whitespace_on_save": true
    }

**Do not use this setting**

Removing trailing whitespace by default causes a *ton* of noise in commits.

Keep commits for stylistic cleanup separate from those that make important
changes to code.

The `TrailingSpaces`_ SublimeText plugin can help with this.

.. _TrailingSpaces: https://github.com/SublimeText/TrailingSpaces

Here are the settings you can use:

.. code-block:: json

    {
        //...
        "trailing_spaces_modified_lines_only": true,
        "trailing_spaces_trim_on_save": true,
        // ...
    }

This allows trimming whitespace on save, but *only on lines you have directly
modified*. You can still trim *all* whitespace manually and keep changesets
free of noise.

Follow-Along
------------

The final requirement for a reasonable IDE experience is to be able to follow a
debugging session in the file where the code exists.

There is no plugin for SublimeText that supports this. But there is a Python
package you can install into the virtualenv for each of your projects that does
it.

The package is called `PDBSublimeTextSupport`_ and its simple to install with ``pip``:

.. _PDBSublimeTextSupport: https://pypi.python.org/pypi/PdbSublimeTextSupport

.. code-block:: bash

    (projectenv)$ pip install PDBSublimeTextSupport

With that package installed in the Python that is used for your project, any
breakpoint you set will automatically pop to the surface in SublimeText.  And
as you step through the code, you will see the current line in your Sublime
Text file move along with you.

