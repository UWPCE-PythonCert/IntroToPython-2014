# These functions are not tested by a test script.

def comp1():
    feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

    comprehension = [delicacy.capitalize() for delicacy in feast]
    print comprehension
    print comprehension[0]
    print comprehension[2]

def comp2():
    feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
    comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]
    print comprehension

    print len(feast)
    print len(comprehension)


def comp3():
    list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
    comprehension = [ skit * number for number, skit in list_of_tuples ]
    print comprehension

