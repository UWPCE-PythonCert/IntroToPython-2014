.. _homework_html_renderer:

==================================
HTML Renderer Homework Assignment
==================================

HTML Render
============

Goal:
------

The goal is to create a set of classes to render html pages -- in a "pretty printed" way. i.e nicely indented and human readable. We'll try to get to all the features required to render:

:download:`sample_html.html  <./sample_html.html>`

The exercise is broken down into a number of steps -- each requiring a few more OO concepts in Python.

General Instructions:
---------------------

For each step, add the required functionality. There is example code to run your code for each step in: ``code\session06\run_html_render.py``

name your file: ``html_render.py`` -- so it can be imported by ``run_html_render.py``

You should be able to run that code at each step, uncommenting each new step in ``run_html_render.py`` as you go.

It builds up a html tree, and then calls the ``render()`` method of your element to render the page.

It uses a ``cStringIO`` object (like a file, but in memory) to render to memory, then dumps it to the console, and writes a file. Take a look at the code at the end to make sure you understand it.

The html generated at each step is in the files: ``test_html_ouput?.html``

At each step, your results should look similar that those (maybe not identical...)


Step 1:
-------

Create an ``Element`` class for rendering an html element (xml element).

It should have class attributes for the tag name ("html" first) and the indentation (spaces to indent for pretty printing)

The constructor signature should look like

.. code-block:: python

    Element(content=None)

where ``content`` is a string

It should have an ``append`` method that can add another string to the content.

It should have a ``render(file_out, ind = "")`` method that renders the tag and the strings in the content.

``file_out`` could be any file-like object ( i.e. have a ``write()`` method ).

.. nextslide::

``ind`` is a string with the indentation level in it: the amount that the tag should be indented for pretty printing.

 - This is a little tricky: ``ind`` will be the amount that this element should be indented already. It will be from zero (an empty string) to a lot of spaces, depending on how deep it is in the tree.

The amount of indentation should be set by the class attribute: ``indent``

NOTE: don't worry too much about indentation at this stage -- the primary goal is to get proper, compliant html. i.e. the opening and closing tags rendered correctly. Worry about cleaning up the indentation once you've got that working.

You should now be able to render an html tag with text in it as contents.

See: step 1. in ``run_html_render.py``

Step 2:
--------

Create a couple subclasses of ``Element``, for a ``html``, ``<body>``, and ``<p>`` tag. All you should have to do is override the ``tag`` class attribute (you may need to add a ``tag`` class attribute to the Element class first...).

Now you can render a few different types of element.

Extend the ``Element.render()`` method so that it can render other elements inside the tag in addition to strings. Simple recursion should do it. i.e. it can call the ``render()`` method of the elements it contains. You'll need to be smart about setting the ``ind`` optional parameter -- so that the nested elements get indented correctly.

Figure out a way to deal with the fact that the contained elements could be either simple strings or ``Element`` s with render methods (there are a few ways to handle that...).

You should now be able to render a basic web page with an html tag around
the whole thing, a ``<body>`` tag inside, and multiple ``<p>`` tags inside that, with text inside that. And all indented nicely.

See ``test_html_output2.html``

NOTE: when you run step 2 in ``run_html_render.py``, you will want o comment out step 1 -- that way you'll only get one set of output.

Step 3:
--------

Create a ``<head>`` element -- simple subclass.

Create a ``OneLineTag`` subclass of ``Element``:

* It should override the render method, to render everything on one line -- for the simple tags, like::

    <title> PythonClass - Session 6 example </title>

Create a ``Title`` subclass of ``OneLineTag`` class for the title.

You should now be able to render an html doc with a head element, with a
title element in that, and a body element with some ``<P>`` elements and some text.

See ``test_html_output3.html``

Step 4:
--------

Extend the ``Element`` class to accept a set of attributes as keywords to the
constructor, ie. (``run_html_render.py``)

.. code-block:: python

    Element("some text content", id="TheList", style="line-height:200%")

( remember ``**kwargs``? )

The render method will need to be extended to render the attributes properly.

You can now render some ``<p>`` tags (and others) with attributes

See ``test_html_output4.html``

Step 5:
--------

Create a ``SelfClosingTag`` subclass of Element, to render tags like::

   <hr /> and <br /> (horizontal rule and line break).

You will need to override the render method to render just the one tag and
attributes, if any.

Create a couple subclasses of ``SelfClosingTag`` for and <hr /> and <br />

See ``test_html_output5.html``

Step 6:
-------

Create a ``A`` class for an anchor (link) element. Its constructor should look like::

    A(self, link, content)

