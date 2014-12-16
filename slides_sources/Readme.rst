******************************
Sources for Slides / Materials
******************************

This directory holds the source materials (RestructuredText, mostly) used
to build the slides and HTML pages for the class.

The ``old_versions`` dir has older version of the materials, done in LaTeX.
The contents are a bit different and have been updated. There are just
there for reference.

The documentation is written in `ReStructuredText`_ and output formats are
included for html, epub and `html5slides`_ (via the excellent `hieroglyph`_
package).

.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _html5slides: https://code.google.com/p/io-2012-slides/
.. _hieroglyph: http://docs.hieroglyph.io/en/latest/index.html


Building The Documents
======================

You will need a handful of Python packages to build this project. You may want to use `virtualenv`_ to help manage those dependencies. 

.. _virtualenv: http://virtualenv.org
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org:


First step is to clone this repository:

.. code-block:: bash

    $ git clone https://github.com/UWPCE-PythonCert/IntroToPython.git
    ...
    $ cd codefellows_f2_python

Once that is complete, you can install all the required packages with `pip`_:

.. _pip: http://www.pip-installer.org

.. code-block:: bash

    $ pip install -r requirements.txt

Finally, build the documentation using one of the output targets. To build the
plain html version, for example:

.. code-block:: bash

    $ make html
    sphinx-build -b html -d build/doctrees   source build/html
    Running Sphinx v1.2.2
    ...
    build succeeded.

    Build finished. The HTML pages are in build/html.

Or the html5 slides:

.. code-block:: bash

    $ make slides
    sphinx-build -b slides -d build/doctrees   source build/slides
    Running Sphinx v1.2.2
    ...
    Build finished. The HTML slides are in build/slides.


License
=======

Copyright 2014 Christopher Barker, Cris Ewing.

Thanks to Jon Jacky and Brian Dorsey, who developed the materials from which
this course was derived.

This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
International License.

To view a copy of this license, visit
`<http://creativecommons.org/licenses/by-sa/4.0/>`_ or send a letter to:

Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

A copy of this license in text format is included in this package in the LICENSE.txt file.
