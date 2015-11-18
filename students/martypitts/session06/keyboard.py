def colors(fore_color= "blue", back_color = "black", link_color = "yellow", visited_color = "green"):
    print("position: {},{},{},{}".format(fore_color, back_color, link_color, visited_color))

def colors2(*args):
    print("the positional arguments are:", args)

def colors3(**kwargs):
    print("the key word arguments are:", kwargs)



colors()
colors2("black", "green", "red", "white")
colors3(fore_color : "black", back_color = "green", link_color : "red", visited_color : "white")
#colors(*fore_color)
