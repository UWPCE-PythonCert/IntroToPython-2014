class Element:
    tag = 'html'
    indent = 0

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind='    '):
        f.write(ind * self.indent)
        start_tag = '<{}'.format(self.tag)
        # is there a better way to do this?
        for k, v in self.attributes.items():
            start_tag += ' {}={}'.format(k, v)
        start_tag += '>'
        f.write(start_tag)
        for el in self.content:
            f.write('\n')
            # EAFP
            try:
                el.render(f)
            except AttributeError:
                f.write((self.indent * ind) + ind)
                f.write(str(el))
        f.write('\n')
        f.write(ind * self.indent)
        end_tag = '</{}>'.format(self.tag)
        f.write(end_tag)


class OneLineTag(Element):
    def render(self, f, ind='    '):
        f.write(ind * self.indent)
        start_tag = '<{}'.format(self.tag)
        for k, v in self.attributes.items():
            start_tag += ' {}={}'.format(k, v)
        start_tag += '>'
        f.write(start_tag)
        for el in self.content:
            # EAFP
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        end_tag = '</{}>'.format(self.tag)
        f.write(end_tag)


class Html(Element):
    indent = 1


class Head(Element):
    tag = 'head'
    indent = 2


class Title(OneLineTag):
    tag = 'title'
    indent = 3


class Body(Element):
    tag = 'body'
    indent = 2


class P(Element):
    tag = 'p'
    indent = 3
