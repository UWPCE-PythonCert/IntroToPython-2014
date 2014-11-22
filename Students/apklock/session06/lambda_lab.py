print "The equation is x**4 + (x*y) + y**2 - x**y + y**x,"
print "where y is the set of numbers 1 through 10"

x = raw_input("Input value for x here -->")

x = int(x)

lam = []
for i in range(10):
	lam.append(lambda x, y=i: x**4 + (x*y) + y**2 - x**y + y**x)
	
for f in lam:
	print f(x)
	
