#When the script is run, it should accomplish the following four series of actions:

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
dic = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate"}

#Display the dictionary.
print(dic)

#Delete the entry for “cake”.
del dic["cake"]

##Display the dictionary.
print(dic)

#Add an entry for “fruit” with “Mango” and display the dictionary.
dic["fruit"] = "Mango"

#Display the dictionary keys.
print(dic.keys())

#Display the dictionary values.
print(dic.values())

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("cake" in dic)

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in dic)

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
t_dict = dict(dic)
for i,j in dic.items():
        t_dict[i] = j.count("t")
print(t_dict)



#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = set()
s3 = set()
s4 = set()
for i in range(1,21):
    if i % 2 == 0:
        s2.update([i])
    if i % 3 == 0:
        s3.update([i])
    if i % 4 == 0:
        s4.update([i])



#Display the sets.
print(s2)
print(s3)
print(s4)

#Display if s3 is a subset of s2 (False)
print(s3 in s2)

#and if s4 is a subset of s2 (True).
print(s4 in s2)

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
py_set = set()
for i in "Python":
    py_set.update(i)
py_set.add("i")
print(py_set)

#Create a frozenset with the letters in ‘marathon’
m_set = frozenset(["m","a","r","a","t","h","o","n"])
print(m_set)


#display the union and intersection of the two sets.
print("union: ", py_set.union(m_set))
print("intersection: ", py_set.intersection(m_set))
