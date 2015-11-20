from io import StringIO

import html_render as hr


def test_init():
    hr.Element()


def test_init2():
    hr.Element('some text')


def test_content():
    e = hr.Element('some text')
    assert e.content is not None


def test_content_str():
    e = hr.Element("this")
    print(e.content)
    assert "this" in e.content


def test_tag():
    assert hr.Element.tag == 'html'


def test_append():
    e = hr.Element('this')
    e.append('that')
    assert 'that' in e.content
    assert 'this' in e.content


def test_render():
    e = hr.Element('this')
    e.append('that')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<html>')
    assert text.endswith('</html>')
    assert 'this' in text
    assert 'that' in text


def test_body():
    e = hr.Body('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<body>')
    assert text.endswith('</body>')
    assert 'this' in text


def test_p():
    e = hr.P('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<p>')
    assert text.endswith('</p>')
    assert 'this' in text


def test_nest():
    e = hr.Element()
    p = hr.P('a paragraph of text')
    e.append(p)
    p = hr.P('a paragraph of text')
    e.append(p)
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<html>')
    assert text.endswith('</html>')
    assert text.count('<p>') == 2
    assert text.count('</p>') == 2
    assert text.count('a paragraph of text') == 2
    # use this to check output as you write tests
    # print(text)
    # assert False


def test_indentation():
    e = hr.Element()
    b = hr.Body()
    p = hr.P('a paragraph of text')
    b.append(p)
    p = hr.P('a paragraph of text')
    b.append(p)
    e.append(b)
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<html>')
    assert text.endswith('</html>')
    # these tests need work. adjust indent of <p> has no affect on test passing
    assert '    <html>' not in text
    assert '    <body>\n' in text
    assert '    </body>' in text
    assert '        <p>' in text
    assert '        </p>' in text
    # print(text)
    # assert False


def test_head():
    e = hr.Head()
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<head>')
    assert text.endswith('</head>')


def test_one_liner():
    e = hr.OneLineTag('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert 'this' in text
    assert '\n' not in text


def test_title():
    e = hr.Title('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<title>')
    assert text.endswith('</title>')
    assert 'this' in text
    assert '\n' not in text


def test_attributes():
    e = hr.P('a paragraph of text', id='"MyText"')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert 'id="MyText"' in text
    # print(text)
    # assert False
