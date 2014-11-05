"""
html_render.py
"""

# starting render classes


class Element(object):

    def __init__(self, html, indtag, content=None):
        self.html = html
        self.ind = indtag
        self.content = content

    def append(self, new_content):
        self.content = " ".join(self.content, new_content)

    def render(self, file_out, ind=""):
        pass
