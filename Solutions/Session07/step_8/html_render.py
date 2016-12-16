#!/usr/bin/env python3

"""
Chris's solution through step 8
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

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            # call the classes append method
            # so that it can do anything special it needs to do
            self.append(content)

    def append(self, content):
        """
        add a new piece of content or another element to this element
        """
        # note: this changed the internal representation of content
        #       it no longer holds strings -- so a test will fail
        #       but that test was testing internal API --
        #       it's probably better remove it
        # if isinstance(content, Element):
        if hasattr(content, 'render'):
           self.content.append(content)
        else:
           self.content.append(TextWrapper(str(content)))
        # self.content.append(content)


    def make_tags(self):
        """
        create the tags
        -- in a separate method so different subclass's render methods can use it
        """
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag

    def render(self, out_file, cur_ind=""):
        print("in render, type of self", type(self))
        open_tag, close_tag = self.make_tags()
        out_file.write(cur_ind + open_tag + "\n")
        for stuff in self.content:
            stuff.render(out_file, cur_ind + self.indent)
            out_file.write("\n")
        out_file.write(cur_ind + close_tag)


class OneLineTag(Element):
    def render(self, out_file, cur_ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag, close_tag = self.make_tags()
        out_file.write(cur_ind + open_tag)
        for stuff in self.content:
            try:
                stuff.render(out_file)
            except AttributeError:
                out_file.write(stuff)
        out_file.write(close_tag)


class Html(Element):
    tag = 'html'

    def render(self, file_out, cur_ind=""):
        file_out.write(cur_ind + "<!DOCTYPE html>\n")
        super().render(file_out, cur_ind=cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    """
    base class for tags that have no content
    """
    def render(self, out_file, ind=""):
        # there is some repition here -- maybe factor that out?
        open_tag, _ = self.make_tags()
        # make it a self cloding tag by adding the /
        out_file.write(ind + open_tag.replace(">", " />"))


class Hr(SelfClosingTag):
    """
    Horizontal Rule
    """
    tag = "hr"


class Br(SelfClosingTag):
    """
    Line break
    """
    tag = "br"


class A(OneLineTag):
    """
    anchor element
    """
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)
        # this could also be direct:
        # Element.__init__(self, content, **kwargs)


class Ul(Element):
    """
    unordered list
    """
    tag = "ul"


class Li(Element):
    """
    list element
    """
    tag = "li"


class H(OneLineTag):
    """
    section head
    """
    tag = "H"

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    """
    metadata tag
    """
    tag = "meta"
