
import html_render as hr
from io import StringIO

import re # import regular expressions so I can strip spaces and \n's from text

def test_instantiate():
	e = hr.Element()

def test_create_content():
	e = hr.Element("stuff")
	assert e.content is not None

def test_content_None():
	e = hr.Element()
	print (e.content)
	assert None not in e.content

def test_content_This():
	e = hr.Element("this")
	print (e.content)
	assert "this" in e.content

def test_tag():
	e = hr.Element("this")
	assert hr.Element.tag == 'html'

def test_append():
	e = hr.Element('this')
	e.append('that')
	assert 'that' in e.content
	assert 'this' in e.content

def test_render():
	e = hr.Element("this")
	e.append('that')
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()

	assert text.startswith("<html>")
	assert text.endswith("</html>")
	assert 'this' in text
	assert 'that' in text

def test_body():
	e = hr.Body('this')
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()
	assert text.startswith("<body>")
	assert text.endswith("</body>")
	assert 'this' in text

def test_p():
	e = hr.Element("this")
	e.append(hr.P('paragraph of text'))
	e.append(hr.P('another paragraph of text'))
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()
	print(text)
	assert '<p>' in text
	assert '</p>' in text
	assert '<html>' in text
	assert '</html>' in text
	assert 'paragraph of text' in text

def test_nest():
	e = hr.Element()
	body = hr.Body()
	e.append(body)
	body.append(hr.P('a paragraph of text'))
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()

    #use regex to remote pretty printing spaces and new line carriage returns
	text = re.sub('[\n ]','',text)
	print(text)
	assert text.startswith('<html><body>')
	assert text.endswith('</body></html>')

def test_title():
	e = hr.Title('this')
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()
	assert text.startswith("<title>")
	assert text.endswith("</title>")
	assert 'this' in text

def test_paragraph_with_style_string():
	e = hr.Element()
	body = hr.Body()

	body.append(hr.P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text", style="text-align: center; font-style: oblique;"))
	
	f = StringIO()
	e.render(f)
	f.seek(0)
	text = f.read().strip()
	assert text.find("<p style=\"text-align: center; font-style: oblique;\">")

def test_hr():
	html = hr.Html()
	head = hr.Head()
	head.append( hr.Title("PythonClass = Revision 1087:") )
	html.append(head)
	body = hr.Body()
	horizontal_rule = hr.Hr()
	body.append(horizontal_rule)
	html.append(body)

	f = StringIO()
	html.render(f)
	f.seek(0)
	text = f.read().strip()
	print(text)
	assert text.find("<hr />")!= -1

def test_a():
	html = hr.Html()
	head = hr.Head()
	head.append( hr.Title("PythonClass = Revision 1087:") )
	html.append(head)
	body = hr.Body()
	horizontal_rule = hr.Hr()
	body.append(horizontal_rule)
	body.append(hr.A("http://google.com", "link"))
	html.append(body)

	f = StringIO()
	html.render(f)
	f.seek(0)
	text = f.read().strip()
	print(text)
	assert text.find("<a href=\"http://google.com\">link</a>")!= -1
	#assert True

def test_h2():
	html = hr.Html()
	body = hr.Body()
	body.append(hr.H(2, "sample"))
	html.append(body)

	f = StringIO()
	html.render(f)
	f.seek(0)
	text = f.read().strip()
	print(text)
	assert text.find("<h2>sample</h2>") != -1
