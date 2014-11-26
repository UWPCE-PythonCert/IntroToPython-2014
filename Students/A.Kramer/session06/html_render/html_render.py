'''
Created on Nov 5, 2014

@author: Aleksey Kramer
'''

# The start of it all:
# Fill it all in here.
class Element(object):
    def __init__(self, content=None, id=None, style=None):
        self.ind = "    "  
        self.tag = ""
        self.starttag = self.tag + "\n"
        self.endtag = self.tag[:1] + "/" + self.tag[1:] + "\n"
        self.lst = []  
        if content is not None:
            self.lst.append(content)
            
    def append(self, new_content):
        self.lst.append(new_content)

    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        for line in self.lst:
            try:
                line.render(file_out)
            except AttributeError as e:
                file_out.write(self.ind + ind + line + "\n")
        file_out.write(self.endtag)

class Html(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.tag = "<html>"
        self.starttag = self.tag + "\n"
        self.endtag = self.tag[:1] + "/" + self.tag[1:] + "\n"

class Body(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.tag = "<body>"
        self.starttag = self.tag + "\n"
        self.endtag = self.tag[:1] + "/" + self.tag[1:] + "\n"
        
class P(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content, id, style)
        self.tag = "<P>"
        self.id = ""
        self.style = ""
        if id is not None:
            self.id = " id=\"" + id + "\"" 
        if style is not None:
            self.style = " style=\"" + style + "\""
        self.starttag = "<p" + self.id + self.style + ">\n"
        self.endtag = "</p>\n"

class Head(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.tag = "<Head>"
        self.starttag = self.tag + "\n"
        self.endtag = self.tag[:1] + "/" + self.tag[1:] + "\n"

class OneLineTag(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.content = content
    
    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        file_out.write(self.ind + ind + self.content + "\n")
        file_out.write(self.endtag)
        
    def append(self, new_content):
        raise NotImplementedError
        
class Title(OneLineTag):
    def __init__(self, content=None, id=None, style=None):
        OneLineTag.__init__(self, content)
        self.tag = "<Title>"
        self.starttag = self.tag + "\n"
        self.endtag = self.tag[:1] + "/" + self.tag[1:] + "\n"

class SelfClosingTag(Element):
    def __init__(self, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.content = content

    def render(self, file_out, ind=""):
        file_out.write(self.tag)

    def append(self, new_content):
        raise NotImplementedError

class Hr(SelfClosingTag):
    def __init__(self, content=None, id=None, style=None):
        SelfClosingTag.__init__(self, content)
        self.tag = "<hr />\n"

class Br(SelfClosingTag):
    def __init__(self, content=None, id=None, style=None):
        SelfClosingTag.__init__(self, content)
        self.tag = "<br />\n"

class A(Element):
    def __init__(self, link=None, content=None, id=None, style=None):
        Element.__init__(self, content)
        self.starttag = "<a>"
        self.content = ""
        if (link is not None) and (content is not None):
            self.starttag = "<a href=\"" + link + "\">"
            self.content = content
        self.endtag = "</a>"

    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        file_out.write(self.content)
        file_out.write(self.endtag)
        
    def append(self, new_content):
        raise NotImplementedError     

class Ul(Element):
    def __init__(self, content=None, id=None, style=None):
        self.starttag = ""
        self.id = ""
        self.style = ""
        self.lst = []
        if (id is not None) and (style is not None):
            self.starttag = "<ul id=\"" + id + "\" style=\"" + style + "\">\n"
        self.endtag = "</ul>\n"

    def append(self, new_content):
        self.lst.append(new_content)
            
    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        for line in self.lst:
            try:
                line.render(file_out)
            except AttributeError as e:
                file_out.write(self.ind + ind + line + "\n")
        file_out.write(self.endtag)
    
class H(Element):
    def __init__(self, hlevel=None, content=None):
        self.level = str(hlevel)
        self.content = content
        self.starttag = "<h" + self.level + ">"
        self.endtag = "</h" + self.level + ">\n"
    
    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        file_out.write(self.content)
        file_out.write(self.endtag)
        
    def append(self, new_content):
        raise NotImplementedError     

class Li(Element):
    def __init__(self, content=None, style=None):
        self.lst = []
        self.style = style
        self.content = ""
        self.starttag = "<li>"
        if style is not None:
            self.starttag = "<li style=\"" + self.style + "\">"
        if content is not None:
            self.content = content
        self.endtag = "</li>\n"

    def append(self, new_content):
        self.lst.append(new_content)
            
    def render(self, file_out, ind=""):
        file_out.write(self.starttag)
        file_out.write(self.content)
        file_out.write(self.endtag) 
    
if __name__ == "__main__":
    l = Element()

    