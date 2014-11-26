#!/usr/bin/env python

"""
unit tests for html rendering code
"""

from cStringIO import StringIO

import html_render as hr


## utility function for tests:
def render_element(element, ind=""):
    """
    call the render method of an element and return the results as a string
    """
    f = StringIO()
    element.render(f, ind)
    f.reset()
    output = f.read()
    return output # we don't care about leading/trailing whitespace

## these should all pass with my framework code.


def test_init():
    " can I even initialize an Element"
    hr.Element()
    assert True


def test_init_content():
    " can I even initialize an Element with content"

    hr.Element("this is some text")

    assert True


def test_element_content():
    """ should be able to initilize with a string"""
    hr.Element("some content")


## these should pass after part 1


def test_render_content1():
    """ does the render method work """
    e = hr.Element("this is some content")

    output = render_element(e)

    assert output.startswith('<html>')
    assert output.endswith('</html>\n')
    assert "this is some content" in output


def test_render_content2():
    """ does the render method work after appending a string """
    e = hr.Element("this is some content")
    e.append("and this is some more")

    output = render_element(e)

    assert output.startswith('<html>')
    assert output.endswith('</html>\n')
    assert "this is some content" in output
    assert "and this is some more" in output
    print output


def test_render_content_indent():
    """ does the render method work after appending a string """
    e = hr.Element("this is some content")
    e.append("and this is some more")

    output = render_element(e)
    lines = output.split('\n')
    print lines
    assert lines[1].startswith("    ")


## this one no longer currect with step 8 added
# def test_render_html():
#     """ the html element """

#     e = hr.Html("this is some content")
#     e.append("and this is some more")

#     output = render_element(e)

#     print output
#     assert output.startswith('<html>')
#     assert output.endswith('</html>\n')
#     assert "this is some content" in output
#     assert "and this is some more" in output


def test_render_body():
    """ the html element """

    e = hr.Body("this is some content")
    e.append("and this is some more")

    output = render_element(e)

    print output
    assert output.startswith('<body>')
    assert output.endswith('</body>\n')
    assert "this is some content" in output
    assert "and this is some more" in output


def test_render_p_indent():
    p = hr.P("a simple paragraph")
    output = render_element(p, "        ")

    print output
    lines = output.split('\n')

    assert lines[0].startswith("        ")
    assert lines[1].startswith("            ")
    assert lines[2].startswith("        ")


def test_render_sub_elements():
    e = hr.Html("some simple text")
    p = hr.P("a simple paragraph")
    p.append(hr.P("a nested paragraph"))

    e.append(p)

    output = render_element(e)

    print output
    lines = output.split('\n')
    lines[0].startswith('<html>')
    lines[1].startswith('    ')
    lines[3].startswith('        ')
    lines[5].startswith('            ')
    lines[-1].startswith('</html>')


def test_one_line_tag():
    e = hr.OneLineTag('something')
    output = render_element(e, ind="    ")

    print output

    assert output == "    <html>something</html>\n"


def test_attributes():
    e = hr.P("some text", id="TheList", style="line-height:200%")

    output = render_element(e, ind="    ")

    print output

    lines = output.split('\n')
    assert 'id="TheList"' in lines[0]
    assert 'style="line-height:200%"' in lines[0]


def test_attributes_one_line():
    e = hr.Title("some text", id="TheList", style="line-height:200%")

    output = render_element(e, ind="    ")

    print output

    lines = output.split('\n')
    assert 'id="TheList"' in lines[0]
    assert 'style="line-height:200%"' in lines[0]


def test_self_closing():
    e = hr.Hr()
    output = render_element(e, ind="    ")

    print output
    assert output == "    <hr />\n"


def test_self_closing_attr():
    e = hr.Hr(id='fred', style='box')
    output = render_element(e, ind="    ")

    print output
    assert output == '    <hr style="box" id="fred" />\n'


def test_anchor():
    e = hr.A("http://google.com", "link to google")

    output = render_element(e, ind="    ")

    print output
    assert output == '    <a href="http://google.com">link to google</a>\n'


def test_header():
    e = hr.H(2, "The text of the header")

    output = render_element(e, ind="    ")

    print output
    assert output == '    <h2>The text of the header</h2>\n'


def test_header3():
    e = hr.H(3, "The text of the header")

    output = render_element(e, ind="    ")

    print output
    assert output == '    <h3>The text of the header</h3>\n'


def test_doctype():
    """
    html element should render teh doctype header, too
    """

    e = hr.Html("Just a tiny bit of content")

    output = render_element( e )

    print output
    assert output.startswith("<!DOCTYPE html>")
    assert "<html>" in output
    assert output.endswith("</html>\n")

