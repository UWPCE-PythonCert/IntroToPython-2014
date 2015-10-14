def divThree(n):
	return n % 3 == 0


def divFive(n):
	return n % 5 == 0


for number in range(101):
	if divThree(number) and divFive(number):
		print ("FizzBuzz")
	elif divThree(number) and not divFive(number):
		print ("Fizz")
	elif not divThree(number) and divFive(number):
		print ("Buzz")
	else:
		print (number)