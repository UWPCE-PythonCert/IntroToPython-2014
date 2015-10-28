#!/usr/bin/env python 3



def FizzBuzz():
    for i in range(1, 101):
        if ((i % 3) + (i % 5)) == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == "__main__":
    FizzBuzz()