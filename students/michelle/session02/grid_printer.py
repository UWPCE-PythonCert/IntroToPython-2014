#print("let's see if this works")
fourminus = "- " * 4
border = '+ ' + fourminus + '+ ' + fourminus + '+' + '\n'
ninespace = ' '*9
middle = '|' + ninespace + '|' + ninespace + '|' + '\n'
grid = border + middle * 4 + border + middle * 4 + border
print (grid)