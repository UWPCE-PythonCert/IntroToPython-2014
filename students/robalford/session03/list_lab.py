# Series 1

fruity_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruity_list)

another_fruit = input('Give me a fruit!')

fruity_list.append(another_fruit)

print(fruity_list)

number_fruit = input('Give me a number between one and five!')

print(number_fruit + ' ' + fruity_list[int(number_fruit)-1])

fruity_list = ['Grapefruit'] + fruity_list

print(fruity_list)

fruity_list.insert(0, 'Pomegranate')

print(fruity_list)

for fruit in fruity_list:
    if fruit[0].lower() == 'p':
        print(fruit)

# Series 2

print(fruity_list)

fruity_list.pop()

print(fruity_list)

fruit_gone = input('Give me a fruit to lose!')

fruity_list.remove(fruit_gone)

print(fruity_list)

double_fruity_list = fruity_list * 2

# refactor to make this more pythonic?
while fruit_gone not in double_fruity_list:
    fruit_gone = input('Give me a fruit to lose!')
    for fruit in double_fruity_list[:]:
        if fruit == fruit_gone:
            double_fruity_list.remove(fruit_gone)
    break

print(double_fruity_list)

# series 3

# iterate over a copy in order to preserve the original length
# as items are removed
for fruit in fruity_list[:]:
    fruit_preference = input('Do you like {}?'.format(fruit.lower()))
    fruit_preference = fruit_preference.lower()
    while fruit_preference != 'yes' and fruit_preference != 'no':
        fruit_preference = input('Yes or no')
        fruit_preference = fruit_preference = fruit_preference.lower()
        break
    if fruit_preference == 'no':
        fruity_list.remove(fruit)

print(fruity_list)

# series 4

# Check to make sure the user didnt erase the whole list in the last
# series and reset the list to original value if they did.
if not fruity_list:
    fruity_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

fruity_copy = fruity_list[:]

for fruit in fruity_copy[:]:
    backwards_fruit = fruit[::-1]
    fruity_copy.remove(fruit)
    fruity_copy.append(backwards_fruit)

fruity_list.pop()

print(fruity_list, fruity_copy)
