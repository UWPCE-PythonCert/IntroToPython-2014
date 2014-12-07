'''
p_wrapper.py

Define p_wrapper and tag_wrapper decorators.

Since we aren't saving any state info will not use callable class. For p_wrapper.

For tag_wrapper gonna make it callable class

'''



def p_wrapper (func):
    def string_return (string):
        return '<p> '+string+' </p>'
    return string_return
    
class tag_wrapper (object):

    def __init__(self, tag):
        #print "Inside __init__()"
        self.tag = tag
    
    def __call__(self, string):
        #print "Inside __call__()"
        def tagged_line (string):
           # print 'decorator'
           # print '<'+self.tag+'> '+string+' </'+self.tag+'>'
            return '<'+self.tag+'> '+string+' </'+self.tag+'>'
        return tagged_line
        
