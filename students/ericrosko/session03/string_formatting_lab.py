'''
Eric Rosko
string_formatting_lab.py
Tuesday, Nov. 10, 2015

Description:
	Part 1 of Session 3 homework

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest
Usage: 
	py.test -v series.py
	or
	python3 series.py

'''

def format_string_one(one, two, three):
	return "file_00{} :   {:.2f}, {:.0e}".format(one,two,three)

def format_string_two(mytuple):
	return "The first {:d} numbers are: {}".format(len(mytuple), mytuple)

if __name__ == "__main__":
	pass

def test_format_string_one():
	assert format_string_one(2, 123.4567, 10000) == "file_002 :   123.46, 1e+04"

def test_format_string_two():
	assert format_string_two( (4,5,6)) == 'The first 3 numbers are: (4, 5, 6)'