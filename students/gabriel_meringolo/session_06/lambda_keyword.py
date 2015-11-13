# Write a function that returns a list of n functions,
# such that each one, when called, will return the input
# value, incremented by an increasing number.
# Use a for loop, lambda, and a keyword argument


def function_builder(func_amount, l=None):
    if l is None:
        l = []
    for index in range(func_amount):
        l.append(lambda x, e=index: x + e)
    return l


lamb_list = function_builder(4)
print(lamb_list[1](3))