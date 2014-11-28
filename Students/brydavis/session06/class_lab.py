def function_builder(n):	
	return [lambda x: x+i for i in range(n+1)]



class Point(object):
	size = 4
	color = 'red'

	def __init__(self, x,y):
		self.x = x
		self.y = y

	def xy(self):
	    return self.x * self.y

	def new_color(self,color=color):
		self.color = color
		# color = color

	def new_size(self,size=size):
		self.size = size


		