where link is the link, and content is what you see. It can be called like so::

    A(u"http://google.com", u"link to google")

You should be able to subclass from ``Element``, and only override the ``__init__`` --- Calling the ``Element`` ``__init__`` from the  ``A __init__``

You can now add a link to your web page.

See ``test_html_output6.html``

Step 7:
--------

Create ``Ul`` class for an unordered list (really simple subclass of ``Element``)

Create ``Li`` class for an element in a list (also really simple)

Add a list to your web page.

Create a ``Header`` class -- this one should take an integer argument for the
header level. i.e <h1>, <h2>, <h3>, called like

.. code-block:: python

   H(2, "The text of the header")

for an <h2> header

It can subclass from ``OneLineTag`` -- overriding the ``__init__``, then calling the superclass ``__init__``

See ``test_html_output7.html``

Step 8:
--------

Update the ``Html`` element class to render the "<!DOCTYPE html>" tag at the head of the page, before the html element.

You can do this by subclassing ``Element``, overriding ``render()``, but then calling the ``Element`` render from the new render.

Create a subclass of ``SelfClosingTag`` for ``<meta charset="UTF-8" />`` (like for ``<hr />`` and ``<br />`` and add the meta element to the beginning of the head element to give your document an encoding.

The doctype and encoding are HTML 5 and you can check this at: http://validator.w3.org.

You now have a pretty full-featured html renderer -- play with it, add some
new tags, etc....

See ``test_html_output8.html``


HTML Primer
============

.. rst-class:: medium

    The very least you need to know about html to do this assigment.

If you are familar with html, then this will all make sense to you. If you have
never seen html before, this might be a bit intimidating, but you really don't
need to know much to do this assignment.

First of all, sample output from each step is provided. So all you really need
to do is look at that, and make your code do the same thing. But it does help to
know a little bit about what you are doing.

HTML
----

HTML is "Hyper Text Markup Language". Hypertext, because it can contain links
to other pages, and markup language means that text is "marked up" with
instructions about how to format the text, etc.

Here is a good basic intro:

http://www.w3schools.com/html/html_basic.asp

And there are countless others online.

But here is a tiny intro of just what you need to know for this project.

Elements
--------

Modern HTML is a particular dialect of XML (eXrensible Markup Language),
which is itself a special case of SGML (Standard Generalized Markup Language)

It inherits from SGML a basic structure: each piece of the document is an element. each element is described by a "tag". each tag has a different meaning, but they all have the same structure::

    <some_tag> some content </some_tag>

that is, the tag name is surrounded by < and >, which marks the beginning of
the element, and the end of the element is indicated by the same tag with a slash.

The real power is that these elements can be nested arbitrarily deep. In order to keep that all readable, we often want to indent the content inside the tags, so it's clear what belongs with what. That is one of the tricky bits of this assignment.

Basic tags
----------

.. code-block:: html

    <html> is the core tag indicating the entire document </html>

    <p> is a single paragraph of text </p>

    <body> is the tag that indicated the text of the document </body>

    <head> defines the header of the document -- a place for metadata </head>

Attributes:
------------

In addition to the tag name and the content, extra attributes can be attached to a tag. These are added to the "opening tag", with name="something", another_name="somethign else" format:

.. code-block:: html

    <p style="text-align: center; font-style: oblique;">

There can be all sorts of stuff stored in attributes -- some required for specific tags, some extra, like font sizes and colors. Note that since tags can essentially have any attributes, your code will need to support that -- doesn't it kind of look like a dict? And keyword arguments?

Special Elements
----------------

The general structure is everything is between and opening and closing tag. But some elements don't really have content -- just attributes. So the slash goes at the end of the tag, after the attributes. We can call these self-closing tags:

.. code-block:: html

   <meta charset="UTF-8" />

To make a link, you use an "anchor" tag: ``<a>``. It required attributes to indicate what the link is:

.. code-block:: html

    <a href="http://google.com">link</a>

the ``href`` attribute is the link (hyper reference).

To make a bulleted list, you use a <ul> tag (unordered list), and inside that, you put individual list elements <li>:

.. code-block:: html

        <ul style="line-height:200%" id="TheList">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
        </ul>

Note that the list itself, and the list items can both take various attributes (all tags can...)

Section Headers are created with "h" tags: <h1> is the biggest (highest level), and there is <h2>, <h3>, etc. for sections, sub sections, subsub sections.

.. code-block:: html

    <h2>PythonClass - Class 6 example</h2>

I think that's all you need to know!





