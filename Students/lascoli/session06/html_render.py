#!/usr/bin/env python

"""
Python class example.

"""


# The start of it all:
# Fill it all in here.
class Element(object):
    tag = 'html'
    indent = '    '

    def __init__(self, content=None):
        if content is not None:
            self.content = [str(content)]
        else:
            self.content = []

    def append(self, new_content):
        """ add some new content to the element"""
        self.content.append(new_content)

    def render(self, file_out, ind=""):
        """render the content to the given file like object"""

        file_out.write( ind+"<"+self.tag+">\n"+ind+self.indent )
        file_out.write( ("\n"+ind+self.indent).join(self.content) )
        file_out.write( "\n"+ind+"</"+self.tag+">" )


