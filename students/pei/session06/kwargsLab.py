# the "=" makes it optional argument
def color(fore_color="white",back_color = "black",link_color = "blue", visited_color ="green"):
    print ("fore_color is {}, back_color is {}, link_color is {}, visited_color is {}".format(fore_color,back_color,link_color, visited_color))
c = {"back_color": "gold", "link_color" : "silver"}
color(**c)
color("orange", **c)
color("orange",visited_color ="pink", **c)