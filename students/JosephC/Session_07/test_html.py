import html_render as hr
from io import StringIO

def render_me(element):
''' a utility to render an elment so you can see if its doing the right thing'''
   
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

def test_content_None():
    e = hr.Element()
    print(e.content)
    assert None not in e.content

def test_content_str():
    e = hr.Element('this')
    print(e.content)
    assert 'this' in e.content

def test_tag():
    e = hr.Element('this')
    assert hr.Element.tag == 'html'
    assert e.tag == 'html'

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
    assert "this" in text
    assert "that" in text
    print(text)
    assert False

def test_body():
    e = hr.Body('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<body>')
    assert text.endswith('</body>') 
    assert 'this' in test

def test_P():
    e = hr.Body('this')
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<p>')
    assert text.endswith('</p>') 
    assert 'this' in test

def test_nest():
    e = hr.Element()
    p = hr.P('a paragraph')
    e.append(p)
    f = StringIO()
    e.render(f)
    f.seek(0)
    text = f.read().strip()
    assert text.startswith('<p>')
    assert text.endswith('</p>') 
    assert 'this' in test
    
    print (text)
    assert False

def test_indent():
    p = hr.P('some text')
    f = StringIO()
    P.render(f)
    f.seek(0)
    text = f.read().strip()
