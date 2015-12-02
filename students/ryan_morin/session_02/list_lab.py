fruit_list = ['Apples', 'Pears','Oranges','Peaches', 'Pears', 'Pears']


def list_lab(lst):
    print (lst)
    response = input('Name of fruit to include in the list > ')
    lst.append(response)
    print (lst)
    response = input('Enter a number that corresponds to the position of fruit in the list > ')
    print (int(response), lst[int(response) - 1])
    response = input('Name of fruit to include in the list > ')
    lst = [response] + lst
    print (lst)
    response = input('Name of fruit to include in the list > ')
    lst.insert(0,response)
    print (lst)
    temp = []
    for i in lst:
        if i[0] == 'P':
            temp.append(i)
    return (temp)

def part2(lst):
    print (lst)
    lst.remove(lst[-1])
    print (lst)
    response = input('Please provide the name of a fruit to delete >')
    lst.remove(response)
    print (lst)
    temp = []
    response = input('Please provide the name of a fruit to delete >')
    while response not in lst:
        response = input('Please provide the name of a fruit to delete >')
    for i in lst:
        if i !=  response:
            temp.append(i)
    print (temp)

def part3(lst):
    answer = ['yes', 'no']
    for fruit in lst[:]:
        response = input('Do you like {} > '.format((fruit).lower()))
        if response.lower() == 'no':
            lst.remove(fruit)
        while response not in answer:
            response = input('Do you like {} > '.format((fruit).lower()))
            if response.lower() == 'no':
                lst.remove(fruit)
    print (lst)

def part4(lst):
    copy_lst = lst[:]
    temp = []
    for fruit in copy_lst:
        temp.append(fruit[::-1])
    lst.remove(lst[-1])
    print (temp)
    print (lst)
