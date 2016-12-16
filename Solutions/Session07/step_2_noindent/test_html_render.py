"""
test code for html_render.py

includes through step 2 without indentation
"""
import io

from html_render import Element, Html, Body, P, TextWrapper


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


# These two tests were testing internals
# so they failed when I added the TextWrapper
# but I"m removing them because tests really should be testing
# the external API.
# def test_content():
#     # fixme: this tests internals!!!!
#     e = Element("this is some text")

#     assert "this is some text" in e.content

# def test_append():
#     e = Element("this is some text")

#     e.append("some more text")

#     assert "some more text" in e.content


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


def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.strip().endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.strip().endswith("</p>")


def test_text_wrapper():
    tw = TextWrapper("A basic piece of text")

    file_contents = render_result(tw)
    assert file_contents == "A basic piece of text"


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)

    # note: the above tests should make sure that the tags are getting rendered.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents


def test_step_2_noindent():
    """
    This is more if an integration test -- a number of things together

    this test does not yet include indentation
    """
    page = Html()
    body = Body()
    page.append(body)
    body.append(P("a small paragraph of text"))
    body.append(P("another small paragraph of text"))
    body.append(P("and here is a bit more"))

    file_contents = render_result(page).strip()

    print(file_contents)
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")
    assert "a small paragraph of text" in file_contents
    assert "<body>" in file_contents
    # you could do more here, but it should all be covered above.
    assert False

