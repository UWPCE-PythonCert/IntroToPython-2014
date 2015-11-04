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

# Another solution (these are not complete!):

def fizzbuzz2(n):
    for i in range(1, n+1):
        msg = " "
        if i % 3 == 0
            msg += "fizz"
        elif i % 5 == 0
            msg += "buzz"



        for i in range(1, n + 1)
            msg = "fizz" if i % 3 = 0 else " "
            msg += "buzz" if i % 5 == 0 else " "
            print(msg or i)

for i in range(1, n + 1): print("fizz" * (not (1 % 3))) + "buzz" * (not( 1 % 5))