'''
Eric Rosko
lambda_keyword.py
Tuesday, Nov. 11, 2015

Description:
	Trying to pass the tests in test_lambda.py using both a lamba and
	a comprehension.  To run each one, comment out the other since I'm
	using the same function name for each one.

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest
Usage: 
	py.test -v series.py
	or
	python3 series.py

'''

def function_builder(n):
	fns=[]
	for i in range(0,n):
		fns.append( lambda x, e=i: x+e )

	return fns
