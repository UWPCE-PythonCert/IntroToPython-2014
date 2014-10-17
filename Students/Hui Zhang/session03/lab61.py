"""
List Lab# 1
When the script is run, it should accomplish the following four series of actions:

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list.
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""

fruit1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print fruit1
str1 = raw_input("Please input a new fruit name here: ")
fruit1.append(str1)
print fruit1
inp2 = int(raw_input("Please input a number and i can show you the corresponding fruit: "))
print "For number: " + str(inp2) +",the corresponding fruit is: " + fruit1[inp2-1]
fruit2 = ['Banana'] + fruit1
print fruit2
fruit2.insert(0, 'Mongo')
print fruit2
for i in range(len(fruit2)):
    a1 = fruit2[i]
    if a1[0] == 'P':
        print a1
