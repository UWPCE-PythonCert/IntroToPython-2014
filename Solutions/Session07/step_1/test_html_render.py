"""
test code for html_render.py

only step 1
"""

import io

from html_render import Element

# utility function for testing render methods
# needs to be used in multiple tests, so write it once here.


def render_result(element, ind=""):
    """
    calls element's render method, and returns what got rendered as a string
    """
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()


def test_init():
    """
    this only tests that it can be initialized -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_content():
    # fixme: this tests internals!!!!
    e = Element("this is some text")

    assert "this is some text" in e.content


def test_append():
    e = Element("this is some text")

    e.append("some more text")

    assert "some more text" in e.content


def test_two_instances():
    e = Element("this is some text")
    e2 = Element("this is some text")

    e.append("some more text")

    assert "some more text" not in e2.content


def test_render():
    e = Element("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")
