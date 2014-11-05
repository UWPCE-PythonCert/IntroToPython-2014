'''
start of html_render.py

Step 1.

Create the element class.
'''

Create an Element class for rendering an html element (xml element).

It should have class attributes for the tag name (“html” first) and the indentation (spaces to indent for pretty printing)

The constructor signature should look like

Element(content=None)
where content is a string

It should have an append method that can add another string to the content.

It should have a render(file_out, ind = "") method that renders the tag and the strings in the content.

file_out could be any file-like object ( i.e. have a write() method ).

ind is a string with the indentation level in it: the amount that the tag should be indented for pretty printing.

This is a little tricky: ind will be the amount that this element should be indented already. It will be from zero (an empty string) to a lot of spaces, depending on how deep it is in the tree.
The amount of indentation should be set by the class attribute: indent

You should now be able to render an html tag with text in it as contents.

class Element(object):
    tag = 'html'
    indent = ''   
    
    def __init__self, content=None):
        self.content = content

        
    def append(self, added_content):
        '''
        Add content to existing content, if any.
        '''
        if self.content:
            self.content = self.content+added_content
        
    def render (self, file_out, ind = ''):
        '''
        Render the line to file_out.write.
        '''
        
        