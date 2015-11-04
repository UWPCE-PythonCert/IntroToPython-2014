#List-lab homework for Intro to Python 2015

""" 
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
def froots():
    #   Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches” and display the list.
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

    print("Our initial fruits are: " , fruits)

    print('\n')
    #    Ask the user for another fruit and add it to the end of the list and display the list.
    moar_fruits = input("This diet is terrible.  Add more fruits: ")

    fruits.append(moar_fruits)

    print('\n')
    #    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
    fruit_num = input("We need to number some fruit.  Enter a number to bring up the fruit in the corresponding location: ")

    for foo in fruits[0:int(fruit_num)]:
        print("Your number " + fruit_num + "brought up " + fruits[int(fruit_num)])
        break

    print('\n')
    #   Add another fruit to the beginning of the list using “+” and display the list.
    print("Now we need to add some banana")    
    fruits = ['banana'] + fruits
    print(fruits)

    print('\n')
    #    Add another fruit to the beginning of the list using insert() and display the list.
    print("Nope.  More fruits.")    
    fruits.insert(0, 'Devil Fruit')
    print(fruits)

    print('\n')
    #   Display all the fruits that begin with “P”, using a for loop.
    print("Now we have to find only the fruits with P.")
    for items in fruits:
        if items.startswith('p') or items.startswith('P'):
            print(items)
            #break
        

froots()
            




    
