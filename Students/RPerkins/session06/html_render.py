__author__ = 'Robert W. Perkins'


#!/usr/bin/env python

"""
Python class example.
"""


class Element(object):

    tag = '<html>'
    endtag = '</html>'
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

        #file_out.write('{tag_indent}{start_tag}\n'.format
                      #(tag_indent=self.indent, start_tag=self.tag,))

        for item in self.content:
            if type(item) is str:
                file_out.write('{tag_indent}{start_tag}\n{element_indent}{content}\n{tag_indent}{end_tag}\n'.format
                              (tag_indent=self.indent, start_tag=self.tag, element_indent=ind+self.indent,
                               content=item, end_tag=self.endtag))
            else:
                file_out.write('{tag_indent}{start_tag}\n'.format(tag_indent=self.indent, start_tag=self.tag,))
                item.render(file_out, "    ")
                file_out.write('{tag_indent}{end_tag}\n'.format(tag_indent=self.indent, end_tag=self.endtag))

        #file_out.write('{tag_indent}{end_tag}\n'.format(tag_indent=self.indent, end_tag=self.endtag))


class Html(Element):

    tag = '<html>'
    endtag = '</html>'


class P(Element):

    tag = '<p>'
    endtag = '</p>'
    indent = '            '


class Body(Element):

    tag = '<body>'
    endtag = '</body>'
    indent = '        '