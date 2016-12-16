#!/usr/bin/env  python

"""
html render code -- this shows how to wrap plain text in a simple class
for rendering.
"""


class TextWrapper:
    """
    A simple wrapper that creates a class with a render method
    for simple text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


# here is how you might use it:
class Element:

    tag = 'html'  # shouldn't really be usable without properly subclassing
    indent = '    '

    def __init__(self, content=None, **attributes):

        self.content = []
        self.attributes = attributes

        if content is not None:
            # call this class's append -- so any magic done in there is used.
            self.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))
