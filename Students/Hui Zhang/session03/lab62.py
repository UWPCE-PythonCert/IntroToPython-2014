"""
List Lab# 2
Using the list created in previous List Lab# 1:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete and find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

"""
fruit2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print fruit2.pop()
fruit3 = 2*fruit2
print fruit3
str2 = raw_input("Please input a fruit name here to be removed: ")
fruit4 = []
for i in range(len(fruit3)):
    if fruit3[i] != str2:
        fruit4.append(fruit3[i])
print fruit4