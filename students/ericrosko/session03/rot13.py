'''
Eric Rosko
rot13.py
Tuesday, Nov. 10, 2015

Description:
	Implementation of ROT13

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest
Usage: 
	py.test -v series.py
	or
	python3 series.py

'''

def rot13(string_input):
	'''
	Implementation or ROT13.  Just pass in a string!
	'''
	result=""
	for n in string_input:
		if n.islower():
			value = ord(n)+13
			if value > 122:
				value = 97+value-123
			result+=chr(value)
		elif n.isupper():
			value = ord(n)+13
			if value > 90:
				value = 65+value-91
			result += chr(value)
		else:
			result += n

	return result

if __name__ == "__main__":
	assert rot13("a") == "n"
	assert rot13("A") == "N"
	assert rot13("z") == "m"
	assert rot13("Z") == "M"
	assert rot13("Uryyb, jbeyq!") == "Hello, world!"
	assert rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner"

def test_rot13_a():
	assert rot13("a") == "n"

def test_rot13_A():
	assert rot13("A") == "N"

def test_rot13_z():
	assert rot13("z") == "m"

def test_rot13_Z():
	assert rot13("Z") == "M"
	
def test_rot13_punctuation():
	assert rot13("Uryyb, jbeyq!") == "Hello, world!"

def test_rot13():
	assert rot13("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner"
