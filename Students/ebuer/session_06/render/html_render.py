#coding: utf-8
"""
html_render.py

"""

# starting render classes
class Element(object):
    indent = ''  # indent level for tag
    tag = u"html"

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content=""):
        if self.content is None:
            self.content = [new_content] # create a list to render ea. element
        else:
            self.content.append(new_content)

    # renders the tag and the strings in the content
    """Extend the Element.render() method so that it can render other elements inside the tag in addition to strings. Simple recursion should do it. i.e. it can call the render() method of the elements it contains. You’ll need to be smart about setting the ind optional parameter so that the nested elements get indented correctly
            """

    def render(self, file_out, ind=""):

        self.file_out = file_out.write(u'{indent}<{tag}>\n'
            .format(indent=self.indent, tag=self.tag))

        # for c in self.content:  # render each line from list
        self.file_out = file_out.write(u'{indent}{content}\n'
            .format(indent=self.indent, content=self.render(self.content)))

        self.file_out = file_out.write(u'{indent}</{tag}>\n'
            .format(indent=self.indent, tag=self.tag))

# Create subclasses for body and paragraph tags
class Body(Element):
    tag = u'body'

class Html(Element):
    tag = u'!Doctype: HTML'

class P(Element):
    tag = u'p'
