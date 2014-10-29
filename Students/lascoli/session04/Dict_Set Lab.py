#Create a dictionary
dict_1 = {}
dict_1={'name':'Chris','city':'Seattle','cake':'Chocolate'}

#Display the dictionary
dict_1

#Delete the entry for “cake”.
dict_1.pop('cake')

#Add an entry for “fruit” with “Mango” and display the dictionary.
dict_1.setdefault('fruit', 'Mango')
#Display the dictionary keys
dict_1.keys()

#Display the dictionary values
dict_1.keys()

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
'cake'in dict_1

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
'Mango'in dict_1.values()

#Using the dict constructor and zip, build a dictionary of numbers 
#from zero to fifteen and the hexadecimal equivalent (string is fine).

def gen_lists():
    
    llist1 =[]
    hlist1 =[]
    n_list =[]
    tmp_lists_dict ={}

    llist1 = range(1,16)
    for i in llist1:
        x = hex(i)
        hlist1.append(x)
        
    n_list = zip(llist1,hlist1)
    #return (n_list)
    tmp_lists_dict = dict(n_list)
    print (tmp_lists_dict)


gen_lists()


#Using the dictionary from item 1: Make a dictionary using the same keys but
#with the number of‘t’s in each value.

dict_1={'name':'Chris','city':'Seattle','cake':'Chocolate'}
dict_2={}
list_1=[]
for a,b in dict_1.items():
   list_1.append((a,b.count('t')))
dict_2 =dict(list_1)
print dict_2


#Create sets set_2, set_3 and set_4 that contain numbers from zero through twenty, divisible 2, 3 and 4.


s_0 = set(range(21))
set_2 = []
set_3 = []
set_4 = []
for i in s_0:
    if i % 2 == 0:
        set_2.append(i)
set_2 = set(set_2)

for i in s_0:
    if i % 3 == 0:
        set_3.append(i)
set_3 = set(set_3)

for i in s_0:
    if i % 4 == 0:
        set_4.append(i)
set_4 = set(set_4)


#Display the sets.
print set_1
print set_2
print set_3
print set_4

#Display if set_3 is a subset of set_2 (False)

set(set_3).issubset(set_2)

#if set_4 is a subset of set_2 (True)
set(set_4).issubset(set_2) 


# Create a set with the letters in ‘Python’ and add ‘i’ to the set.
x = set("Python")
x.add("i")

# Create a frozenset with the letters in ‘marathon’
y = frozenset(“marathon”)

# display the union and intersection of the two sets.
x.union(y)
x.intersection(y)

