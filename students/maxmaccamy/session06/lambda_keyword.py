__author__ = 'Max'

def function_builder(numfunctions):
    return [lambda x, e=i: x + e for i in range(numfunctions)]