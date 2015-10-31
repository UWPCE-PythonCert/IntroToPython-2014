x = open("sherlock.txt", "r").read() # opened txt file as file object
y = x.split()
first_two = " ".join(x.split()[:2]) # isolating first two words


start_point = (x.index(first_two) + len(first_two))
next_word = [" ".join(x[start_point:].split()[:1])]
next_two = first_two.split()[1] + " " + "".join(next_word)
print(x.index())
print(next_two)


#print(x[start_point])