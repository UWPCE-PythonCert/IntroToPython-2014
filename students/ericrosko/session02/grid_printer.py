
def edgeline(count):
	return ("+" + ((" -" * count)) + " ") * 2 + "+" 

def middleline(count):
	return ("|" + (("  " * count)) + " ") * 2 + "|" + "\n"

def printlines(count):
	print(middleline(count))

def printgrid(rows, columns):
	assert isinstance(rows, int) and isinstance(columns, int), "Rows and columns must both be of integer type."
	print(edgeline(columns))
	print(middleline(columns) * rows, end="")
	print(edgeline(columns))
	print(middleline(columns) * rows, end="")
	print(edgeline(columns))

#printgrid(6, 5)

def main():
	while True:
		user_input = input("\nPrintGrid\nEnter width and height separated by comma, i.e. \"3,4\" (q to quit): ")
		if user_input == 'q':
			break;
		print(user_input)
		width = user_input.split(",")[0]
		height = user_input.split(",")[1]
		printgrid(int(height), int(width))

main()
