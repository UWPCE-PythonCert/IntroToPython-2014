#!/usr/bin/python

class Element(object):

    #tag = 'html'
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
