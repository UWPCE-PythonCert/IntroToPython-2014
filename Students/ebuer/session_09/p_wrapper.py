#decorator lab

"""Write a simple decorator that returns a string wrapped in an html tag
Extra credit, allow user to pass the tag"""

# dummy func to return a string

def p_wrapper(func):
    def wrapped(*args):
        result = func(*args)
        return '<p> {} </p>'.format(result)
    return wrapped


class tag_wrapper(object):
    """remember that a class is just a collection of objects
       with its own namespace"""

    def __init__(self, tag='p'):
        self.tag = tag

    def __call__(self, func):
        print 'The function has been called'

        def wrapped_func(*args):
            tagged_r = '<{t}> {} </{t}>'.format(t=self.tag, *args)
            print 'fargs run'
            return tagged_r
        return wrapped_func


@p_wrapper
def dummyfunc(s):
    return str(s)

teststr = 'Your mom is 223 kg with makeup'

dummyfunc(teststr)
