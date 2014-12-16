string = "Today is October 14"

string[0] string[-1]

string[::2]

string[4:-4:2]

string[::-1]

def slice(string):
    x = len(string)/3
    first = string[0:x-1]
    mid = string[x:x+(x-1)]
    last = string[:]

len(string)/3
##6
mid = string[6:11]
first = string[0:5]
last = string[12:18]
result = mid + last + first
result



## List Lab
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit

## Add fruit to the end 
ask = raw_input("What is another fruit?")
    ## Grapes
ask
fruit.append(ask)
fruit

## Display number corresponding to fruit
ask2 = raw_input("Number: ")
    ##3
ask2
ask2 = int(ask2)
ask2 = ask2 - 1
fruit[ask2]

## Add fruit to the beginning using +
ask3 = raw_input("What is another fruit?")
    ##Mangos
ask3
ask3 = [ask3]
fruit = ask3 + fruit

## Add fruit to the beginning with insert
ask4 = raw_input("What is another fruit?")
    ##Blueberries
fruit

## Display fruits beginning with P
for x in fruit:
    if x[:1] == 'P':
     print x

## Display List
fruit
## Remove the last fruit from the list.
fruit.pop(-1)
print fruit

## Ask the user for a fruit to delete and find it and delete it.
ask5 = raw_input("Delete a fruit: ")
    ##Apples
fruit.remove(ask5)
print fruit
## (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit_copy = fruit[:] *2
##############################
for x in fruit_copy:
    if x(fruit) == fruit
    fruit.remove(x)
##############################

## Ask the user for input displaying a line like “Do you like apples?”
## for each fruit in the list (making the fruit all lowercase).
## For each “no”, delete that fruit from the list.
## For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
ask6 = raw_input("Do you like apples?")

for x in fruit:
    fruit.lower([])
    print fruit

for x in fruit:
    ask6 = raw_input("Do you like apples?")
    if ask6 == 'no':
        fruit.remove(x)

    else ask == 'yes'

    while ask6 != 'no' or 'yes':


##test