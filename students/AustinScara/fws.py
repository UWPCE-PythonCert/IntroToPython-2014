
import random

lst = []
while len(lst) < 40:
	lst.append(random.randint(0,45))

# lst = [randint(0,45) for ]
# print (lst)

print ("the first 3 numbers are: {:d}, {:d}, {:d}".format(lst[0], lst[1] ,lst[2]))