def grid(n):
	headMidBot = "+ " + "- "*n + "+" + " -"* n+ " +"
	mid = "|" + "  "*n + " + " + "  "*n + "|" + '\n'
	return headMidBot +'\n' + mid*n + headMidBot + '\n' + mid*n + headMidBot





print (grid(10))