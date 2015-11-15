'''
Write a function that returns a list of n functions, such that 
each one, when called, will return the input value, incremented by 
an increasing number.

Use a for loop, lambda, and a keyword argument
'''


def function_builder(input_value):
        l = []
        [l.append(lambda input_value, e=i: input_value + e) for i in range(input_value)]
        return l
        # for i in range(input_value):
        #     l.append(input_value  + i)

# for f in function_builder(5):
#     print(f(5))