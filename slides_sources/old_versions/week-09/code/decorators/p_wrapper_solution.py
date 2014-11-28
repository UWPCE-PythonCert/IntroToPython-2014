"""
Python decorator example

Simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

func()

"""

# the simple decorator

def p_wrapper(func):
    def function(*args, **kwargs):
        result = func(*args, **kwargs)
        return "<p> " + result + " </p>"
    return function

"""

Fancier decorator using a class:

this lets you make a decorator with some custom input
the argument to the __init__ sets what tag you want
this creates a custom decorator
the __call__ method is the decorator itself.

"""

class tag_wrapper(object):
    def __init__(self, tag='p' ):
        """
        inititilze the decorator class with the tag you want
        """
        self.open_tag = "<%s> "%tag
        self.close_tag = " </%s>"%tag

    def __call__(self, func, *args, **kwargs):
        """
        The actual decorator function.

        using lambda - 'cause why not?
        """
        return lambda *args, **kwargs: self.open_tag + func(*args, **kwargs) + self.close_tag

