#coding: utf-8
"""
html_render.py

Questions:
l. 41
l. 65


"""

import pdb

# starting render classes
class Element(object):
    indent = ''  # indent level for tag
    tag = u"html"

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content] # create a list to render ea. element

    def append(self, new_content):
        if new_content:
            self.content.append(new_content)

    # renders the tag and the strings in the content
    """Extend the Element.render() method so that it can render other elements inside the tag in addition to strings. Simple recursion should do it. Call the render() method of the elements passed. You’ll need to be smart about setting the ind optional parameter so that the nested elements get indented correctly
            """

    def render(self, file_out, ind=""):
        tag_dict = {'indent': self.indent, 'tag': self.tag}

        file_out.write(u'{indent}<{tag}>\n'.format(**tag_dict))

        # expand here to create handling for either string or object
        for obj in self.content:
            # string
            try:
                # file_out.write(u'{indent}{content}\n'
                #     .format(indent=self.indent+ind, content=obj))
                ## above doesn't work: .format() method will render ANY var passed!

                file_out.write(self.indent + u'    ' + obj + u'\n')
                # pdb.set_trace()

            # object rendering, which does not work
            except (TypeError):
                obj.render(file_out, ind=(self.indent))
                # pdb.set_trace()

        file_out.write(u'{indent}</{tag}>\n'.format(**tag_dict))

# Create subclasses for html, body and paragraph tags
class Html(Element):
    tag = u"HTML"

    def render(self, file_out, ind=""):
        """
        Extend the render method for this subclass to write DOCTYPE @ top
        """
        file_out.write(u'<!Doctype {tag}>\n'.format(tag=self.tag))
        Element.render(self, file_out, ind="")  
        # Element.render is called here to create stack

class Body(Element):
    tag = u"body"
    indent = u'    '

class P(Element):
    tag = u"p"
    indent = u'        '
