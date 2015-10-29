# list_lab.py

fruit_basket = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_basket)

response = input("Please enter the name of another fruit: ")

fruit_basket.append(response)

print(fruit_basket)

print("There are {0} types of fruit in the fruit basket.\n".format(len(fruit_basket)))
response = input("Please enter a number 1 through {0} to return a type of fruit: ".format(len(fruit_basket)))

print(fruit_basket[int(response)-1])

fruit_basket = fruit_basket + ['Kiwi']
print(fruit_basket)

fruit_basket.insert(0, 'Strawberries')
print(fruit_basket)

print("\nThe following fruits begin with the letter 'p':\n")
for fruit in fruit_basket:
    if fruit[0] == 'p' or fruit[0] =='P':
        print(fruit)
    elif fruit[0] == 'P':
        print(fruit)

print('\nThe contents of the fruit basket are: ', fruit_basket, '\n')

fruit_basket.pop()

print('After pop(), the contents of the fruit basket are: ', fruit_basket, '\n')

response = input("Please enter the name of a fruit to be removed from the basket: ")

fruit_basket.remove(response)

print('After removing {0}, the contents of the fruit basket are: '.format(response), fruit_basket, '\n')

i = 0

while i < len(fruit_basket):
    response = input('Do you like {0}? '.format(fruit_basket[i]))
    if response == 'no' or response == 'No':
        print('removing {0}'.format(fruit_basket[i]), '...')
        fruit_basket.remove(fruit_basket[i])
    elif response == 'Yes' or response == 'yes':
        i = i + 1
    else:
        print('Error! Please respond with yes or no.')


print('The fruit basket now contains: ', fruit_basket)

fruit_copy = fruit_basket

for i in range(len(fruit_copy)):
    print(fruit_copy[i][::-1])


