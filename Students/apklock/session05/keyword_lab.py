def colour(fore_colour = 'gold', back_colour = 'black', link_colour = 'green', visited_colour = 'red'):
	print "The default foreground colour is:", fore_colour
	print "The default background colour is:", back_colour
	print "The default link colour is:", link_colour
	print "The default visited colour is:", visited_colour

colour()
	
fore = raw_input("Type a new foreground colour here -->")
fore_colour = fore
	
back = raw_input("Type a new background colour here -->")
back_colour = back
	
link = raw_input("Type a new link colour here -->")
link_colour = link
	
visited = raw_input("Type a new visited colour here -->")
visited_colour = visited

def new_colours(*args):
	print "This is the new colour scheme:", args
	
new_colours(fore, back, link, visited)
