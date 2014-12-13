#!/usr/bin/python


def sum_generator(number_range):

    counter = list(range(number_range))

    new_value = 0
    i = new_value

    while i < number_range:

	try:
	
	    item = counter.pop(0)+counter.pop(0)
	    yield item
	    counter.insert(0,item)

	except IndexError:

	    break


sum_gen = sum_generator(10)
print next(sum_gen)
print next(sum_gen)
print next(sum_gen)
print next(sum_gen)
print next(sum_gen)
print next(sum_gen)

def doubler(number_range):
    i = 0
    while i<number_range:
	if i < 1:
	    i = i+1
	    yield i
	    
	else:

	    yield i*2
	    i = i*2 
	
def fibonacci(number_range):
    """Returns n numbers in the Fibonnacci sequence"""

    a, b = 0, 1
    for i in range(number_range):
        a, b = b, a + b
	yield a
	    



fibo = fibonacci(10)
print next(fibo)
print next(fibo)
print next(fibo)
print next(fibo)
print next(fibo)
print next(fibo)
print next(fibo)
print next(fibo)

counter = doubler(32)

print next(counter)
print next(counter)
print next(counter)
print next(counter)
print next(counter)
print next(counter)


