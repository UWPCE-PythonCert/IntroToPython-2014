'''
html_render.py

Python Certification Course
Nov 8, 2014

Pretty print an html string

'''



class Element(object):
    '''
    Step One, create the element class.
    '''
    tag = 'html'
    indent = '   ' 
    attributes = ''
    
    def __init__ (self, content=None, **attributes):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        self.attributes = ' '.join([' {}="{}"'.format(key, val) for key,val in attributes.items()])  
        
    def append(self, added_content):
        '''
        Add content to existing content, if any.
        '''
        self.contents.append (added_content)
        
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''
        
        file_out.write (ind + '<'+self.tag+self.attributes+'>\n')
        for content in self.contents:
            
            if isinstance(content,  Element):
                content.render(file_out, ind + self.indent)
            else:
                file_out.write (ind+self.indent+content+'\n')
        file_out.write (ind+'</'+self.tag+'>\n')
        
        
'''        
Step 2, 3
'''


class bodyElement (Element):
    '''
    Sub class Element to replace tag 'html' with 'body'
    '''
    tag = 'body'
    
class pElement (Element):
    '''
    Sub class Element to replace tag 'html' with 'p' (paragraph)
    '''
    tag = 'p'
    
class headElement (Element):
    '''
    Sub class Element to replace tag 'html' with 'head' 
    '''
    tag = 'head'   
    
class  OneLineTag (Element):
    '''
    Re-defines render top print on one line.
    '''
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''

        for content in self.contents:
            file_out.write (ind+'<'+self.tag+'>'+content+'</'+self.tag+'>'+'\n')

class titleElement (OneLineTag):
    '''
    Sub class Element to replace tag 'html' with 'title' 
    '''
    tag = 'title'
    
#Step 5

class SelfClosingTag(Element):
    '''
    Uses Element's init and replaces render with self closer.
    '''
    def render (self, file_out, ind = ''):
        if len(self.contents) > 0:
            file_out.write (ind+'<'+self.tag+' '+self.contents[0]+'/>\n')
        else:
            file_out.write (ind+'<'+self.tag+' />\n')
            
        
class brElement (SelfClosingTag):
    tag = 'br'
    
class hrElement (SelfClosingTag):
    tag = 'hr'
    

#step 6
class anchorElement (OneLineTag):
    '''
    Add a link element. Overrides __init__
    '''
    tag = 'a'
    def __init__(self, url, link):
        self.contents = [' href="{}">{}'.format(url,link)]
    
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''
        file_out.write (ind+'<'+self.tag+self.contents[0]+'/>\n')
            
            
#step 7
class ulElement (Element):
    tag = 'ul'

class liElement (Element):
    tag = 'li'
    
class headerElement(OneLineTag):
    '''
    Create tag based on header level. Redefines __init__ and calls base class __init__.
    '''
    def __init__ (self, level, content=None):
        self.tag = 'h{}'.format(level)
        super(headerElement, self).__init__(content)

class htmlElement (Element):
    '''
    Override render to ass DOCTYPE and call base class render.
    '''
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''
        file_out.write (ind+'<!DOCTYPE html>\n')
        return super(htmlElement, self).render(file_out, ind)
        
class metaElement (SelfClosingTag):
    tag = 'meta'
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Test code


def testStepOne ():
    e = Element ('Some string')
    e.append ('some other string')
    file_out = open('step1.txt', 'w')
    e.render (file_out, '    ')
    file_out.close()  
    
def testStepTwo():
    e = Element ('Some string')
    b = bodyElement ('Some body text')
    p = pElement ('some paragraph text')
    e.append (b)
    e.append(p)
    file_out = open('step2.txt', 'w')
    e.render (file_out, '    ')
    file_out.close()   
    
def testStepThree():
    e = Element ('Some string')
    t = titleElement('Title Line Here')
    b = bodyElement ('Some body text')
    h = headElement('Header line')
    p = pElement ('some paragraph text')
    e.append (t)
    e.append (h)
    e.append (b)
    b.append(p)
    file_out = open('step3.txt', 'w')
    e.render (file_out, '    ')
    file_out.close()   

