from io import StringIO

#create a class for rendering an HTML element
class Element():
    tag = 'html'    
    def __init__(self, content = None):
                
        self.content = []
        if content is not None:
            self.content.append(content)
    def append(self, content):
        self.content.append(content)
    
    def render(self, f, ind="    "):
        start_tag = "<{}>".format(self.tag)
        f.write(start_tag)
        
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                
                f.write(str(el)) #f.write(render(f))
        
        end_tag = "</{}>".format(self.tag)        
        f.write(end_tag)        

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'
