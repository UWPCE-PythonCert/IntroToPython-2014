# This file prints a simple grid consisting of '+', '-', and '|' characters.
def print_grid(size):
    numfiller = size // 2
    crossline = "+" + (numfiller * "-") + "+" + (numfiller * "-") + "+"
    verticalline = "|" + (numfiller * " ") + "|" + (numfiller * " ") + "|"
    rtnString = ""
    for i in range(size):
        mod = i % numfiller
        if 0 == mod:
            rtnString += crossline + "\n"
        else:
            rtnString += verticalline + "\n"

    return rtnString

def print_grid(numboxes, numfiller):
    crossline = "+" + ((("-" * numfiller) + "+") * numboxes) + "\n"
    verticalline = "|" + (((" " * numfiller) + "|") * numboxes) + "\n"
    return (crossline + (((verticalline * numfiller) + crossline) * numboxes))

#print(print_grid(11))
#print(print_grid(3))
#print(print_grid(3,4))
#print(print_grid(5,3))
print(print_grid(3,3))
