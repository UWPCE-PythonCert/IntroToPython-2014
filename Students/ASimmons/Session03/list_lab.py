__author__ = 'Ari'

import re

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

print fruit

while True:
    new_fruit = raw_input("Enter a fruit: ")

    fruit.append(str(new_fruit))

    print fruit

    new_fruit = len(fruit)

    for (i,item) in enumerate(fruit, start=1):
        print(str(i) + ": " + str(item))

    gimme_a_number = int(raw_input("Gimme a number (as an integer) that is < or = to " + str(new_fruit) + " : "))

    if gimme_a_number > new_fruit:
        print "Your number is greater then the length of the list"
    else:
        print (str(gimme_a_number) + " : " + str(fruit[gimme_a_number - 1]))

    front_of_line_fruit = raw_input("Enter another fruit to add to front of the line: ")

    fruit.insert(0,front_of_line_fruit)

    print fruit

    another_front_of_line_fruit = raw_input("Enter YET ANOTHER fruit to add to front of the line: ")

    fruit.insert(0,another_front_of_line_fruit)

    print fruit

##Problems finding p:

    pattern = re.compile("p\w+", re.IGNORECASE)



    sub_list = filter(pattern.match, fruit)


    print "These items start with a P : " + str(sub_list)



    ## Tests against the list created by the above steps


## Delete an item from beginning of list

    del fruit[0]

    print fruit

