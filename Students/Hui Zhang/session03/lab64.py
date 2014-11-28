"""
List Lab# 4
Once more, using the list from series 1:

 Make a copy of the list and reverse the letters in each fruit in the copy.
 Delete the last item of the original list. Display the original list and the copy.
"""

fruit1 = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Mongo', 'Banana']
fruit6 = fruit1
fruit7 = []
for i in range(len(fruit6)):
    fruit7.append(fruit6[i][::-1])
fruit1.pop()
print fruit1
print fruit7
