#coding: utf-8
"""
html_render.py

Questions:
"""

import pdb

# starting render classes
class Element(object):
    indent = ''  # indent level for tag
    tag = u"html"

    def __init__(self, content=None, **attrsdict):  
        # update with content=None, **attributes/kwargs empty dictionary initialized, but not populated assuming dict isn't passed

        self.tag_dict = {'indent': self.indent, 'tag': self.tag,
                    'ind': ""}  # , 'ind': ind

        self.attrsdict = attrsdict

        # print attrsdict

        if content is None:
            self.content = []
        else:
            self.content = [content] # create a list to render ea. element

    def append(self, new_content):
        if new_content:
            self.content.append(new_content)

    # render method, extended a couple times
    def render(self, file_out, ind=""):

        attrstring = []
        for k, v in self.attrsdict.items():
            tempstring = u'{}= "{}" '.format(k, v)
            print tempstring
            attrstring.append(tempstring)

        # print attrstring

        tempattr = u''.join(attrstring)

        # consider moving entire attrstring work into new method

        file_out.write(u'{ind}{indent}<{tag} '.format(**self.tag_dict))
        file_out.write(tempattr)
        file_out.write(u'>\n')

        # expand here to create handling for either string or object
        for obj in self.content:
            # string
            try:
                file_out.write(self.indent + ind*2 + obj + u'\n')

            # object rendering, which does not work
            except (TypeError):
                obj.render(file_out, ind=(self.indent))
                # pdb.set_trace()

        file_out.write(u'{ind}{indent}</{tag}>\n'.format(**self.tag_dict))

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
        # print self.tag_dict

        file_out.write(u'{indent}{ind}<{tag}>'.format(**self.tag_dict))
        for obj in self.content:
            try:
                file_out.write(obj)
            except (TypeError):
                obj.render(file_out, ind="")

        file_out.write(u'</{tag}>\n'.format(**self.tag_dict))

class Title(OneLineTag):
    tag = u'title'
    indent = u'        '

class SelfClosingTag(Element):

    def render(self, file_out, ind="        "):
        self.tag_dict['ind'] = ind

        # tag_dict = {'indent': self.indent, 'tag': self.tag,
        #             'style': self.style, 'ind': ind}

        file_out.write(u'{indent}{ind}<{tag} />\n'.format(**self.tag_dict))

# step 5 elements, self closing horizontal rule and break tags

class Hr(SelfClosingTag):
    tag = u'hr'

class Br(SelfClosingTag):
    tag = u'br'

# step 6, add hyperlink tag as subclass of Element

class A(Element):
    tag = u'a'

    """A(self, link, content)
        where link is the link, and content is what you see
        A(u"http://google.com", u"link to google")

        subclass from Element, and only override the __init__ —
        Calling the Element __init__ from the A __init__
    """

    def __init__(self, link, content=None):
        # pass in link url, text to hyperlink
        # create a dictionary k, v pair from link that is passed in
        # to lower element init
        print link
        Element.__init__(self, content, **{'href': link})


"""
MOAR FOR LATER
# file_out.write(u'{indent}{content}\n'
#     .format(indent=self.indent+ind, content=obj))
## above doesn't work: .format() method will render ANY var passed!

"""