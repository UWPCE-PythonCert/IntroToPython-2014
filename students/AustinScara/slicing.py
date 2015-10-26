# return a sequence with the first and last items exchanged.
def swapFirstLast(string):
	first = string[0]
	last = string[-1]
	mid = string[1:-1] 

	return last + mid + first



# return a sequence with every other item removed
def dropEveryOther(string):
	return string[::2]




# return a sequence with the first and last 4 items removed, and every other item in between
def dropFLfourWeveryother(string):
	return string[4:-4:2]



# return a sequence reversed (just with slicing)
def revSli(string):
	return [::-1]


# return a sequence with the middle third, then last third, then the first third in the new order
def thirds(string):
	return string[]