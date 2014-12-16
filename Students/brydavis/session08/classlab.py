#!/usr/bin/env python

class Circle(object):
	"""docstring for Circle"""

	def __init__(self, radius):
		self.radius = radius

	@property
	def diameter(self):
	    return self._diameter
	
	@diameter.setter
	def diameter(self, value):
	    self.radius = value / 2

	
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		