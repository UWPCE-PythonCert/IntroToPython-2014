"""
test code for html_render.py

includes step 4
"""
import io

from html_render import (Element,
                         Html,
                         Body,
                         P,
                         TextWrapper,
                         Head,
                         Title,
                         )

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


def test_non_str():
    """ you should be able to pass anything in, and it will get
    "stringified"
    """
    e = P(34)  # a number
    e.append((3, 4, 5))  # even a tuple

    file_contents = render_result(e)

    print(file_contents)
    assert("34") in file_contents
    assert("(3, 4, 5)") in file_contents


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
    # assert False


def test_indent():
    """
    Tests that the indentation gets passed through to the renderer
    """
    html = Html("some content")
    file_contents = render_result(html, ind="   ")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    assert lines[-1].startswith("   <")


def test_indent_contents():
    """
    The contents in a element should be indented more than the tag
    by the amount in the indent class attribute
    """
    html = Html("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)


def test_multiple_indent():
    """
    make sure multiple levels get indented fully
    """
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):
        assert lines[i].startswith(i * Element.indent + "<")

    assert lines[3].startswith(3 * Element.indent + "some")


def test_title():
    """
    This will implicitly test the OneLineTag element
    """
    t = Title("Isn't this a nice title?")

    # making sure indentation still works
    file_contents = render_result(t, ind="   ")

    print(file_contents)
    # no "strip()" -- making sure there are no extra newlines
    assert "\n" not in file_contents
    assert ">    " not in file_contents
    assert file_contents.startswith("   <title>")
    assert file_contents.endswith("</title>")
    # the only newline should be at the end
    assert "\n" not in file_contents


def test_head():
    """
    testing Head with a title in it -- it should never be blank
    """
    h = Head()
    h.append(Title("A nifty title for the page"))


def test_full_page_with_title():
    """
    not much to actually test here, but good to see it put together.

    everything should have already been tested.
    """
    page = Html()

    head = Head()
    head.append(Title("PythonClass Example"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, "
                  "but this is enough  to show that we can do some text"))
    body.append(P("And here is another piece of text -- you should be able to add any number"))

    page.append(body)

    file_contents = render_result(page)

    print(file_contents)

    # uncomment this to see results
    # assert False


def test_attributes():
    """
    tests that you can pass attributes in to the tag
    """
    e = Element("some text", id="this", color="red")  # could be any attributes
    file_contents = render_result(e)
    print(file_contents)
    assert 'id="this"' in file_contents
    assert 'color="red"' in file_contents
    # note -- dicts aren't ordered, so you can't enforce order!
    # assert '<html color="red" id="this">' in file_contents


def test_attributes_one_line_tag():
    """
    tests that you can pass attributes in to the tag
    """
    e = Title("some text", id="this", color="red")  # could be any attributes
    file_contents = render_result(e)
    print(file_contents)
    assert 'id="this"' in file_contents
    assert 'color="red"' in file_contents


