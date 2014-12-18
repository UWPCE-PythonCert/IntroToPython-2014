class Element(object):
    tag = ''
    indent = '    '

    def __init__(self, content=None, **attributes):

        self.content = []
        self.attributes = attributes

        if content is not None:
            self.content.append(content)

    def append(self, content):
        """
        add some new content to the element
        might want to apply html entities to this user input
        """
        self.content.append(content)


    def render_tag(self,current_indent):
        attrs = "".join([' {}="{}"'.format(key,val) for key, val in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_indent, self.tag, attrs)
        return tag_str

    def render(self, file_out, current_indent=""):
        """render the content to the given file like object"""
        file_out.write(self.render_tag(current_indent))
        file_out.write('\n')
        for con in self.content:
            try:
                file_out.write(self.indent + current_indent + con+"\n")
            except TypeError:
                con.render(file_out, current_indent + self.indent)
        file_out.write("{}</{}>\n".format(current_indent,self.tag))


class OneLineTag(Element):
    def render(self, file_out, current_indent=""):
        file_out.write(self.render_tag(current_indent))
        for con in self.content:
            try:
                file_out.write(con+"")
            except TypeError:
                con.render(file_out, current_indent + self.indent)
        file_out.write("</{}>".format(self.tag))

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(OneLineTag):
    def render(self, file_out, current_indent=""):
        file_out.write("{}<{}>".format(current_indent, self.tag))


class Hr(SelfClosingTag):
    tag = 'hr'


class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content, **attributes):
        OneLineTag.__init__(self, content=None, **attributes)
        self.attributes["href"] = link

class H(OneLineTag):
    tag = 'h'
    def __init__(self, level, content=None, **attributes):
        OneLineTag.__init__(self, content, **attributes)
        self.tag = "h%i"%(level)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class Html(Element):
    tag = 'html'
    def render(self, file_out, current_indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, current_indent=self.indent)


class Body(Element):
    tag = 'body'



class P(Element):
    tag = 'p'


'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>PythonClass = Revision 1087:</title>
    </head>
    <body>
        <h2>PythonClass - Class 6 example</h2>
        <p style="text-align: center; font-style: oblique;">
            Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text
        </p>
        <hr />
        <ul style="line-height:200%" id="TheList">
            <li>
                The first item in a list
            </li>
            <li style="color: red">
                This is the second item
            </li>
            <li>
                And this is a
                <a href="http://google.com">link</a>
                to google
            </li>
        </ul>
    </body>
</html>
'''