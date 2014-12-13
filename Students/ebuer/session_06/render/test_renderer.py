"""test_renderer.py
"""

import html_render_refactor as hr
from html_render_refactor import Element
from cStringIO import StringIO
from io import open, StringIO

## utility function for tests:
def render_element(element, ind=""):
    """
    call the render method of an element and return the results as a string
    """
    f = StringIO()
    element.render(f, ind)
    f.seek(0)
    output = f.read()
    return output # we don't care about leading/trailing whitespace

def test_Element():
    assert Element is not None
    assert Element.tag == 'html'
    assert Element.indent == '    '


def test_elappend():
    e = Element('test content')
    e.append('test')

    assert e.content == ['test content', 'test']

def test_render():
    e = Element('test content')

    output = render_element(e)
    print output

    assert '<html>' in output
    assert 'test content' in output
    assert '</html>' in output
