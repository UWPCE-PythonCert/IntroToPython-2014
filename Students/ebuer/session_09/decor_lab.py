#decorator lab

"""Write a simple decorator that returns a string wrapped in an html tag
Extra credit, allow user to pass the tag"""

# dummy func to return a string

def p_wrapper(func):
    def wrapped(*args):
        result = func(*args)
        return '<p> {} </p>'.format(result)
    return wrapped


def tag_wrapper(func, tag):
    def twrapped(*args):

        return

@p_wrapper
def dummyfunc(s):
    return str(s)

teststr = 'Your mom is 223 kg with makeup'

dummyfunc(teststr)
