# html render code...here goes nothing...
# trying to build using your code but i just have no idea what to do...

class Element(object):
	tag = 'html'
	indent = '    '
	
	def __init__(self, content=None, **attributes): # defining the initializer
		self.content = []
		self.attributes = attributes
		if content is not None:
			self.content.append(content)
	
	def append(self, content): # defining how to append content
		self.content.append(content)
		
	def render_tag(self, current_ind): # defining the render tag
		attrbs = "".join(['{} = "{}"'.format(key, val) for key, val in self.attributes.ietms()])
		tag_str = "{}<{}{}>".format(current_ind, self.tag, attrbs)
		return tag_str
	
	def render(self, file_out, current_ind=""): # defining how the code renders and presents itself
		file_out.write(self.render_tag(current_ind))
		file_out.write('\n')
		for con in self.content:
			try:
				file_out.write(current_ind + self.indent + con + "\n")
			except TypeError:
				con.render(file_out, current_ind + self.indent)
		file_out.write("{}</{}>\n".format(current_ind, self.tag))
	
class OneLineTag(Element):
	def render(self, file_out, current_ind=""):
		file_out.write(self.render_tag(current_ind))
		for con in self.content:
			file_out.write(con)
		file_out.write("{}</{}>\n".format(self.tag))
		
class Title(OneLineTag):
	tag = 'title'
	
#def __init__(self, "Python is fun, Python is fast, Python is fascicular but not Macaca fascicularis!!"):
	#pass
#def append(self, "But what if Python WAS Macaca fascicularis? Well, for one thing that would be extremely weird,"/n "even if we consider the ramifications of Python being a member of the Animalia phylum,"/n "that would not grant them access to being a Primata. Could they breed with Macaca? Prezygotic barriers along with a multitude of other factors would say no."/n "I mean, c'mon, Macaca fascicularis would NEVER find Python sexy!"):
	#pass
#def render(self, file_out, ind=""):
	#pass
