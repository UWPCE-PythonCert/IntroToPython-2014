__author__ = 'Ari'

# STEP 1:
#   -

# Step 3:
# - create a head element


# Step 4:
# - create a class to accept a set of attributes
# remember "**kwargs" --

# Step 5:
# - create a SelfClosingTag



class Element(object):
    # 4 spaces = indent,
    # these are called class attributes
    indent = '    '

    ## chris used **attributes instead of **kwargs
    def __init__(self, content=None, **kwargs):
        # we have a dictionary of keys
        self.attributes = kwargs
        self.content = []
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render_tag(self, current_ind):
    # because there is some code duplication in OneLineTag and def render
    # we wrote this to deal with the tag formatting
        attrs = "".join([' {}="{}"'.format(k, v) for k, v in self.attributes.items()])
        tag_str = "{}<{}{}>".format(current_ind, self.tag,attrs)
        return tag_str


    def render(self, file_out, current_ind=""):
        """
        render, just renders itself
        """
        # from kwargs...need to format a dictionary of items, replaced with render_tag
        #attrs = "".join([' {}="{}"'.format(k, v) for k, v in self.kwargs.items()])

        # file_out -- File name in which to output render

        # a file_out has a write method
        # carriage return is necessary
        # so you could have file_out.write("<html>\n")...
        # but once you start using the class Html..
        # this isn't going to work so well (so '.format' to the rescue)

        file_out.write(self.render_tag(current_ind))
        # adding the carriage return since we took it out of render_tag
        file_out.write('\n')
        # append content in a list as entered
        # print self.content
        for con in self.content:
            #print "trying to render",con
            try:
                file_out.write(current_ind+ self.indent + con+"\n")
            except TypeError:
                # in order to have indent = ""...we are modifying the
                # embedded element to add an indent
                # by
                con.render(file_out, current_ind+self.indent)
        file_out.write("{}</{}>\n".format(current_ind,self.tag))



class OneLineTag(Element):
    def render(self, file_out, current_ind=""):
        file_out.write(self.render_tag(current_ind))
        for con in self.content:
            file_out.write(con)
        file_out.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = 'hr'

class SelfClosingTag(Element):
    def render(self, file_out, current_ind=""):
        # a little array slicing notation
        file_out.write(self.render_tag(current_ind)[:-1])
        file_out.write(" />\n")

class Hr(SelfClosingTag):
    tag = 'hr'


class A(OneLineTag):
    tag ='a'
    # it is content, and not self.content because you
    # haven't assigned it
    def __init__(self, link, content, **kwargs):
        OneLineTag.__init__(self, content=None, **kwargs)
        self.attributes["href"] = link

class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        OneLineTag.__init__(self, content, **kwargs)
        self.tag = "h%i"%(level)

class U1(Element):
    tag = "u1"

class Li(Element):
    tag='li'

class Html(Element):
    tag = 'html'
    def render(self, file_out, current_ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, current_ind=current_ind)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'
