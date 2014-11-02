def count_evens(nums):
  return len([n for n in nums if n%2 == 0])


print count_evens([2, 1, 2, 3, 4]) # 3
print count_evens([2, 2, 0]) # 3
print count_evens([1, 3, 5]) # 0