
# step 1
class Element ():
    tag = 'html'
    end_tag = None
    add_param = None
    def __init__(self, content = None, **kwargs):
        self.content = []
        self.end_tag = None
        self.add_param = kwargs
        if content is not None:
            self.content.append(content)

    def append(self, content):
        self.content.append(content)

    def render(self, f, ind = ""):
        if self.end_tag is None:
            self.end_tag = self.tag

        start_tag =ind + '<{}'.format(self.tag)
        for key, value in self.add_param.items():
            start_tag += ' {}="{}"'.format(key,value)
        start_tag += ">"
    # print('in render', self.tag, self.end_tag, self.add_param)
        f.write(start_tag)
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        end_tag = "</{}>".format(self.end_tag) + "\n"
        f.write(end_tag)

#1st subclass
class Html (Element):
    tag ='html'

class Body (Element):
    tag ='body'

class P (Element):
    tag ='p'

class Head (Element):
    tag ='head'

# create a oneline tag subclass of Element
#step 3
class OneLineTag (Element):
    def render(self, f, ind = " "):
        start_tag = "<{}>".format(self.tag)
        f.write(start_tag)
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))
        end_tag = "</{}>".format(self.tag)
        f.write(end_tag)

class Title (OneLineTag):
    tag ='title'

# step 5
class SelfClosingTag (Element):
    def render(self, f, ind = " "):
        if self.add_param is None:
            selfclose_tag ="<{} />".format(self.tag) + "\n"
        else:
            selfclose_tag = '<{} "{}"/>'.format(self.tag, self.add_param) + "\n"
        #print ("charset = ", charset)
        f.write(selfclose_tag)
        for el in self.content:
            try:
                el.render(f)
            except AttributeError:
                f.write(str(el))

class Hr (SelfClosingTag):
    tag ='hr'

# subclass for anchor
# step 6
class A (Element):
    tag = 'a'
    def __init__(self, link = None, content = None, *args, **kwargs):
        #self.add_param = None
        self.content = []
        #self.end_tag = "a"
        if content is not None:
            self.content.append(content, *args, **kwargs)

# Create Ul class for an unordered list (really simple subclass of Element)
# step 7
class Ul (Element):
    tag = 'ul'

class Li (Element):
    tag = 'li'

class H (Element):
    def __init__(self, level = None, content = None, *args, **kwargs):
            self.content = []
            #self.add_param = None
            if level is not None:
                self.tag =  'h' + str(level)
                #print ("head level" + self.tag)
                #print("content", content)
                self.content.append(content, *args, **kwargs)
# step 8
class Meta (SelfClosingTag):
    tag = 'meta'
















