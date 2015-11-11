# When the script is run, it should accomplish the following four series of actions:

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list.
# Display all the fruits that begin with “P”, using a for loop.

def fruits():
    fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    print_list(fruit_list)
    append_list(fruit_list)
    print_list(fruit_list)
    get_index(fruit_list)
    new = adding_items(fruit_list)
    first_letter_search(new)

def print_list(l):
    # Display the list.
    print("The complete list is: " + str(l))

def append_list(l):
    # Ask the user for another fruit and add it to the end of the list.
    new_item = input("What would you like to add to the list? ")
    l.append(new_item)

def get_index(l):
    # Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
    v = len(l)
    i = int(input("Pick a number: "))
    assert isinstance (i, int), "An integer was not entered."
    print(l[i] + " is item number " + str(i) + " in the list.")

def adding_items(l):
    # Add another fruit to the beginning of the list using “+” and display the list.
    new = [input("What would you like to add to the list? ")]
    new += l
    print_list(new)
    # Add another fruit to the beginning of the list using insert() and display the list.
    i = input("What else would you like to add to the list? ")
    new.insert(0, i)
    print_list(new)
    return new

def first_letter_search(l):
    print('The items that begin with "P" are:')
    for i in l:
        if "P" is i[0].upper:
            print(i)
        else:
            pass

fruits()
