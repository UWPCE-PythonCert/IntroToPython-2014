#!/usr/bin/env python




def f(x=None, *hello, **world):
	print "x is: ", x
	print "the positional arguments are:", hello
	print "the keyword arguments are:", world







class Trigram(str):
	""" Adding critically unimportant functionality to Python's str type """

	def len(self):
		return self.__len__()

	@property
	def length(self):
		return self.len()
		
	@property
	def frequency(self):
		arr = self.split()
		o = {}
		for i in arr:
			if i in o.keys():
				o[i] += 1            
			else:
				o[i] = 1            
		return o

	@property
	def model(self) :  
		self = self.split()
		o = {}
		len_self = len(self)

		for n,i in enumerate(self):
			pass
			# if n+1 <= len_self-1 :
			# 	k = s[i] + ' ' + s[i+1]
			# 	if o[k]: 
			# 		o[k].append(s[i+2])
			# 	else:
			# 		o[k] = [s[i+2]]
		return o
    


