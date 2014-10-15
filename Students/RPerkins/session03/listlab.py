basket = ["Apples", "Pears", "Oranges", "Paches"]
print basket
new_fruit = raw_input('Type in the name of another fruit')
basket.append(new_fruit)
print basket
fruit_index = raw_input("Type in the fruit index")
print fruit_index +': ' + basket[fruit_index-1]
new_fruit = raw_input("Type in the name of another fruit")
basket = new_fruit + basket
print basket