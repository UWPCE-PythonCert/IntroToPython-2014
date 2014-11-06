"""
html_render.py
"""

# starting render classes


class Element(object):
    ind = 4  # tag for number of spaces in ind
    tag = "<html>"

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content=""):
        if self.content is None:
            self.content = new_content
        else:
            self.content = " ".join([self.content, new_content])

    # renders the tag and the strings in the content
    def render(self, file_out, ind=""):
        self.file_out = file_out
        # fid = open(file_out, 'w')

