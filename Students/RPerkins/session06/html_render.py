__author__ = 'Robert W. Perkins'


#!/usr/bin/env python

"""
Python class example.
"""


class Element(object):

    tag = '<html>'
    endtag = tag[:1] + '/' + tag[1:]
    indent = '    '

    def __init__(self, content=None):

        self.content = [content]

    def append(self, new_content):
        """Check for existing content and add new_content"""

        if self.content[0] is None:
            self.content = [new_content]
        else:
            self.content.append(new_content)

    def render(self, file_out, ind=""):
        """Write content and tags to the file_out StringIO object"""

        file_out.write('{tag_indent}{start_tag}\n'.format
                            (tag_indent=self.indent, start_tag=self.tag,))

        file_out.writelines('{element_indent}{content}\n'.format
                            (element_indent=ind+self.indent, content=item) for item in self.content)

        file_out.write('{tag_indent}{end_tag}'.format
                            (tag_indent=self.indent, end_tag=self.endtag))
