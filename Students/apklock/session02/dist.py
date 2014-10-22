def dist(x1, y1, x2, y2):
	x3 = abs(x1 - x2)
	y3 = abs(y1 - y2)
	z = (x3 * x3) + (y3 * y3)
	return math.sqrt(z)
	
