#!/usr/bin/python

class Element(object):

    #tag = 'html'
    indent = '    '
    def __init__(self, content=None, **attributes):

        self.content = []
        
        self.attributes = attributes

        if content is not None:

            self.content.append(content)
    def append(self, content): 
    
        self.content.append(content)

    def render_tag(self, current_ind):

        attrs = "".join([' {}={}'.format(key,val) for key, val in self.attributes.items()])

        tag_str = "{}<{}{}>".format(current_ind,self.tag,attrs)

        return tag_str

    def render(self, file_out, current_ind=""):

        file_out.write(self.render_tag(current_ind))
        file_out.write('\n')

        for con in self.content:
            try:
                file_out.write(current_ind + self.indent + con + '\n')

            except TypeError:
                con.render(file_out, current_ind + self.indent)

        file_out.write("{}</{}> \n".format(current_ind, self.tag))

class Html(Element):
    tag = 'html'
    def render(self, file_out,current_ind=""):

        file_out.write("<!DOCTYPE html>\n")
        Element.render(self,file_out, current_ind=current_ind)

class Body(Element):
    tag = 'body'
        
class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):

    def render(self, file_out, current_ind=""):

        file_out.write(self.render_tag(current_ind))

        for con in self.content:
            file_out.write(con)

        file_out.write("</{}> \n".format(self.tag))

class Title(OneLineTag):

    tag = 'title'

class SelfClosingTag(Element):
    
    def render_tag(self, current_ind):

        attrs = "".join([' {}={}'.format(key,val) for key, val in self.attributes.items()])

        tag_str = "{}<{}{} />".format(current_ind,self.tag,attrs)

        return tag_str

    def render(self, file_out, current_ind=""):

        file_out.write(self.render_tag(current_ind))

        for con in self.content:
            try:
                file_out.write(current_ind + self.indent + con)

            except TypeError:
                con.render(file_out, current_ind + self.indent)

        #file_out.write("{}</{}> \n".format(current_ind, self.tag))
        file_out.write("\n")


class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **attributes):

        OneLineTag.__init__(self, content, **attributes)
        self.attributes["href"] = link

class Ul(Element):

    tag = 'ul'

class Li(Element):

    tag = 'li'

class H(OneLineTag):

    tag = 'h'

    def __init__(self, level, content=None, **attributes):

        OneLineTag.__init__(self, content, **attributes)
        self.tag = 'h{}'.format(level)

class Meta(SelfClosingTag):

    tag = 'meta'

     
