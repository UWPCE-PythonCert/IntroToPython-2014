#!/usr/bin/python

#Monkey Trouble

#x = raw_input("Please enter a boolean value: ").title()
#y = raw_input("Please enter another boolean value: ").title()

x = "True"
y = "False"

def monkey_trouble(a_smile, b_smile):
    if a_smile == 'True' and b_smile == 'True':
        
        return True

    elif a_smile == 'False' and b_smile == 'True':

        return False

    elif a_smile == 'True' and b_smile == 'False':

        return False

    elif a_smile == 'False' and b_smile == 'False':

        return True

    else:

        return True

print "Are we in trouble? " 

print monkey_trouble(x,y)




