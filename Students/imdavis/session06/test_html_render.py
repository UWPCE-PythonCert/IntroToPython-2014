#!/usr/bin/env python2.7

"""
Some unit testing for our HTML renderer

Make sure that pytest is installed.
Since the name of this testing script file begins with 'test_'
pytest will find it and run it.

In the directory where this file lives, simply do:
    $ py.test
    -or-
    $ py.test -s (will show print statements)

For more information, see: www.pytest.org
"""

from cStringIO import StringIO
import html_render

indent_spaces = "    "

def render_element(element, ind=""):
    """
    call the render method of an elemnet and return elements as a string
    """
    f = StringIO()
    element.render(f, ind)
    f.reset()
    output = f.read()
    return output

def test_init():
    """
    can we even initialize an Element
    """
    html_render.Element()
    assert True

def test_init_content():
    """
    now can we initialize an Element with some content
    """
    html_render.Element("some content")
    assert True

def test_render_content():
    """
    Can we initialize an Element with some content?
    Does it begin and end with the correct tag?
    Does the 'append' method work?
    """
    e = html_render.Element("this is some content")
    e.append("and this is some more")

    output = render_element(e)

    assert output.startswith('<html>')
    assert output.endswith('</html>\n')
    assert "this is some content" in output
    assert "and this is some more" in output
    print ("\n" + output)

def test_render_content_indent():
    """
    Is the indent level correct?
    """
    e = html_render.Element("this is some content")
    e.append("and this is some more")

    output = render_element(e)
    lines = output.split("\n")
    print lines
    assert lines[1].startswith(indent_spaces)

def test_render_html():
    """
    Can we initialize an 'Html' object with some content?
    Does it begin and end with the correct tag?
    Does the 'append' method work?
    Do we get the correct 'DOCTYPE' at the beginning?
    """
    e = html_render.Html("this is some content")
    e.append("and this is some more")

    output = render_element(e)
    print ("\n" + output)
    lines = output.split("\n")
    assert "this is some content" in output
    assert "and this is some more" in output
    assert "<!DOCTYPE html>" in lines[0]
    assert "<html>" in lines[1]
    assert output.endswith('</html>\n')
    assert lines[2].startswith(indent_spaces)

def test_render_body():
    """
    Can we initialize a 'Body' object with some content?
    Does it begin and end with the correct tag?
    Does the 'append' method work?
    """
    e = html_render.Body("this is some content")
    e.append("and this is some more")

    output = render_element(e)
    lines = output.split("\n")
    print ("\n" + output)
    assert output.startswith("<body>")
    assert output.endswith("</body>\n")
    assert "this is some content" in output
    assert "and this is some more" in output
    assert lines[1].startswith(indent_spaces)

def test_render_p_indent():
    content = "a simple paragraph"
    p = html_render.P(content)
    output = render_element(p, indent_spaces)
    lines = output.split("\n")
    print ("\n" + output)
    assert output.startswith(indent_spaces + "<p>")
    assert output.endswith(indent_spaces + "</p>\n")
    assert "{}{}".format(2*indent_spaces, content) in lines[1]

def test_render_sub_elements():
    content1 = "some simple text"
    content2 = "a simple paragraph"
    content3 = "a nested paragraph"
    e = html_render.Html(content1)
    p = html_render.P(content2)
    p.append(html_render.P(content3))
    e.append(p)

    output = render_element(e)
    print ("\n" + output)
    lines = output.split('\n')
    assert lines[1].startswith("<html>")
    assert output.endswith("</html>\n")
    assert "{}{}".format(indent_spaces, content1) in lines[2]
    assert "{}{}".format(indent_spaces, content1) in lines[2]
    assert "{}{}".format(2 * indent_spaces, content2) in lines[4]
    assert "{}{}".format(3 * indent_spaces, content3) in lines[6]

def test_onelinetag():
    o = html_render.OneLineTag("content")
    output = render_element(o, indent_spaces)
    print ("\n" + output)
    assert "{}{}{}{}".format(indent_spaces, "<html>", "content", "</html>\n") == output

def test_title():
    t = html_render.Title("A Title")
    output = render_element(t, indent_spaces)
    print ("\n" + output)
    assert "{}{}{}{}".format(indent_spaces, "<title>", "A Title", "</title>\n") == output

def test_attributes():
    a = html_render.P("some text", id="TheList", style="line-height:200%")
    output = render_element(a, indent_spaces)
    print ("\n" + output)
    lines = output.split('\n')
    assert lines[0].startswith(indent_spaces + "<p ")
    assert ('id="TheList"' and 'style="line-height:200%"') in lines[0]
    assert lines[0].endswith(">")
    assert (2 * indent_spaces + "some text") == lines[1]
    assert (indent_spaces + "</p>") == lines[-2]

def test_selfclosing_attr():
    a = html_render.A("www.alink.com", "link", id="cat", style="hat")
    output = render_element(a, indent_spaces)
    print ("\n" + output)
    assert output.startswith(indent_spaces + "<a ")
    assert ('style="hat"' and 'id="cat"' and 'href="www.alink.com"') in output
    assert output.endswith(">link</a>\n")

def test_header():
    sometext = "Header text"
    h = html_render.H(2, sometext)
    output = render_element(h, indent_spaces)
    print ("\n" + output)
    assert "{}{}{}{}".format(indent_spaces, "<h2>", sometext, "</h2>\n") == output
