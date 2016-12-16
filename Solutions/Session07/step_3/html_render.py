#!/usr/bin/env python3

"""
Chris's solution through step 3
"""


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for just text

    This allows the Element classes to render either Element objects or
    plain text

    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


class Element:

    tag = "html"
    indent = "    "

    def __init__(self, content=None):
        self.content = []
        if content:
            # call the classes append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, content):
        """
        add a new piece of content or another element to this element
        """
        # note: this changed the internal represntation of content
        #       it no longer holds strings -- so a test will fail
        #       but that test was testing internal API --
        #       it's probably better remove it
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render(self, out_file, ind=""):
        out_file.write("{}<{}>\n".format(ind, self.tag))
        for stuff in self.content:
            stuff.render(out_file, ind + self.indent)
            out_file.write("\n")
        out_file.write("{}</{}>".format(ind, self.tag))


class OneLineTag(Element):
    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        out_file.write("{}<{}>".format(ind, self.tag))
        for stuff in self.content:
            stuff.render(out_file)
        out_file.write("</{}>".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


