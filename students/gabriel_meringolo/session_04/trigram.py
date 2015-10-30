x = open("sherlock.txt", "r").read() # opened txt file as file object
y = x.split()
first_two = " ".join(x.split()[:2]) # isolating first two words

start_point = (x.index(first_two) + len(first_two))
next_word = [" ".join(x[start_point:].split()[:1])]
#print(" ".join(x[start_point:].split()[:1]))
#if first_two in x:
#    print(x.index(first_two + len(first_two)))
print(first_two, "=>", next_word)



