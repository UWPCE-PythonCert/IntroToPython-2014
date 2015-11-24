class Element:
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def format_start_tag(self, self_closing=False):
        start_tag = '<{}'.format(self.tag)
        for k, v in self.attributes.items():
            start_tag += ' {}="{}"'.format(k, v)
        start_tag += ' />' if self_closing else '>'
        return start_tag

    def render(self, f, ind='    '):
        f.write(ind)
        start_tag = self.format_start_tag()
        f.write(start_tag)
        ind += '    '
        for el in self.content:
            f.write('\n')
            # EAFP
            try:
                el.render(f, ind)
            except AttributeError:
                f.write(ind)
                f.write(str(el))
        ind = ind[:-4]
        f.write('\n')
        f.write(ind)
        end_tag = '</{}>'.format(self.tag)
        f.write(end_tag)


class OneLineTag(Element):
    def render(self, f, ind='    '):
        f.write(ind)
        start_tag = self.format_start_tag()
        f.write(start_tag)
        for el in self.content:
            # EAFP
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        end_tag = '</{}>'.format(self.tag)
        f.write(end_tag)


class SelfClosingTag(Element):
    def render(self, f, ind='    '):
        f.write(ind)
        self_closing_tag = self.format_start_tag(self_closing=True)
        f.write(self_closing_tag)


class Meta(SelfClosingTag):
    tag = 'meta'


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        Element.__init__(self, content, href=link)


class H(OneLineTag):
    tag = 'h'

    def __init__(self, header_level, content=None, **kwargs):
        self.tag = self.tag + str(header_level)
        Element.__init__(self, content, **kwargs)


class Html(Element):

    def render(self, f, ind='    '):
        f.write('<!DOCTYPE html>\n')
        Element.render(self, f, ind='    ')


class Head(Element):
    tag = 'head'


class Title(OneLineTag):
    tag = 'title'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'
