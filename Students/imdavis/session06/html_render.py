#!/usr/bin/env python

"""
Class for building up an HTML document from strings
"""

class Element(object):
    indent_spaces = "    "
    tag = "html"
    attrib = ""
    def __init__(self, content=None, **attributes):
        """
        If no content is passed in at initialization of the object, 
        initialize an empty list otherwise put the content passed in 
        into a list
        """
        if (not content):
            self.content = []
        else:
            self.content = [content]
        self.attributes = attributes

    def append(self, new_content):
        # append the new content to the list
        if new_content:
            self.content.append(new_content)

    def render_tag(self, current_ind):
        attribs = "".join([' {}="{}"'.format(k, v) for k, v in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_ind, self.tag, attribs)
        return tag_str

    def render(self, file_out, ind=""):
        """
        Be able to handle a string or an 'Element' object as and element
        of the self.content list
        """
        file_out.write(self.render_tag(ind))
        file_out.write("\n")
        # This could be a string or an Element object
        for obj in self.content:
            # if a string is the content, handle it this way
            try:
                file_out.write( ind + self.indent_spaces + obj + "\n" )
            # if an "Element" object is the content, handle this way
            # keeping track of indentation
            except (TypeError):
                obj.render(file_out, self.indent_spaces + ind )
        file_out.write("{}</{}>\n".format(ind, self.tag))

class Html(Element):
    tag = "html"
    def render(self, file_out, ind=""):
        """ 
        Extension of the render method inherited for this subclass to 
        write the DOCTYPE at the top of the page
        """
        file_out.write("<!DOCTYPE {}>\n".format(self.tag))
        Element.render(self, file_out, ind="")

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, file_out, ind=""):
        """
        Extend the render method we inherit from 'Element' to write the 
        title content and tags in a single line.
        """
        file_out.write(self.render_tag(ind))
        # print the contents of this object on the same line within the tag
        for obj in self.content:
            file_out.write(obj)
        file_out.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        """
        Extend the render method to render just the one tag and
        attributes, if any.
        """
        file_out.write(ind + "<{} />\n".format(self.tag))

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **attributes):
        OneLineTag.__init__(self, content, **attributes)
        self.attributes["href"] = link

class H(OneLineTag):
    def __init__(self, level, content=None, **attributes):
        OneLineTag.__init__(self, content, **attributes)
        self.tag = "h{}".format(level)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class Meta(SelfClosingTag):
    tag = "meta"
    def render(self, file_out, ind=""):
        """
        Override the SelfClosingTag render method we inherit to write the 
        content and tags in a single line with self closing tag
        """
        # Slice tag returned by 'render_tag' to remove the trailing '>'
        # after the tag contents
        file_out.write(self.render_tag(ind)[:-1])
        # Write the self closing tag with space
        file_out.write(" />\n")