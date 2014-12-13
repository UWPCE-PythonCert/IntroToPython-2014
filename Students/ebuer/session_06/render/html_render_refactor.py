#coding: UTF-8
"""html_render_refactor.py"""


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

        for s in self.content:
            file_out.write(ind + s + u'\n')

        file_out.write(u'</' + self.tag + u'>\n')

