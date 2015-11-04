#Series 1
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
list = ['Apples', 'Pears', 'Oranges', 'Peaches']
#Display the list
print (list)
#Ask the user for another fruit 
newFruit = input ("please input a fruit name: ")
#add it to the end of the list.
list = ['Apples', 'Pears', 'Oranges', 'Peaches', newFruit]
#Display the list
print (list)
#Ask the user for a number 
number = int(input ("please select a number from 1-5: "))
#display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
print(list[number-1])
#Add another fruit to the beginning of the list using “+”
newList  = ['Strawberries'] + list
#display the list.
print (newList)
#Add another fruit to the beginning of the list using insert()
newList.insert (0, 'Pomegranates')
#display the list
print (newList)
#Display all the fruits that begin with “P”, using a for loop
print ([fruit for fruit in newList if (fruit[0] is 'P')])

#Series 2
#display the list
print (newList)
#Remove the last fruit from the list
newList.remove(newFruit)
#Display the list
print (newList)
#Ask the user for a fruit to delete
deleteFruit = input ("please select a fruit you would like to remove from the list: ")
# find it and delete it.
newList.remove(deleteFruit)
#Display the list
print (newList)

#Series 3
#Ask the user for input displaying a line like “Do you like apples?”
for fruit in newList:
    likeOrNot = input("Do you like %s ?" %fruit)
#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values 
    while (likeOrNot.strip() != 'yes') and (likeOrNot.strip() != 'no'):
        likeOrNot = input("Please respond with 'yes' or ,no':" )
    # for each “no”, delete that fruit from the list.
    if likeOrNot == "no":
        newList.remove(fruit)
# for each fruit in the list (making the fruit all lowercase)
# Display the list
print ([x.lower() for x in newList])

#Series 4
newList = ['Pomegranates', 'Strawberries', 'Apples', 'Pears', 'Oranges', 'Peaches']
#Make a copy of the list
import copy
copiedList = copy.copy(newList)
# reverse the letters in each fruit in the copy
fruit1 = [ ]
for fruit in copiedList:
    #fruit[ ::-1]
    fruit1.append(fruit[ ::-1])
print(fruit1)

#Delete the last item of the original list
newList.pop()
#Display the original list and the copy
print(newList + fruit1)


