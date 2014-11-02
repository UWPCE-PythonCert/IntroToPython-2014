# 1. Print the dict by passing it to a string format method, so that you get something like:
food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

desc = '{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.'

def print_sentence(arr, desc):
	print desc.format(**arr)
	return

# 2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).


# def hex_list(high,low=0):
# 	store = {} 
# 	return [store[r] = hex(r) for r in range(low,high+1]

# hex_list(15)
# print

# 3. Do the previous entirely with a dict comprehension - should be a one - liner
def hex_dict(high,low=0):
	return {r:hex(r) for r in range(low,high+1)}





# 4. Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 'a's in each value. You can do this either by editing 
# the dict in place, or making a new one. If you edit in place, make a copy first!


def count_a(orig_dict):
	return {k:v.count('a') for k,v in orig_dict.iteritems()}


# 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
# divisible 2, 3 and 4.

def divisible_set(denom,high,low=0):
	return {n for n in range(low,high+1) if n%denom == 0}


if __name__ == '__main__':
	print_sentence(food_prefs,desc)
	print
	
	print hex_dict(15)
	print

	print count_a(food_prefs)
	print

	for i in [2,3,4]:
		print divisible_set(i,20)
	print
	





