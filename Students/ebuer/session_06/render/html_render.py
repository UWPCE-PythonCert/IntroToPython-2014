"""
html_render.py
"""

# starting render classes


class Element(object):
    indent = 0  # tag for number of spaces in ind
    tag = "<html>"

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content=""):
        if self.content is None:
            self.content = new_content
        else:
            # think here about adding unicode conversion str.unicode(**kwargs)
            # need to preserve line breaks for render, make this a list
            self.content = " ".join([self.content, new_content])

    # renders the tag and the strings in the content
    def render(self, file_out, ind=""):
        self.ind = ind
        if self.ind is "":
            pass
        else:
            self.ind = ind

        # content will need to be read in one line at a time and rendered
        temp_content = u'{content}'.format(content=self.content)

        self.file_out = file_out.write(temp_content)



