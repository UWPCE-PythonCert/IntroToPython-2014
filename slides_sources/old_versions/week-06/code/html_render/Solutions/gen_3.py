#!/usr/bin/env python

"""
Python class example.

over-riding a method...

"""

class Element(object):
    """
    An element with multiple items in the content
    """
    tag = ""
    indent = "    "
    def __init__(self, content=None):
        """
        initialize an element and any number of sub-elements and content

        :param content: content of the element:  single string or another element.
                        an empty string will be ignored

        example:
        """
        if not content:
            self.children = []
        else:
            self.children = [content]

    def append(self, element):
        self.children.append(element)

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
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

class OneLineTag(Element):

    def render(self, file_out, ind = ""):
        """
        an html rendering method for elements that have attributes and content
        """
        file_out.write("\n")
        file_out.write(ind)
        file_out.write("<%s"%self.tag)
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

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

    page.append(body)

    f = cStringIO.StringIO()

    page.render(f)

    f.reset()
    print f.read()

    f.reset()
    open("test_html.html", 'w').write(f.read())
