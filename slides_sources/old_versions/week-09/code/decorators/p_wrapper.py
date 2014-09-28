"""
Python decorator example

Simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

>> func()

"<p> this is the returned string </p>"

"""

# the simple decorator

def p_wrapper(func):
    ## put decorator here
    pass



"""

Fancier decorator using a class:

This lets you make a decorator with some custom input

the argument to the __init__ sets what tag you want, which creates a custom decorator.

the __call__ method is the decorator itself.

"""

class tag_wrapper(object):
    def __init__(self, tag='p' ):
        """
        inititilze the decorator class with the tag you want
        """
        pass
    def __call__(self, func, *args, **kwargs):
        """
        The actual decorator function.
        """
        pass
        # return a_function...

