"""
List Lab# 3
using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?”
 for each fruit in the list (making the fruit all lowercase).
 For each “no”, delete that fruit from the list.
 For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
 Display the list.
"""

fruit1 = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Mongo', 'Banana']
fruit5 = []
for i in range(len(fruit1)):
    input1 = raw_input("Do you like:" + fruit1[i].lower() + " (yes/no) ?")
    while (input1 != 'yes') and (input1 != 'no'):
        print "please answer yes or no"
        input1 = raw_input("Do you like:" + fruit1[i].lower() + " (yes/no) ?")
    if input1 == 'yes':
        fruit5.append(fruit1[i])
    # if input1 == 'no':
        # continue
for i in range(len(fruit5)):
    fruit5[i] = fruit5[i].lower()
print fruit5
