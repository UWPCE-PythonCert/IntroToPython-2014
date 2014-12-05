mylist = ["apples", "pears", "oranges", "peaches"]
print mylist

addfruit = raw_input ("Which fruit would you like to add?")
mylist.append(addfruit)
print mylist

asknumber = int(raw_input("Give me a number and I will show you that fruit!"))
if (asknumber >= 1) and (asknumber <= len(mylist)):
	print str(asknumber) + " " + mylist[asknumber - 1]
else: 
	print "Your number is out of range."

print ["Kiwis"] + mylist

mylist.insert(0, "melons")
print mylist

for item in mylist:
	if item.startswith("p"):
		print item

print mylist
del mylist[len(mylist)-1]
print mylist

removefruit = raw_input ("Which fruit would like you remove?")
mylist.remove(removefruit)
print mylist

for item in mylist:
	checkfruit = raw_input("Do you like %s?" %item)
	checkfruit = checkfruit.lower()
	if checkfruit == "yes":
		print mylist
	if checkfruit == "no":
		del item
	while checkfruit != "yes" and checkfruit != "no":
		print ("Please enter either 'yes' or 'no'.")
		checkfruit = raw_input("Do you like %s?" %item)
print mylist

mylist_copy = mylist[:]
print mylist_copy

for item in mylist_copy:
	reversed_mylist_copy = item[::-1]
	print reversed_mylist_copy

print mylist
del mylist[len(mylist)-1]
print mylist
print mylist_copy
