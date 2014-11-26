__author__ = 'Robert W. Perkins'

#feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#comprehension = [delicacy.capitalize() for delicacy in feast]

#feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

#list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
#comprehension = [ skit * number for number, skit in list_of_tuples ]

#list_of_eggs = ['poached egg', 'fried egg']
#list_of_meats = ['lite spam', 'ham spam', 'fried spam']

dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third': 'ruthless efficiency',
                   'forth': 'fanatical devotion',
                   'fifth': None}

dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}


if __name__ == '__main__':

    #print comprehension[0]
    #print comprehension[2]
    #print len(feast)
    #print len(comprehension)
    #print comprehension[0]
    #print len(comprehension[2])
    #print comprehension
    #comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]
    #print len(comprehension)
    #print comprehension[0]
    #print comprehension

    print 'first' in dict_comprehension
    print 'FIRST' in dict_comprehension
    print len(dict_of_weapons)
    print len(dict_comprehension)
