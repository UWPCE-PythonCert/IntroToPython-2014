print ' '
print '# Create a list that contains Apples, Pears, Oranges and Peaches and display the list.'
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print fruits
print ' '

print '# Ask the user for another fruit and add it to the end of the list and print the list.'
fruit1 = raw_input('Enter another fruit: ')
fruits.append(fruit1)
print fruits
print ' '

print '# Ask the user for a number and display the number back to the user and the fruit'
print 'corresponding to that number (on a 1-is-first basis).'
i = int(raw_input('Enter a number between 1 and 5: '))
print i, fruits[i-1]
print ' '

print '# Add another fruit to hte beginning of the list using "+" and display the list.'
fruits = ['Bananas'] + fruits
print fruits
print ' '

print '# Add another fruit to the beginning of the list using insert() and display the list.'
fruits.insert(0,'Grapes')
print fruits
print ' '

print '# Display all the fruits that begin with "P", using a for loop.'
for fruit in fruits:
    if fruit[0] == 'P':
        print fruit

print ' '
print '# Display the list.'
print fruits
print ' '

print '# Remove the last fruit from the list and display the list.'
fruits.pop()
print fruits
print ' '

print '# Double the list.'
print '# Ask the user for a fruit to  delete and find it and delete it.'
print '# Keep asking until they enter a fruit that is in the list.'
print '# Remove all occurrences of the fruit and display the list.'
fruits *= 2
x = raw_input('Please enter a fruit to delete: ')
while x not in fruits:
    x = raw_input('That fruit is not in the list. Please try again: ')
while x in fruits:
    fruits.remove(x)
print fruits
print ' '


print '# Ask the user for input displaying a line like Do you like apples?'
print '# for each fruit in the list (making the fruit all lowercase).'
print '# For each no, delete that fruit from the list.'
print '# For any answer that is not yes or no, prompt the user to answer with one of those two values (a while loop is good here):'
print '# Display the list.'
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
for fruit in fruits[:]:
    x = raw_input('Do you like ' + fruit.lower() + '?')
    while x not in ['yes', 'no']:
        x = raw_input('Please answer yes or no. Do you like ' + fruit.lower() + '?')
    if x == 'no':
        fruits.remove(fruit)
print fruits
print ''


print '# Once more, using the list from series 1:'
print '# Make a copy of the list and reverse the letters in each fruit in the copy.'
print '# Delete the last item of the original list. Display the original list and the copy.'
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruits = fruits[:]
for i, fruit in enumerate(new_fruits):
    new_fruits[i] = fruit[::-1]
fruits.pop()
print 'Original', fruits
print 'Copy', new_fruits

