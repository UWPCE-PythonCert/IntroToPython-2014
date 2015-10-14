
def edgeline(count):
	return ("+" + ((" -" * count)) + " ") * 2 + "+" 

def middleline(count):
	return ("|" + (("  " * count)) + " ") * 2 + "|" + "\n"

def printlines(count):
	print(middleline(count))
	
def printgrid(count):
	print(edgeline(count))
	print(middleline(count) * 4, end="")
	print(edgeline(count))
	print(middleline(count) * 4, end="")
	print(edgeline(count))

printgrid(4)
