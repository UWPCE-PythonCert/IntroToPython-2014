#!/usr/bin/env python 

# from sys import argv
# import requests

# html = argv[1] if len(argv) > 1 else \
# 	'http://uwpce-pythoncert.github.io/IntroToPython/_downloads/sample_html.html'

doctype = '<!DOCTYPE html><html><head><title></title>{style}</head><body>{body}</body></html>'
style = [
	'//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css',
	'./style/main.css',
	'./style/other.css',
	]

# The start of it all:
# Fill it all in here.
class Element(object):
	tag = 'div'

	def __init__(self, content=None):
		self.content = content
	
	def append(self, new_content):
		pass


	def render(self, file_out=None, ind=""):
		self.indent = ind
		
		css = ''
		for s in style:
			links = '<link rel="stylesheet" type="text/css" href="{style}">'.format(style=s)
			css += links

		title = 'New Page'
		body = '<{tag}>{content}</{tag}>'.format(tag=self.tag,content=self.content)

		return doctype.format(body=body,title=title,style=css)



if __name__ == '__main__':
	# print html

	element = Element('hello world')
	print element.render()






