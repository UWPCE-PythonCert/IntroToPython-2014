def fizzbuzz():
    for i in range(100):
        i += 1
        if ((0 == i % 5) and (0 == i % 3)):
            print("FizzBuzz")
        elif (0 == i % 5):
            print("Buzz")
        elif (0 == i % 3):
            print("Fizz")
        else:
            print(i)


fizzbuzz()


