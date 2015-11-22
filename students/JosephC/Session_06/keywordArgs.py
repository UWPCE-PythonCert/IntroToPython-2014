#Keyword argument lab

''' 
    Write a function that has four optional parameters (with defaults):
        fore_color
        back_color
        link_color
        visited_color
    Have it print the colors (use strings for the colors)
    Call it with a couple different parameters set
    Have it pull the parameters out with *args, **kwargs - and print those

'''
#   create with defaults
def pretty_colors(fore_color = 'white', back_color='grey', link_color='blue', visited_color='purple'):
	print("Here are the colors you've chosen : {}, {}, {} ,{}".format(fore_color, back_color,link_color, visited_color))

#   call with different parameters
pretty_colors('purple', 'red', 'yellow', 'green')

#	call with a bunch of hex parameters set
pretty_colors('90CDD4','DE1BAD','B0D1B5','2fB00C')

#   create a dictionary and stuff to pass along
foreBack = ("teal", "purple")
links = {'link_color': 'blue', 'visited_color': 'red'}

pretty_colors(*foreBack, **links)

#   pull out parameters using * and **

def very_pretty(*args, **kwargs):
    print("The background color will always be {}!  The rest can be just {}".format(args, kwargs))

very_pretty('white' , fore_color= "grey", link_color = "blue", visted_color = "red")

