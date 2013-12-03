"""
Python decorator example

simple decorator that turns any function that returns a string
into one that returns that string wrapped in the html <p> tag:

@p_wrapper
def func():
    " simplest example possible"
    return "this is the returned string"

>> func()

"<p> this is the returned string </p>"

Advanced:

Try using a class to make a decorator that will wrap a
specified tag around a function that returns a string -- i.e:

@tag_wrapper('h1')
def func2(x, y=4, z=2):
    return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

>>> print func2(3,4)
<h1>the sum of 3 and 4 and 2 is 9</h1>


"""

from p_wrapper import p_wrapper, tag_wrapper
#from p_wrapper_solution import p_wrapper, tag_wrapper


def test_simple_func():
    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the raw version"
    print func()

    assert func() == "this is the returned string"

    # now add the decorator:
    @p_wrapper
    def func():
        " simplest example possible"
        return "this is the returned string"

    print "the decorated version"
    print func()

    assert func() == "<p> this is the returned string </p>"

def test_more_complex_function():
    # # try it with another function

    @p_wrapper
    def func2(x,y):
        return "the sum of %s and %s is %s"%(x, y, x+y)

    # call it:
    print func2(3,4)

    assert func2(3,4) == "<p> the sum of 3 and 4 is 7 </p>"

def test_func_with_keywords():
    # # and one with keyword arguments

    @p_wrapper
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    # call it:
    print func2(3)
    print func2(3, 5)
    print func2(3, 5, 7)

    assert func2(3,5,7) == "<p> the sum of 3 and 5 and 7 is 15 </p>"

## testing the class version
def test_class_decorator():

    @tag_wrapper('h1')
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    print func2(3,4)

    assert func2(3,4) == "<h1> the sum of 3 and 4 and 2 is 9 </h1>"

def test_class_decorator_div():

    @tag_wrapper('div')
    def func2(x, y=4, z=2):
        return "the sum of %s and %s and %s is %s"%(x, y, z, x+y+z)

    print func2(5,6,7)

    assert func2(5,6,7) == "<div> the sum of 5 and 6 and 7 is 18 </div>"

