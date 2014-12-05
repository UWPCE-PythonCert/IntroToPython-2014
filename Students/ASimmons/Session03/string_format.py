__author__ = 'Ari'

# "Rewrite the first 3 numbers are: %i, %i, &i"%(1,2,3)
# Want to be able to pass in a sequence of any length
# and display

# to test:


# # idea: use a list, pass it as a tuple (item,)

def print_my_tuple(nums):
    print "the first %d numbers are: %s " % (len(nums), nums,)


## OR use a string

def print_my_string(nums):
    s = str(nums).strip("()")
    print "the first %d numbers are: %s " % (len(nums), s)