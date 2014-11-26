__author__ = 'asimmons'

#Using a list comprehension, return the number of even ints in the given array.

def count_evens(nums):
   #one_line_comprehension_here
   even = len([n for n in nums if n % 2 == 0])
   return even