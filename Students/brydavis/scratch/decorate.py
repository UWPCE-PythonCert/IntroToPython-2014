def scratch():
	def decorate_me(func,x):
		return 'Decorative text: %s' % func(x)

	def wrap_me(func,x):
		return 'Wrapper text: %s' % func(x)

	def say_hello(x):
		return 'Hello, %s' % x

	print wrap_me(say_hello,'Bob')

	# @decorate_me()