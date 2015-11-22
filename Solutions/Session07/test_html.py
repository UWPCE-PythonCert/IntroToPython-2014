
from io import StringIO

import html_render as hr


def render_me(element):
    """A utility to render an element so you can see if it's doing the right thing"""
    f = StringIO()
    element.render(f)
    f.seek(0)
    return f.read()


def test_init():
    hr.Element()


def test_init2():
    hr.Element("some text")


def test_content():
    e = hr.Element("some text")
    assert e.content is not None


def test_content_none():
    e = hr.Element()
    print(e.content)
    assert None not in e.content


def test_content_str():
    e = hr.Element("this")
    print(e.content)
    assert "this" in e.content


def test_tag():
    e = hr.Element("this")
    assert hr.Element.tag == 'html'
    assert e.tag == 'html'


def test_append():
    e = hr.Element("this")
    e.append("that")
    assert 'that' in e.content
    assert 'this' in e.content


def test_render():
    e = hr.Element("this")
    e.append("that")
    text = render_me(e).strip()
    assert text.startswith("<html>")
    assert text.endswith("</html>")
    assert "this" in text
    assert "that" in text


def test_body():
    e = hr.Body("this")
    text = render_me(e).strip()
    assert text.startswith("<body>")
    assert text.endswith("</body>")
    assert "this" in text


def test_p():
    e = hr.P("this")
    text = render_me(e).strip()
    assert text.startswith("<p>")
    assert text.endswith("</p>")
    assert "this" in text


def test_nest():
    e = hr.Element()
    p = hr.P("a paragraph of text")
    e.append(p)
    p = hr.P("another paragraph of text")
    e.append(p)

    text = render_me(e).strip()
    print(text)
    # there should be two <p> tags in there:
    assert text.count("<p>") == 2
    # and two closing tags
    assert text.count("</p>") == 2
    # and one <html> tag
    assert text.count("<html>") == 1
    assert text.count("</html>") == 1
    # and the text:
    assert "a paragraph of text" in text
    assert "another paragraph of text" in text
