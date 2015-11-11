#feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#comprehension = [delicacy.capitalize() for delicacy in feast]

#print(comprehension[0]) #lambs
#print(comprehension[2]) #orangutangs


#feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
#comp = [delicacy for delicacy in feast if len(delicacy) > 6]

#print(len(feast)) #5
#print(len(comp)) #3


#list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
#comprehension = [ skit * number for number, skit in list_of_tuples]

#print(comprehension[0]) # one lumberjack
#print(len(comprehension[2])) #16 -number of chars not multiples of spam, its a string duh!


#eggs = ['poached egg', 'fried egg']
#meats = ['lite spam', 'ham spam', 'fried spam']
#comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

#print(len(comprehension)) #6
#print(comprehension[0]) #poached egg and lite spam


#comprehension = {x for x in 'aabbbcccc'}

#print(comprehension) #aaabababacacacac? nope - a, b, c its a set so no dups and not ordered


#dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency',
#                   'forth':'fanatical devotion', 'fifth': None}
#dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}


#print('first' in dict_comprehension) #fear? False  the comp puts the keys in caps -this doesn't exist as a key
#print('FIRST' in dict_comprehension) #True                                        -this does!
#print(len(dict_of_weapons)) #5
#print(len(dict_comprehension)) #4


def count_evens(nums):
    return len([x for x in nums if x % 2 == 0])

print(count_evens([2, 4, 6, 7, 8, 9, 10])) #5
print(count_evens(range(30))) #15
