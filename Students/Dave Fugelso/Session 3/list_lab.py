'''


List Lab (after http://www.upriss.org.uk/python/session5.html)

In your student folder, create a new file called list_lab.py.

The file should be an executable python script. That is to say that one should be able to run the script directly like so:

$ ./list_lab.py
Add the file to your clone of the repository and commit changes frequently while working on the following tasks. When you are done, push your 
changes to GitHub and issue a pull request.

(if you are struggling with git -- just write the code for now)

When the script is run, it should accomplish the following four series of actions:

Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
Display the list.
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
Add another fruit to the beginning of the list using "+" and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with "P", using a for loop.
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete and find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
Again, using the list from series 1:

Ask the user for input displaying a line like "Do you like apples?"
for each fruit in the list (making the fruit all lowercase).
For each "no", delete that fruit from the list.
For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here):
Display the list.
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.

Delete the last item of the original list. Display the original list and the copy.

'''

#Windows development platform: 

if __name__ == "__main__":
    #Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    #Display the list.
    print fruits
 
    '''
    #Ask the user for another fruit and add it to the end of the list.
    newFruit = raw_input ('Enter a new fruit to add to the list: ')
    fruits.append(newFruit)
    #Display the list.
    print fruits
    
    #Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
    validIndex = False
    while not validIndex:
        fruitIndex = raw_input ('Enter an index for a fruit: ')
        try:
            index = int(fruitIndex)
            if index >= 0 and index < len(fruits):
                validIndex = True
        except:
            print 'Invalid input. Enter number between zero and ', len (fruits)
    print index, fruits[index]
    '''    
    #Add another fruit to the beginning of the list using "+" and display the list.
    fruits = ['Kiwi'] + fruits
    print fruits

    #Add another fruit to the beginning of the list using insert() and display the list.
    fruits.insert (0, 'Pomegranates')
    print fruits

    #Display all the fruits that begin with "P", using a for loop.
    for fruit in fruits:
        if fruit[0].upper() == 'P':
            print fruit,
    print
    
    
    #Using the list created in series 1 above:
    #
    #Display the list.
    print fruits
    #Remove the last fruit from the list.
    #Display the list.
    fruits.pop()
    print fruits
    
    #Ask the user for a fruit to delete and find it and delete it.
    #(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    '''
    success = False
    fruits = fruits*2
    print fruits
    while not success:
        remove = raw_input ('Enter a fruit to delete from the list: ')
        if remove in fruits:
            success = True
            while remove in fruits:
                fruits.remove (remove)
        else:
            print "That's not in the list. Choose one of these: ", fruits
             
    print fruits       
        
    
    
    #Again, using the list from series 1:
    #
    #Ask the user for input displaying a line like "Do you like apples?"
    #for each fruit in the list (making the fruit all lowercase).
    #For each "no", delete that fruit from the list.
    #For any answer that is not "yes" or "no", prompt the user to answer with one of those two values (a while loop is good here):
    #Display the list.
    fruitListForIteration = fruits
    likeList = []
    for fruit in fruitListForIteration:
        if fruit in fruits:
            if fruit not in likeList:
                haveAnswer = False
                while not haveAnswer:
                    remove = raw_input ('Do you like '+fruit+'?')
                    if remove.upper() == 'NO':
                        haveAnswer = True
                        while fruit in fruits:
                            fruits.remove(fruit)
                    elif remove.upper() == 'YES':
                        likeList.append(fruit)
                        haveAnswer = True
                    else:
                        print 'What kind of reply is that?'
    print fruits       
    '''
                
    
    
    #Once more, using the list from series 1:
    #
    #Make a copy of the list and reverse the letters in each fruit in the copy.
    #
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches', 'Kiwi', 'Grapes']
    fruitsCopy = fruits
    for i in range (0,len(fruitsCopy)):
        fruit = fruitsCopy[i]
        fruitsCopy[i] = fruit[::-1]
    print fruits
    print fruitsCopy
    
    

    #Delete the last item of the original list. Display the original list and the copy. 
    fruits.pop()
    print fruits
    print fruitsCopy
