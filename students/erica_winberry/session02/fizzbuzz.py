# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number
# For the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

def fizzbuzz():
    for i in range(1,101):
        if((i % 3 == 0) and (i % 5 == 0)):
            print("fizzbuzz")
            i += 1
        elif(i % 3 == 0):
            print("fizz")
            i += 1
        elif(i % 5 == 0):
            print("buzz")
            i += 1
        else:
            print(i)
            i += 1

fizzbuzz()
