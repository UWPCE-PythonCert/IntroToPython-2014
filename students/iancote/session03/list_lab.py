l = ["Apples", "Pears", "Oranges", "Peaches"]
print(l)
response = input('Add fruit to list: ')
l.append(response)
print(l)
response = input('Enter a number from 1 to {} to display the item on \
    list: '.format(len(l)))
if int(response)  
