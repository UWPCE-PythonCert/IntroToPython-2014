# This file prints a simple grid consisting of '+', '-', and '|' characters.
def makegrid(size):
    numfiller = size // 2
    crossline = "+" + (numfiller * "-") + "+" + (numfiller * "-") + "+"
    verticalline = "|" + (numfiller * " ") + "|" + (numfiller * " ") + "|"
    for i in range(size):
        mod = i % numfiller
        if 0 == mod:
            print(crossline)
        else:
            print(verticalline)

    return None

makegrid(11)