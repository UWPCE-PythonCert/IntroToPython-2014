#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
#Display the list.
fruit1 = ['Apples','Pears','Oranges','Peaches']
print fruit1 ,'\n'

#Ask the user for another fruit and add it to the end of the list.
#Display the list.
new1 = raw_input("Please add a new fruit to the list:\n") 
fruit1.append(new1)
print fruit1 ,'\n'

#Ask the user for a number and display the number back to the user and
#the fruit corresponding to that number (on a 1-is-first basis).
#Display the list.
new2 = int(raw_input("Please choose a number from the list of fruit:\n"))
print fruit1[new2] ,'\n'

#Add another fruit to the beginning of the list using “+” and display the list.
new3 = raw_input("Please add a new fruit to the list:\n")
fruit2  = [new3]
fruit3 = fruit2 + fruit1
print fruit3 ,'\n'

#Add another fruit to the beginning of the list using insert() and display the list.
new4 = raw_input("Please add a new fruit to the list:\n")
fruit3.insert(0, new4)
print fruit3 ,'\n'

##Display all the fruits that begin with “P”, using a for loop.
print ("All the fruits that begin with P:\n")
for i in fruit3:
   if i[0] == 'P':
       print i + '\n'
#Using the list(fruit3) created in series 1 :


#Remove the last fruit from the list.Display the list.
fruit4 = fruit3
print ("Removing the last fruit from the list:\n")
fruit4.remove(fruit4[-1])
print fruit4

#Ask the user for a fruit to delete and find it and delete it.Display the list.
new4 = raw_input("Please choose a fruit from the list to delete:\n")
for i in fruit4:
    if i == new4:
        fruit4.remove(i)
print fruit4 ,'\n'

#Ask the user for input displaying a line like “Do you like apples?”
#For each fruit in the list (making the fruit all lowercase).
#For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
#Display the list.

#Remove extra copy
fruit5 = fruit3
for i in fruit5[:]:
    i =i.lower()
    

    
    while True:
        new4 = raw_input('Do you like ' + i +' ? Please answer with a Yes or No\n' )
        
        if new4 == 'Yes'or new4 == 'No':
            break
    if new4 == 'Yes':
        continue
             
    else:
        i = i[0].upper() +i[1::]
        fruit5.remove(i)        
        
print fruit5,'\n'

#Make a copy of the list and reverse the letters in each fruit in the copy.
#Delete the last item of the original list. Display the original list and the copy.


oring_fruit = fruit3[:] 
copy_fruit = fruit3[:]
  
for i in range(len(copy_fruit)):
    fruit6_reverse = [] 
    fruit6 = copy_fruit.pop(i) 
    fruit6_reverse.extend(fruit6) 
    fruit6_reverse.reverse() 
    fruit6 = "".join(fruit6_reverse) 
    copy_fruit.insert(i, fruit6) 
oring_fruit.remove(oring_fruit[-1])

print "Original List of Fruit: %s" % oring_fruit 
print "Copied List of Fruit: %s" % copy_fruit                     

