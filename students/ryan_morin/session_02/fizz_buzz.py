__author__ = 'Ryan'

def FizzBuzz(num):
    """
    :param num: number 100
    :return: print values and string based on logic statements
    """
    for num in range(1, (num + 1)):
        if num%15 == 0:
            print ("FizzBuzz")
        elif num%3 == 0:
            print ("Fizz")
        elif num%5 == 0:
            print ("Buzz")
        else:
            print (num)

print(FizzBuzz(100))