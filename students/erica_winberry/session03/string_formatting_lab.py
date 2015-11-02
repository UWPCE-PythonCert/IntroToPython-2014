# Write a format string that will take: ( 2, 123.4567, 10000) and produce: 'file_002 :   123.46, 1e+04'

print('file_00{}: {: >.2f}, {:.2e}'.format(2, 123.4567, 10000))

# Rewrite: "the first 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) to take an arbitrary number of values
# Trick: You can pass in a tuple of values to a function with a *

# numbers = (1,2,3)
# print("The first three numbers are {:d}, {:d}, {:d}".format(*numbers))

def format_lab():
    numbers = (1,2,3,4,5,6,7,8,9)
    l = len(numbers)
    print("There are " + str(l) + " numbers in the list.")
    i = int(input("How many of the numbers would you like to print? "))
    if i <= l: 
        result = "\nThe first " + str(i) + " numbers are: " + ("{:d}, " * (i)).format(*numbers)
        print(result.strip(', '))
    else:
        print("\nThere are not that many numbers in the list!")
        result2 = "The numbers in the list are: " + ("{:d}, " * l).format(*numbers)
        print (result2.strip(', '))

format_lab()

