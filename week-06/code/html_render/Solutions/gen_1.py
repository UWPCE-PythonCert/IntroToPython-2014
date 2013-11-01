#!/usr/bin/env python

"""
Python class example.

This is the first Element base class ---

"""

class Element(object):
    """
    An element with multiple items in the content
    """
    tag = "html"
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
            file_out.write("\n")
            file_out.write(ind + self.indent)
            file_out.write(child)
        file_out.write("\n")
        file_out.write(ind)
        file_out.write('</%s>'%self.tag)


if __name__ == "__main__":
    import sys, cStringIO
    page = Element()

    page.append("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

    page.append("And here is another piece of text -- you should be able to add any number")

    f = cStringIO.StringIO()

    page.render(f)

    f.reset()
    print f.read()

    f.reset()
    open("test_html.html", 'w').write(f.read())
