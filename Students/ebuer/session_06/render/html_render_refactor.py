#coding: UTF-8
"""html_render_refactor.py"""

import pdb

#Step 1: create Element

class Element(object):
    """docstring for Element"""
    tag = u'html'
    indent = u'    '

    def __init__(self, content=None):
        if not content:
            self.content = []
        else:
            self.content = [content]

    def append(self, s):
        """append method for element"""
        self.content.append(s)

    def render(self, file_out, ind=u''):
        file_out.write(u'<' + self.tag + u'>\n')

        try:
            for s in self.content:
                file_out.write(ind + s + u'\n')
        except TypeError:
            for s in self.content:
                # pdb.set_trace()
                s.render(file_out, ind)

        file_out.write(u'</' + self.tag + u'>\n')

# Step 2 create subclasses for body and p
class Html(Element):
    tag = 'Html'

class Body(Element):
    tag='body'

class P(Element):
    tag = 'p'

