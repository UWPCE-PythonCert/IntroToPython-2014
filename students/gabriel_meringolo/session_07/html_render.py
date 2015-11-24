

class Element:
    tag = "html"
    atts = ""
    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind="    "):
        if self.attributes != {}:
            for key, value in self.attributes.items():
                self.atts += ' {}="{}"'.format(key, value)
        else:
            self.atts = ""
        start_tag = "<{}{}>".format(self.tag, self.atts)
        f.write(start_tag + "\n")
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(ind + str(el) + "\n")
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag + "\n")


class A(Element):
    tag = "a"

    def __init__(self, link, content):
        self.link = link
        self.content = content

    def render(self, f, ind="    "):
        f.write(ind + '<{} href="{}">{}</{}>'.format(self.tag, self.link, self.content, self.tag) + "\n")


class OneLineTag(Element):

    def render(self, f, ind="    "):
        f.write("<{}>".format(self.tag))
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        f.write("</{}>".format(self.tag) + "\n")


class SelfClosingTag(Element):

    def render(self, f, ind="    "):
        if self.attributes != {}:
            for key, value in self.attributes.items():
                self.atts += ' {}="{}"'.format(key, value)
        else:
            self.atts = ""
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        f.write("<{}{} />".format(self.tag, self.atts) + "\n")


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"

    def render(self, f, ind="    "):
        f.write("<!DOCTYPE {}>\n".format(self.tag))
        Element.render(self, f, ind="    ")


class Head(Element):
    tag = "head"


class Ul(Element):
    tag = "ul"


class Li(Element):
    tag = "li"


class Title(OneLineTag):
    tag = "title"


class H(OneLineTag):
    tag = "h"

    def __init__(self, num, text):
        self.tag += str(num)
        self.content = text


class Meta(SelfClosingTag):
    tag = "meta"


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"





