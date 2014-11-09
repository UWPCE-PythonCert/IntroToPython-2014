#!/usr/bin/env python

"""
Class for building up an HTML document from strings
"""

class Element(object):
    indent_spaces = "    "
    tag = "html"
    def __init__(self, content=None):
        """
        If no content is passed in at initialization of the object, 
        initialize an empty list otherwise put the content passed in 
        into a list
        """
        if (not content):
            self.content = []
        else:
            self.content = [content]
    def append(self, new_content):
        # append the new content to the list
        if new_content:
            self.content.append(new_content)
    def render(self, file_out, ind=""):
        """
        Be able to handle a string or an 'Element' object as and element
        of the self.content list
        """
        start_tag = "<"  + self.tag + ">" + "\n"
        end_tag   = "</" + self.tag + ">" + "\n"
        file_out.write(ind + start_tag)
        # This could be a string or an Element object
        for obj in self.content:
            # if a string is the content, handle it this way
            try:
                writeline = "    " + ind + obj + "\n"
                file_out.write(writeline)
            # if an "Element" object is the content, handle this way
            # keeping track of indentation
            except (TypeError):
                obj.render(file_out, ind=(self.indent_spaces + ind) )
        file_out.write(ind + end_tag)

class Html(Element):
    tag = "html"
    def render(self, file_out, ind=""):
        """ 
        Extension of the render method inherited for this subclass to 
        write the DOCTYPE at the top of the page
        """
        file_out.write("<!DOCTYPE " + self.tag + ">" + "\n") 
        Element.render(self, file_out, ind="")

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Title(Element):
    tag = "title"
    def render(self, file_out, ind=""):
        """
        Override the render class we inherit from 'Element' to write the 
        title content and tags in a single line.
        """
        start_tag = ind + "<"  + self.tag + ">"
        end_tag   = "</" + self.tag + ">"
        content = "".join(self.content)
        file_out.write(start_tag + content + end_tag + "\n")
