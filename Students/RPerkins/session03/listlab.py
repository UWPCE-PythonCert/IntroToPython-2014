basket = ["Apples", "Pears", "Oranges", "Peaches"]
print basket
new_fruit = raw_input('Type in the name of another fruit-->')
fruit = str(new_fruit)
basket.append(fruit)
print basket
fruit_index = raw_input("Type in the fruit index-->")
index = int(fruit_index)
print fruit_index + ': ' + basket[index-1]
new_fruit = raw_input("Type in the name of another fruit-->")
fruit = str(new_fruit)
basket = [fruit] + basket
print basket
new_fruit = raw_input("Type in the name of another fruit-->")
fruit = str(new_fruit)
basket.insert(0, fruit)
print basket
for i in range(len(basket)):
    if basket[i][0] == "P":
        print basket[i]
print basket
basket.pop()
print basket