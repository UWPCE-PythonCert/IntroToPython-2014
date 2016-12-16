#!/usr/bin/env python3

# This One Liner solution to the Fizz Buzz problem
# was found by a student on the internet

for i in range(1,101): print([i,'Fizz','Buzz','FizzBuzz'][(i%3==0)+2*(i%5==0)])

# this is a good example of why the most compact code is not always the
# best -- readability counts!
# And this is pretty impenatrable.
# butit's also pretty nifty logic, so below,
# It's unpacked to make it easeir to understand.

# first , add some white space to make it pep8 compatible, and more readable.

for i in range(1, 101): print([i, 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + 2 * (i % 5 == 0)])


# first, take the for loop off one line -- that really makes no difference:


