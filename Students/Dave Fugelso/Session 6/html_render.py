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
    
    def __init__ (self, content=None):
        if content:
            self.contents = [content]
        else:
            self.contents = []
        
    def append(self, added_content):
        '''
        Add content to existing content, if any.
        '''
        self.contents.append (added_content)


        
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''
        file_out.write (ind + '<'+self.tag+'>\n')
        for content in self.contents:
            file_out.write (ind+self.indent+content+'\n')
        file_out.write (ind+'</'+self.tag+'>\n')
        
        
'''        
Step 2
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

class titleElement (Element):
    '''
    Sub class Element to replace tag 'html' with 'title' 
    '''
    tag = 'title'

class headElement (Element):
    '''
    Sub class Element to replace tag 'html' with 'head' 
    '''
    tag = 'head'

class  OneLineTag (Element):
    '''
    Re-defines render top print on one line.
    '''
    def render self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''

        for content in self.contents:
            file_out.write (ind+'<'+self.tag+'>'+self.indent+content+'\n'+'>/'+self.tag+'>')
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Test code


def testStepOne ():
    e = Element ('Some string')
    e.append ('some other string')
    file_out = open('base_element.txt', 'w')
    e.render (file_out, '    ')
    file_out.close()  
    
def testStepTwo():
    b = bodyElement ('Some body text')
    p = pElement ('some paragraph text')
    file_out = open('body_and_paragraph_element.txt', 'w')
    b.render (file_out, '    ')
    p.render (file_out, '    ')
    file_out.close()    

if __name__ == '__main__':
    testStepOne()
    testStepTwo()
