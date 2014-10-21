#@python: 2

#part 1 of list lab
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

print '\nAnd now a mango.'
listo.insert(0, 'Mango')
print '%s\n' %listo

print 'Can I share all the "P" fruits with you?'
for fruit in listo:
    if 'P' in fruit[0]:
        print fruit

#part 2 of list lab
print "\nI'm still excited about our fruit list:"
for fruit in listo:
    print fruit

print "\nBut I don't care for %s" %listo[-1]
del listo[-1]
print listo

##copy list since we did bonus scripting and don't want something too long
p3_list = listo 
p4_list = listo


usr_rm = raw_input("Is there anything you don't care for? ")
print "I can remove %s" %(usr_rm)

#bonus scripting
spincycle = False
while not spincycle:
    if usr_rm in listo:
        n = listo.count(usr_rm)
        for m in range(n):  #need this since .remove only does 1 instance
            listo.remove(usr_rm)
        print '\nGreat, consider it gone.\n%s\n' %listo
        spincycle = True
    else:
        print "\nSorry, I checked but %s isn't in our list.  I checked twice." %usr_rm
        listo = listo * 2
        listo.sort()
        print '\n%s' %listo
        usr_rm = raw_input("\nPlease check the list and let me remove something else. ")

#part 3
print "I think we got off on the wrong foot, let's go back to an earlier list."
for fruit in p3_list:
    usr_fruit = raw_input('Do you like %s? '%fruit.lower())
    spincycle = False
    while not spincycle:
        if usr_fruit == 'no':
            p3_list.remove(fruit)
            spincycle = True
        elif usr_fruit == 'yes':
            spincycle = True
        else:
            print "A yes or no will do, thanks."
            usr_fruit = raw_input('Do you like %s? ' %fruit.lower())

print "Here's your modified final list: %s" %p3_list

#part 4
backward_fruit=[]
for fruit in p4_list:
    backward_fruit.append(fruit[::-1])

del p4_list[-1]

print "Original List: %s" %p4_list
print "Backwards List: %s" %backward_fruit
