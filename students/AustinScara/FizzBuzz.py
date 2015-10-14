def divThree(n):
	return n % 3 == 0


def divFive(n):
	return n % 5 == 0



for number in range(101):
	if divThree(number) is True and divFive(number) is True:
		print ("FizzBuzz")
	elif divThree(number) is True and divFive(number) is False:
		print ("Fizz")
	elif divThree(number) is False and divFive(number) is True:
		print ("Buzz")
	else:
		print (number)