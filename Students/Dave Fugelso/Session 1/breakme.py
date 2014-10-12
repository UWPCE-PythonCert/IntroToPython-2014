'''
In the break_me.py file write four simple Python functions:

Each function, when called, should cause an exception to happen
Each function should result in one of the four common exceptions from our lecture.
for review: NameError, TypeError, SyntaxError, AttributeError


Use the Python standard library reference on Built In Exceptions as a reference
'''

def nameErrorExample():
   t = somethingThatDoesntExist()
   
def typeErrorExample ():
   a = 'Hello, World!'
   worlds = 1
   worlds = worlds + a

def syntaxErrorExample ():
#   a = 'some string'
#   a.print()
   pass
  
import time  
def attributeErroexample():
   t = time.time
   b = t.newtime

#nameErrorExample()
#typeErrorExample ()
syntaxErrorExample ()
attributeErroexample()