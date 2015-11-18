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


def colorize(
    fore_color="black", 
    back_color="white", 
    link_color="red", 
    visited_color="green"
):
    # Have it print the colors (use strings for the colors)
    print("The colors are:\n\
fore_color: {}\n\
back_color: {}\n\
link_color: {}\n\
visited_color: {}\n".format(fore_color, back_color, link_color, visited_color))

colors = {"link_color": "grey", "back_color": "yellow"}

colorize()
colorize("blue", "purple")

colorize("blue", **colors)
