#!/usr/bin/python

# rfj
## Fizz Buzz Exercise
## http://uwpce-pythoncert.github.io/IntroToPython/exercises/fizz_buzz.html
## completed 2015-10-15

## print 1-100 inclusive, but if divisible by 3 print "Fizz", 
## if divisible by 5 prting "Buzz", and if divisible by both 
## print "FizzBuzz"


def fb():
    x = 0
    while x < 100:
        x += 1
        if x % 3 == 0:
            if x % 5 == 0:
                print("FizzBuzz")
            else: 
                print("Fizz")
        if x % 5 == 0:
            print("Buzz")
        else:
            print(x)

fb() 