def testStepFour():
    e = Element ('Some string')
    t = titleElement('Title Line Here')
    b = bodyElement ('Some body text')
    h = headElement('Header line')
    p = pElement ('some paragraph text', style="text-align: center; font-style: oblique;", color="255")
    e.append (t)
    e.append (h)
    e.append (b)
    b.append(p)
    file_out = open('step4.txt', 'w')
    e.render (file_out, '    ')
    file_out.close()   
   
def testStepFive():
    e = Element ('Some string')
    t = titleElement('Title Line Here')
    b = bodyElement ('Some body text')
    h = headElement('Header line')
    p = pElement ('some paragraph text', style="text-align: center; font-style: oblique;", color="255")
    hr = hrElement ()
    br = brElement()
    e.append (t)
    e.append (h)
    e.append (b)
    b.append (p)
    b.append (hr)
    b.append (br)
    file_out = open('step5.txt', 'w')
    e.render (file_out, '    ')
    file_out.close() 
 
def testStepSix():
    e = Element ('Some string')
    t = titleElement('Title Line Here')
    b = bodyElement ('Some body text')
    h = headElement('Header line')
    p = pElement ('some paragraph text', style="text-align: center; font-style: oblique;", color="255")
    hr = hrElement ()
    br = brElement()
    anchor  = anchorElement('http://http://stackoverflow.com/questions', 'Get help here!')
    e.append (t)
    e.append (h)
    e.append (b)
    b.append (p)
    b.append (hr)
    b.append (br)
    b.append (anchor)
    file_out = open('step6.txt', 'w')
    e.render (file_out, '    ')
    file_out.close() 
  
def testStepSeven():
    e = Element ('Some string')
    t = titleElement('Title Line Here')
    b = bodyElement ('Some body text')
    h = headElement('Header line')
    e.append(t)
    p = pElement ('some paragraph text', style="text-align: center; font-style: oblique;", color="255")
    hr = hrElement ()
    br = brElement()
    header = headerElement (2, 'Now Hear This!')
    anchor  = anchorElement('http://http://stackoverflow.com/questions', 'Get help here!')
    e.append (h)
    e.append (b)
    b.append (header)
    b.append (p)
    b.append (hr)
    b.append (br)
    b.append (anchor)
    ul = ulElement(None, style="line-height:200%", id="TheList")
    li1 = liElement ('The first item in a list')
    li2 = liElement ('This is the second item', style="color: red")
    li3 = liElement ('And this is a')
    li3.append(anchor)
    li3.append('to StackOverflow')
    ul.append(li1)
    ul.append(li2)
    ul.append(li3)
    b.append(ul)
    file_out = open('step7.txt', 'w')
    e.render (file_out, '    ')
    file_out.close() 
    
def testStepEight():
    base = htmlElement ('Some string')
    t = titleElement('Title Line Here')
    m = metaElement ('charset="UTF-8"')
    b = bodyElement ('Some body text')
    h = headElement()
    h.append(m)
    h.append(t)
    p = pElement ('some paragraph text', style="text-align: center; font-style: oblique;", color="255")
    hr = hrElement ()
    br = brElement()
    header = headerElement (2, 'Now Hear This!')
    anchor  = anchorElement('http://http://stackoverflow.com/questions', 'Get help here!')
    base.append (h)
    base.append (b)
    b.append (header)
    b.append (p)
    b.append (hr)
    b.append (br)
    b.append (anchor)
    ul = ulElement(None, style="line-height:200%", id="TheList")
    li1 = liElement ('The first item in a list')
    li2 = liElement ('This is the second item', style="color: red")
    li3 = liElement ('And this is a')
    li3.append(anchor)
    li3.append('to StackOverflow')
    ul.append(li1)
    ul.append(li2)
    ul.append(li3)
    b.append(ul)
    file_out = open('step8.txt', 'w')
    base.render (file_out, '    ')
    file_out.close()   
    
if __name__ == '__main__':
    testStepOne()
    testStepTwo()
    testStepThree()
    testStepFour()
    testStepFive()
    testStepSix()
    testStepSeven()
    testStepEight()
