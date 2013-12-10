#!/usr/bin/env python

"""
Spelling switch/case with a dictionary
"""

"""
A switch/case example:
switch(n) {
  case 0:
    printf("You typed zero.\n");
    break;
  case 1:
  case 9:
    printf("n is a perfect square\n");
    break;
  case 2:
    printf("n is an even number\n");
  case 3:
  case 5:
  case 7:
    printf("n is a prime number\n");
    break;
  case 4:
    printf("n is a perfect square\n");
  case 6:
  case 8:
    printf("n is an even number\n");
    break;
  default:
    printf("Only single-digit numbers are allowed\n");
  break;
}
"""
def zero():
    return "You typed zero.\n"

def sqr():
    return "n is a perfect square\n"

def even():
    return "n is an even number\n"

def prime():
    return "n is a prime number\n"

options = { 0 : zero,
            1 : sqr,
            4 : sqr,
            9 : sqr,
            2 : even,
            3 : prime,
            5 : prime,
            7 : prime,
           }

print options[2]()

print options[4]()

