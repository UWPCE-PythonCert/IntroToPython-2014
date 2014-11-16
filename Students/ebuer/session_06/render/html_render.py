"""
html_render.py

Questions: how do I inspect class and object attributes to see if the correct value has been ascribed?

"""

# starting render classes


class Element(object):
    indent = 0  # indent level for tag
    tag = [u"<html>", u"</html>"]

    def __init__(self, content=None):
        self.content = content

    def append(self, new_content=""):
        if self.content is None:
            self.content = [new_content] # create a list to render ea. element
        else:
            self.content.append(new_content)

    # renders the tag and the strings in the content
    def render(self, file_out, ind=""):
        self.ind = ind
        self.indent = 1  # subclass to override class indent (?)

        # content will need to be read in one line at a time and rendered

        self.file_out = file_out.write(u'{indent}{tag}\n'
            .format(indent=Element.indent*self.ind, tag=Element.tag[0]))

        for line in self.content:
            self.file_out = file_out.write(u'{indent}{content}\n'
                .format(indent=self.indent*self.ind, content=line))

        self.file_out = file_out.write(u'{indent}{tag}\n'
            .format(indent=Element.indent*self.ind, tag=Element.tag[1]))
