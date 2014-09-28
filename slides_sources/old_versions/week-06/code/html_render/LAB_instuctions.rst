
Instructions for html renderer exercise:
###########################################

Goal:
======

A set of classes to render html pages. we'll try to get to all the features required to render::
      
    sample_html.html

The exercise is broken down into a number of steps -- each requiring a bit more OO concepts in Python. WE will complete a step or two, then learn a bit more about OO in Python, then do a few more steps.

General Instructions:
======================

For each step, add the required functionality. There is example code to run your code for each step in: ``LAB_calling_code.rst(html)``. You should be abel to run that code at each step, and then call the ``render()`` method to render your page. You may want to use sys.stdout to render to the terminal::

  import sys
  ....
  page.render(sys.stdout)

or you can use a regular file::

  outfile = open('test.html', 'w')
  ...
  page.render(outfile)

or use a cStringIO object (like a file, but in memory)::

    import cStringIO
    
    ...
    
    f = cStringIO.StringIO()

    page.render(f)

    # now print it to the screen:
    f.reset()
    print f.read()

Solutions:
============

There are versions of the instructors' solution to each step in ``code/html_render/solutions``, so you can look at a solution if you get stuck, But do try to figure it out yourself, first. 


Step 1:
=========

Create an ``Element`` class for rendering an html element (xml element). 
  
It should have class attributes for the tag name ("html" first) and the indentation (spaces to indent for pretty printing)
  
The constructor signature should look like::

    Element(content=None)

where ``content`` is a string

It should have an ``append`` method that can add another string to the content
  
It should have a ``render(file_out, ind = "")`` method that renders the tag
and the strings in the content.

``file_out`` could be any file-like object (i.e have a ``write()`` method ).
     
``ind`` is a string with the indentation level in it -- i.e the amount that the tag should be indented for pretty printing (maybe 4 spaces per level).

The amount of indentation should be set by the class attribute: ``indent``
     
You can test with ``sys.stdout`` to print to the console, and/or use a
``cStringIO.sStringIO`` object to store it in a string - or pass a file
     
You should now be able to render an html tag with text in it as contents.
     
Step 2:
==========

Create a couple subclasses of ``Element``, for a <body> tag and <p> tag. All you should have to do is override the ``tag`` class attribute (you may need to add a ``tag`` class attribute to the Element class...).

Now you can render a few different types of element.
   
Extend the ``Element.render()`` method so that it can render other elements
inside the tag in addition to strings. Simple recursion should 
do it. i.e. it can call the ``render()`` method of the elements it contains.

Figure out a way to deal with the fact the the contents elements could be
either simple strings or Elements with render methods...(there are a few
ways to handle that...)

You should now be able to render a basic web page with an html tag around
the whole thing, and body tag inside, and multiple <p> tags inside that,
with text inside that.

Step 3:
==========

Create a <head> element -- simple subclass.

Create a ``OneLineTag`` subclass of ``Element``:

It should override the render method, to render everything on one line -- for the simple tags, like::
    
    <title> PythonClass - Class 6 example </title>
    
Create a ``Title`` subclass of ``OneLineTag`` class for the title.
  
You should now be able to render an html doc with a head element, with a
title element in that, and a body element with some <P> elements and some text.
  
Step 4:
===========

Extend the ``Element`` class to accept a set of attributes as keywords to the
constructor, ie.::
  
    Element("some text content", id="TheList", style="line-height:200%")

( remember ``**kwargs``? )
  
The render method will need to be extended to render the attributes properly.

You can now render some <p> tags (and others) with attributes  
    
Step 5:
========

Create a ``SelfClosingTag`` subclass of Element, to render tags like::
   
   <hr /> and <br /> (horizontal rule and line break).
   
You will need to override the render method to render just the one tag and
attributes, if any.
   
Create a couple subclasses of ``SelfClosingTag`` for and <hr /> and <br />
   
Step 6: 
==========

Create a ``A`` class for an anchor (link) element. Its constructor should look like::

    A(self, link, content)

where link is the link, and content is what you see. It can be called like so::
       
    A("http://google.com", "link")
    
You should be able to subclass from ``Element``, and only override the ``__init__`` --- Calling the ``Element`` ``__init__`` from the  ``A __init__``
       
You can now add a link to your web page.
    
Step 7:
===========

Create ``Ul`` class for an unordered list (really simple subclass of ``Element``)
   
Create ``Li`` class for an element in a list (also really simple)
   
Add a list to your web page.
   
Create a ``Header`` class -- this one should take an integer argument for the
header level. i.e <h1>, <h2>, <h3>, called like::
   
   H(2, "The text of the header") for an <h2> header
   
It can subclass from ``OneLineTag`` -- overriding the ``__init__``, then calling the superclass ``__init__``
   
Step 8:
==========

Update the ``Html`` element class to render the "<!DOCTYPE html>" tag at the
head of the page, before the html element.
   
You can do this by subclassing ``Element``, overriding ``render()``, but then
calling the ``Element`` render from the new render.
   
Create a subclass of ``SelfClosingTag`` for <meta charset="UTF-8" /> (like
for <hr /> and <br /> and add the meta element to the beginning of
the head element to give your document an encoding.
   
The doctype and encoding are HTML 5 and you can check this at:
http://validator.w3.org.
   
You now have a pretty full-featured html renderer -- play with it, add some
new tags, etc....


   