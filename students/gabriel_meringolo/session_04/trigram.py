x = open("sherlock.txt", "r").read().split() # opened txt file as file object makes it readable and splits it
first_two = " ".join(x[:2])
print(first_two)
#x = y.read() # reading file object

#first_two = " ".join(x.split()[:2]) # isolating first two words

#print(first_two)
#x[x.index(first_two) + 1]
#print(x[x.find(first_two) + len(first_two) + 1])

#next_word = first_two.split()[1]
#print(next_word)

#print(first_two.split()[1])
#print(x[x.find(first_two) + len(first_two) + 1:])
#print(first_two)
#if first_two in x:
#    print(x[x.find(first_two) + len(first_two) + 1:])
#print(" ".join(x.split()[:2]))

#print(x[x.find("may") + len("may") : ])


