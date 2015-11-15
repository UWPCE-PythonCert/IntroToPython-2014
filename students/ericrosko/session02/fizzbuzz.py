'''
by Eric Rosko
Tuesday, Nov. 10, 2015

Description:
	Implementation of FizzBuzz using TDD

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest
Usage: 
	py.test -v fizzbuzz.py
	or
	python3 fizzbuzz.py

'''

def create_array(n=100):
	array = []
	for i in range(1,n+1):
		array.append(i)
	return array

def fizzbuzz(array=create_array()):
	output = ""
	for n in array:

		multiple3 = n%3
		multiple5 = n%5

		if not multiple3 and not multiple5:
			output += "FizzBuzz "
		elif not multiple3:
			output += "Fizz "
		elif not multiple5:
			output += "Buzz "
		else:
			output += "{0} ".format(n)
	
	# remove trailing space
	output=output.strip()
	
	return output
	

if __name__ == "__main__":
	print(fizzbuzz())

#
# tests
#
def test_create_array():
	assert create_array(2) == [1,2]

def test_create_array_default_array():
	assert create_array() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def test_multiple_of_three():
	assert fizzbuzz([3]) == "Fizz"

def test_multiple_of_five():
	assert fizzbuzz([20]) == "Buzz"

def test_multiple_of_five_and_three():
	assert fizzbuzz([15]) == "FizzBuzz"

def test_multiple_of_neither_3_nor_5():
	assert fizzbuzz([1]) == "1"

def test_up_to_16():
	assert fizzbuzz(create_array(16)) == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16"

def test_full_output():
	assert fizzbuzz() == "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz"
