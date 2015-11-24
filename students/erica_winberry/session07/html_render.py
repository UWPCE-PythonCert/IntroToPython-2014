class Element:

    indent = 0
    tag = ""

    def __init__(self, content=None, **kwargs):
        self.content = []
        if content is not None:
            self.content.append(content)
        self.kwargs = kwargs

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind=" "):
        start_tag = "\n<{}".format(self.tag)
        if self.kwargs:
            f.write(start_tag)
            for k, v in self.kwargs.items():
                attribute = '{}="{}"'.format(k, v)
                f.write(" " + attribute)
            f.write(">")
        else:
            f.write(start_tag + ">")
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "\n</{}>".format(self.tag)
        f.write(end_tag)


class Body(Element):

    indent = 2
    tag = "body"

    # def __init__(self, content=None):
    #     self.content = []
    #     if content is not None:
    #         self.content.append(content)


class Head(Element):

    indent = 2
    tag = "head"


class Html(Element):

    indent = 0
    tag = "html"


class OneLineTag(Element):

    def render(self, f, ind=" "):
        start_tag = "\n<{}>".format(self.tag)
        f.write(start_tag)
        for element in self.content:
            try:
                element.render(f)
            except AttributeError:
                f.write(str(element))
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag)


class Paragraph(Element):

    indent = 2
    tag = "p"


class Title(OneLineTag):

    tag = "title"
