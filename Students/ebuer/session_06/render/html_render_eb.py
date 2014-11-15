#coding: utf-8
"""
html_render.py

Questions:
line: 41
line: 65
"""

import pdb

# starting render classes
class Element(object):
    indent = ''  # indent level for tag
    tag = u"html"

    def __init__(self, content=None,
                 style=None):  # update with content=None, **attributes/kwargs
        self.style = style
        # self.attributes = attributes

        if content is None:
            self.content = []
        else:
            self.content = [content] # create a list to render ea. element

    def append(self, new_content):
        if new_content:
            self.content.append(new_content)

    # render method, extended a couple times
    def render(self, file_out, ind=""):
        # pdb.set_trace()
        tag_dict = {'indent': self.indent, 'tag': self.tag,
                    'style': self.style, 'ind': ind}

        if self.style is not None:
            file_out.write(u'{ind}{indent}<{tag} style="{style}">\n'.format(**tag_dict))
        else:
            file_out.write(u'{ind}{indent}<{tag}>\n'.format(**tag_dict))

        # expand here to create handling for either string or object
        for obj in self.content:
            # string
            try:

                # file_out.write(u'{indent}{content}\n'
                #     .format(indent=self.indent+ind, content=obj))
                ## above doesn't work: .format() method will render ANY var passed!

                file_out.write(self.indent + ind*2 + obj + u'\n')
                # # pdb.set_trace()

            # object rendering, which does not work
            except (TypeError):
                obj.render(file_out, ind=(self.indent))
                # pdb.set_trace()

        file_out.write(u'{ind}{indent}</{tag}>\n'.format(**tag_dict))

# Create subclasses for html, body and paragraph tags
class Html(Element):
    tag = u"HTML"

    def render(self, file_out, ind=""):
        """
        Extend the render method for this subclass to write DOCTYPE @ top
        """
        file_out.write(u'<!Doctype {tag}>\n'.format(tag=self.tag))
        Element.render(self, file_out, ind="")

class Body(Element):
    tag = u"body"
    indent = u'    '

class P(Element):
    tag = u"p"
    indent = u'        '

class Head(Element):
    tag = u'head'
    indent = u'    '

class OneLineTag(Element):

    # override render to put everything on 1 line where things are simple
    def render(self, file_out, ind=""):
        tag_dict = {'indent': self.indent, 'tag': self.tag,
                    'style': self.style, 'ind': ind}

        file_out.write(u'{indent}{ind}<{tag}>'.format(**tag_dict))
        for obj in self.content:
            try:
                file_out.write(obj)
            except (TypeError):
                obj.render(file_out, ind="")

        file_out.write(u'</{tag}>\n'.format(**tag_dict))

class Title(OneLineTag):
    tag = u'title'
    indent = u'        '

class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        tag_dict = {'indent': self.indent, 'tag': self.tag,
                    'style': self.style, 'ind': ind}

        file_out.write(u'{indent}{ind}<{tag} />\n'.format(**tag_dict))

class Hr(SelfClosingTag):
    tag = u'hr'

class Br(SelfClosingTag):
    tag = u'br'


