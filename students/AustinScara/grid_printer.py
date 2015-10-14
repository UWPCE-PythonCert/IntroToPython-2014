def grid(n):
	headMidBot = "+ " + "- "*n + "+" + " -"* n+ " +"
	mid = "|" + "  "*n + " + " + "  " *n + "|" + '\n'
	return headMidBot +'\n' + mid*n + headMidBot + '\n' + mid*n + headMidBot



size = int(input("How big Do you want this grid to be?"))

print (grid(size))
