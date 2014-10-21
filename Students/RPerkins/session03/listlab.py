
#action #1
basket = ["Apples", "Pears", "Oranges", "Peaches"]
print basket
new_fruit = raw_input('Type in the name of another fruit-->')
fruit = str(new_fruit)
basket.append(fruit)
print basket
fruit_index = raw_input("Type in the fruit index-->")
index = int(fruit_index)
print fruit_index + ': ' + basket[index-1]
new_fruit = raw_input("Type in the name of another fruit-->")
fruit = str(new_fruit)
basket = [fruit] + basket
print basket
new_fruit = raw_input("Type in the name of another fruit-->")
fruit = str(new_fruit)
basket.insert(0, fruit)
print basket
for i in range(len(basket)):
    if basket[i][0] == "P":
        print basket[i]

#action 2
print basket
basket.pop()
print basket
del_fruit = raw_input("Pick a fruit from the list to delete-->")
fruit = str(del_fruit)
if fruit in basket:
    for i in range(len(basket)-1):
        if basket[i] == fruit:
            basket.pop(i)
else:
    print 'That fruit is not in the basket'

#action 3
deletes = 0
for i in range(len(basket)):
    i = i - deletes
    lfruit = None
    while not (lfruit == "yes" or lfruit == "no"):
        like_fruit = raw_input("Do you like %s-->" % basket[i].lower())
        lfruit = str(like_fruit)
    if lfruit == 'no':
        basket.pop(i)
        deletes += 1
print basket

#action 4
rlist = basket
for i in range(len(basket)):
    rlist[i] = rlist[i][::-1]
basket.pop()
print basket
print rlist