# Write a function that has four optional parameters (with defaults):
# fore_color
# back_color
# link_color
# visited_color
# Have it print the colors (use strings for the colors)
# Call it with a couple different parameters set
# Have it pull the parameters out with *args, **kwargs - and print those


def color_code(fore_color="ochre", back_color="sand", link_color="brown", visited_color="tan"):
    print("the fore is {}, the back is {}, the link is {} and the visited is {}.".format(fore_color, back_color, link_color,visited_color))


color_code()


colorz = {"fore": "blue", "back": "azure", "link": "navy", "visited": "periwinkle"}

def color_code2():
    print("the fore is {fore}, the back is {back}, the link is {link} and the visited is {visited}.".format(**colorz))


color_code2()


def color_code3(fore, back, link="pink", visited="salmon"):
    print("the fore is {}, the back is {}, the link is {} and the visited is {}.".format(fore, back, link, visited))
hues = ("red", "rose")

huez = {"link":"Pink","visited": "Salmon"}

color_code3(*hues, **huez)

