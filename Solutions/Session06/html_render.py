#!/usr/bin/env  python

"""
html render code
"""


class Element(object):

    tag = 'html'
    indent = '    '

    def __init__(self, content=None, **attributes):

        self.content = []
        self.attributes = attributes

        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render_tag(self, current_ind):
        attrs = "".join([' {}="{}"'.format(key,val) for key, val in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_ind, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')
        #print "in render:"
        #print self.content
        for con in self.content:
            #print "trying to render:", con
            try:
                file_out.write( current_ind + self.indent + con+"\n")
            except TypeError:
                con.render(file_out, current_ind+self.indent)
        file_out.write("{}</{}>\n".format(current_ind,self.tag))


class OneLineTag(Element):
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        for con in self.content:
            file_out.write(con)
        file_out.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind)[:-1])
        file_out.write(" />\n")


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
        self.tag = "h%i"%(level)

# H(2, "The text of the header")


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


