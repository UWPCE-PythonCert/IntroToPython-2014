#!/usr/bin/env python

"""
Python class example.

Overriding render() again -- and a few more sub-classes.

"""

class Element(object):
    """
    An element with optional attributes and multiple items in the content
    """
    tag = ""
    indent = "    "
    def __init__(self, content=None, **attributes):
        """
        initialize an element with optional attributes, and any number of sub-elements and content

        :param content: content of the element:  single string or another element.
                        an empty string will be ignored
        :param [attributes]: optional attributes as keyword parameters.

        example:
        """
        if not content:
            self.children = []
        else:
            self.children = [content]

        self.attributes = attributes

    def append(self, element):
        self.children.append(element)

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(">")
        for child in self.children:
            try:
                child.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("\n")
                file_out.write(ind + self.indent)
                file_out.write(str(child))
        file_out.write("\n")
        file_out.write(ind)
        file_out.write('</%s>'%self.tag)

class Html(Element):
    tag = "html"

class Head(Element):
    tag = "head"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class SelfClosingTag(Element):
    """
    Element with a single tag -- no content, only attributes
    """
    def __init__(self, **attributes):
        self.attributes = attributes

    def render(self, file_out, ind = ""):
        """
        an html rendering method for self-closing elements:
        attributes, but no content a no closing tag
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(" />")

class Hr(SelfClosingTag):
    tag = "hr"

class OneLineTag(Element):

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"'%(key, value) )
        file_out.write(">")
        for child in self.children:
            try:
                child.render(file_out)
            except AttributeError:
                file_out.write(str(child))
        file_out.write('</%s>'%self.tag)

class Title(OneLineTag):
    tag = "title"


if __name__ == "__main__":
    import sys, cStringIO
    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    page.append(body)

    f = cStringIO.StringIO()

    page.render(f)

    f.reset()
    print f.read()

    f.reset()
    open("test_html.html", 'w').write(f.read())
