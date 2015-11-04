dictone = {'name': 'chris', 'city':'seattle', 'cake':'chocolate'}
print("The dictionary is =", dictone)

# delete the entry cake
dictone.pop('cake')
print("The dictionary is =", dictone)

# add an entry for fruit and mango
dictone.update({'fruit': 'mango'})
print("The dictionary is =", dictone)

# print keys and items
print("Keys =",dictone.keys())
print("Keys =",dictone.items())

# display if mango and cake are in dictionary
print("Mango in dictionary = ", 'mango' in dictone)
for key in dictone:
    if key == 'cake':
        print("cake found")
    # end if
# end for

dicttwo = {}
for k,v in dictone.items():
    print(k,v)
    count = 0
    for char in v:
        if char == 't':
            count += 1
        # end if
        dicttwo.update({k:count})
    # end for
    print("The new dictionary with t count =", dicttwo)
# end for

# Set portion of lab here.
s = set([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("Here is the set we built.", s)

# build sets s2, s3, s4
s2 = set()
s3 = set()
s4 = set()

for item in s:
    if (item % 2)== 0:
        s2.add(item)
    # end if
    if (item % 3) == 0:
        s3.add(item)
    # end if
    if (item % 4) == 0:
        s4.add(item)
    # end if

print("Set divisible by 2 =", s2)
print("Set divisible by 3 =", s3)
print("Set divisible by 4 =", s4)

# execute the is subset tests
if s2.issubset(s3) == True:
    print("S2 is a subset of S3")
else:
    print ("S2 is not a subset of s3")
# end if

# execute the is subset tests
if s4.issubset(s2) == True:
    print("S4 is a subset of S2")
else:
    print ("S4 is not a subset of s2")
# end if

# Create a set with letters in python
pyset = set(['P','y','t','h','o','n'])
pyset.add('i')
marithonset = (('M','a','r','i','t','h','o','n'))
print("The union of pyset and marithonset is =",(pyset.union(marithonset)))
print("The interset of pyset and marithonset is =",(pyset.intersection(marithonset)))
