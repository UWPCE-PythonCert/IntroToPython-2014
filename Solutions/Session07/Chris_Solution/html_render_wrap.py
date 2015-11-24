#!/usr/bin/env  python

"""
html render code -- this version wraps plain text in a simple class for rendering.
"""


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


class Element:

    tag = 'html'  # shouldn't really be usable without properly subclassing
    indent = '    '

    def __init__(self, content=None, **attributes):

        self.content = []
        self.attributes = attributes

        if content is not None:
            # call this class's append -- so any changes will work
            self.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def render_tag(self, current_ind):
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')
        for con in self.content:
            con.render(file_out, current_ind+self.indent)
            file_out.write("\n")
        file_out.write("{}</{}>\n".format(current_ind, self.tag))


class OneLineTag(Element):
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        # is there ever more than one in a OneLineTag?
        for con in self.content:
            con.render(file_out)
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind)[:-1])
        file_out.write(" />\n")


class Meta(SelfClosingTag):
    tag = "meta"

    def __init__(self, content=None, **attributes):
        # give it a default value for charset
        if "charset" not in attributes:
            attributes['charset'] = "UTF-8"
        SelfClosingTag.__init__(self, content, **attributes)


class Hr(SelfClosingTag):
    tag = 'hr'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **attributes):
        OneLineTag.__init__(self, content, **attributes)
        self.attributes["href"] = link


class H(OneLineTag):
    def __init__(self, level, content=None, **attributes):
        OneLineTag.__init__(self, content, **attributes)
        self.tag = "h{:d}".format(level)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Html(Element):
    tag = 'html'

    def render(self, file_out, current_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, current_ind=current_ind)


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'
