''' Ian Cote, list lab session 3'''

# Create and display initial list
l = ["Apples", "Pears", "Oranges", "Peaches"]
print(l)


# Since we'll do this a lot...
def new_fruit():
    '''Return string input'''
    return input('Add fruit to list: ')

# Ask user for fruit and add it to end of list.  Display.
l.append(new_fruit())
print(l)

# Ask the user for a number and display the number back to the user and
# the fruit corresponding to that number (on a 1-is-first basis).
r = len(l) + 2   # Get us into the while loop
while not 0 < int(r) < (len(l) + 1):
    # Ensure an integer was given
    try:
        r = int(input('Enter a number from 1 to {} '.format(len(l)) +
                      'to display the item in the list : '))
    except ValueError:
        print('Please enter a number between 1 and {}'.format(len(l)))
    if 0 < int(r) < (len(l) + 1):
        print('{} : {}'.format(l[r - 1], r))
        break

# Add another fruit to the beginning of the list using “+” and display.
l = [new_fruit()] + l
print(l)

# Add another fruit to the beginning of the list using insert() and display.
l.insert(0, new_fruit())
print(l)

# Display all the fruits that begin with “P”, using a for loop.
for i in range(len(l)):
    if l[i][0] == 'P':
        print(l[i])

# Second section
print('\n' + '=' * 80 + '\n')

# display list, remove last item, display
print(l)
del l[len(l) - 1]
print(l)

# Ask the user for a fruit to delete and find it and delete it. (Bonus version)
# Double the list
l += l
print(l)

match = False

while not match:
    a = input('Enter a fruit to remove from the list: ')
    if a in l:
        l = [i for i in l if i != a]
        match = True

print(l)

'''Ask the user for input displaying a line like “Do you like apples?”
for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with
one of those two values (a while loop is good here). Display the list.'''

new = []

for i in range(len(l)):
    a = ''
    while a not in ['yes', 'no']:
        a = input('Do you like {}? [yes/no]: '.format(l[i].lower()))
    if a == 'yes':
        new.append(l[i])

print(new)

l = new

'''Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and
the copy.'''

new2 = []

for i in range(len(l)):
    x = list(l[i])
    x.reverse()
    new2.append(''.join(x))

del l[len(l) - 1]
print(l)
print(new2)
