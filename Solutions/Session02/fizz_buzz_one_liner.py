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

# second, take the for loop off one line -- that really makes no difference:

for i in range(1, 101):
    print([i, 'Fizz', 'Buzz', 'FizzBuzz'][(i % 3 == 0) + 2 * (i % 5 == 0)])

# so we are looping through the numbers, and the contents of the print()
# is decidding what to print for i

# unpack that line:

for i in range(1, 101):
    options_to_print = [i, 'Fizz', 'Buzz', 'FizzBuzz']
    index = 0  # default index is zero
    index += (i % 3 == 0)  # add one to index if it's a multiple of 3
    index += (2 * (i % 5 == 0))  # add two to the index if a multiple of 5
    print(options_to_print[index])  # print the selection.

# there are 4 possible options that might get printed on each line:
# 1) the number, i
# 2) Fizz
# 3) Buzz
# 4) FizzBuzz

# we now need an index to pick which of these to print
#
# remember that True and False are also the integers 1 and 0:
# so (i % 3 == 0) will return 1 (True) if i is a multiple of 3
# and 0 (False) if not
# and (i % 5 == 0) will do the same for 5
# so (2 * (i % 5 == 0)) will return either 0 or 2
#
# so if the number is a multiple of neither, index will be zero,
# and we'll get the zeroth element of the list: i
#
# if i is a multiple of three (i % 3 == 0), then the index will be 1
#
# and if i is a multiple of 5 the index will then be 3 (1+2)
# if it wasn't a multiple of three, then it will be 2 (0+2)
#
# so using the index will get the right element from the options list.
#
# pretty slick!
