def fizzbuzz():
    for i in range(1,101):
        if ((0 == i % 5) and (0 == i % 3)):
            print("FizzBuzz")
        elif (0 == i % 5):
            print("Buzz")
        elif (0 == i % 3):
            print("Fizz")
        else:
            print(i)


fizzbuzz()


