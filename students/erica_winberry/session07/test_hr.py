from io import StringIO

import html_render as hr


def test_init():
    hr.Element()


def test_init2():
    hr.Element("test string")


def test_init_keywords():
    hr.Element("test string", test="more tag text here")


def test_content():
    e = hr.Element("some text")
    assert e.content is not None


def test_content_None():
    e = hr.Element()
    print(e.content)
    assert None not in e.content


def test_content_not_None():
    e = hr.Element("this")
    print(e.content)
    assert "this" in e.content


# def test_tag():
#     e = hr.Element("this")
#     assert hr.Element.tag == "html"
#     assert e.tag == "html"


def test_append():
    e = hr.Element("this")
    e.append("that")
    assert "that" in e.content
    assert "this" in e.content


def test_render():
    e = hr.Element("this")
    e.append("that")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert "this" in text
    assert "that" in text


def test_render_keywords():
    e = hr.Html("this", style='test')
    e.append("that")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<html style="test">')
    assert text.endswith('</html>')
    assert "this" in text


def test_Html():
    e = hr.Html("this")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<html>")
    assert text.endswith("</html>")
    assert "this" in text


def test_Body():
    e = hr.Body("this")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<body>")
    assert text.endswith("</body>")
    assert "this" in text


def test_Para():
    e = hr.Paragraph("this")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<p>")
    assert text.endswith("</p>")
    assert "this" in text


def test_Head():
    e = hr.Head("this")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<head>")
    assert text.endswith("</head>")
    assert "this" in text


def test_Link():
    e = hr.Link(link="link URL", content="link content")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<a href")
    assert text.endswith("</a>")
    assert "link content" in text


def test_OneLine_Title():
    e = hr.Title("this")
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<title>")
    assert text.endswith("</title>")
    assert "this" in text


def test_SelfClosing_HRule():
    e = hr.HRule()
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith("<hr />")


def test_nest():
    e = hr.Html()
    head = hr.Head()
    e.append(head)
    title = hr.Title("Your title goes here")
    head.append(title)
    body = hr.Body()
    e.append(body)
    p = hr.Paragraph("A paragraph of text", style="testy")
    body.append(p)
    br = hr.LineBreak()
    body.append(br)
    p = hr.Paragraph("Another paragraph of text")
    body.append(p)
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()

    print(text)
    assert False

    # assert text.startswith("<p>")
    # assert text.endswith("</p>")
    # assert "this" in text
