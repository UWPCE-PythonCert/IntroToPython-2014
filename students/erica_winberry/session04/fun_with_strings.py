# Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)
# for an arbitrary number of numbers...

n = int(input("How many numbers do you want to print? "))
numbers = []
for i in range(1, n+1):
    numbers.append(i)
number = tuple(numbers)
print("The first {:d} numbers are: " + ("{:d}, " * (n)).format(n, (*number)))


def counting(n):
    for i in range(1, n+1):
        return i