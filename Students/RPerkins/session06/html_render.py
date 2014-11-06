__author__ = 'Robert W. Perkins'


#!/usr/bin/env python

"""
Python class example.
"""


# The start of it all:
# Fill it all in here.
class Element(object):

    tag = '<html>'
    indent = '    '

    def __init__(self, content=None):

        self.content = content

    def append(self, new_content):

        if self.content is None:
            self.content = new_content
        else:
            self.content = '{ex_content}{n_content}'.format(ex_content=self.content, n_content=new_content)

    def render(self, file_out, ind=""):
        """Write content and tags to the file_out StringIO object"""
        file_out.write('{tag_indent}{start_tag}\n{element_indent}{content}\n{tag_indent}{end_tag}'.format
                       (tag_indent=self.indent, start_tag=self.tag, element_indent=ind+self.indent, content=self.content,
                        end_tag=self.tag))
