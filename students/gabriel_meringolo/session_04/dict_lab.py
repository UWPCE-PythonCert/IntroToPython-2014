#When the script is run, it should accomplish the following four series of actions:

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
dict = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate"}

#Display the dictionary.
print(dict)

#Delete the entry for “cake”.
del dict["cake"]

##Display the dictionary.
print(dict)

#Add an entry for “fruit” with “Mango” and display the dictionary.
dict["fruit"] = "Mango"

#Display the dictionary keys.
print(dict.keys())

#Display the dictionary values.
print(dict.values())

#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print("cake" in dict)

#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in dict)

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
#for i in dict[0]:
    #print(i)

#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
#Display the sets.
#Display if s3 is a subset of s2 (False)
#and if s4 is a subset of s2 (True).
#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#Create a frozenset with the letters in ‘marathon’
#display the union and intersection of the two sets.
