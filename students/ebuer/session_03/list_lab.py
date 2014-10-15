#@python: 2

listo = ['Apples', 'Pears', 'Oranges', 'Peaches']
print listo

usr_fruit = raw_input("Please add another fruit: ")
listo.append(usr_fruit)
print listo, '\n'

usr_number = raw_input('And now provide a number: ')
list_value = int(usr_number)-1

if list_value < len(listo):
    print 'Value %i is %s\n' %(int(usr_number), listo[list_value])
else:
    print "Sorry, there is no value there.\n"

print 'Let me add something for you, like an Avocado.'
listo = ['Avocado'] + listo
print listo

print 'And now a mango.'
listo.insert(0, 'Mango')
print '%s\n' %listo

for fruit in listo:
    if 'P' in fruit[0]:
        print fruit
