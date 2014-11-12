#!/usr/bin/python

class element(object):
    tag = 'html'

    indent = '    '

    def __init__(self, content=None, **attributes):
        
        self.content = []

        if content is not None:
            self.content.append(content)
            self.attributes = attributes
    def append(self, content):
    
        self.content.append(content)

    def render_tag(self, current_ind):

        attrs = "".join([' {}={}'.format(key,val) for key, val in self.attributes.items()])

        tag_str = "{}<{}{}>").format(current_ind,self.tag, attrs)

        return tag_str

    def render(self, file_out, current_ind=""):

        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')

        for c in self.content:
            try:
                file_out.write(current_ind + self.indent + con + '\n')
            except TypeError:
                con.render(file_out, current_ind + self.indent)

        file_out.write("{}<{}> + \n".format(current_ind, self.tag))

        
class Html(element):

    tag = 'html'

class Body(element):

    tag = 'body'

class P(element):
    
    tag = 'p'

class Head(element):
    
    tag = 'head'
    
class OneLineTag(element):
    
    def render(self, file_out, current_ind=""):

        file_out.write(self.render_tag(current_ind))
        
        for c in self.content:
                file_out.write(con)

        file_out.write("</{}>\n").format(self.tag))

class SelfClosingTag(OneLineTag):
    
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        file_out.write(" />\n")


class Hr(SelfClosingTag):



class title(OneLineTag):

    tag = 'title'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content):
        OneLineTag.___init__(self, content=None, **attributes)
        self.attributes["href"] = link
        
class H(OneLineTag):

    tag = 'h'
    
    def __init__(self, level, content=None, **attributes):
        self.tag = 'h{}'.format(level)

class Ul(element):
    tag = 'ul'

class li(element):
    tag = 'li'
