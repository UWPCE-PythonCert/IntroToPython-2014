fruity_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruity_list)

another_fruit = input('Give me a fruit!')

fruity_list.append(another_fruit)

print(fruity_list)

number_fruit = input('Give me a number between one and five!')

print(number_fruit + fruity_list[int(number_fruit)-1])

fruity_list = ['Grapefruit'] + fruity_list

print(fruity_list)

fruity_list.insert(0, 'Pomegranate')

print(fruity_list)

for fruit in fruity_list:
    if fruit[0] == 'P':
        print(fruit)
