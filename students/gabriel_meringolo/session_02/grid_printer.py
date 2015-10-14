def makegrid():
    top = "+ - - - - " * 2 + "+\n"
    side = (("|" + " " * 9) * 2) + "|\n"
    print(top + side * 4 + top + side * 4 + top)

makegrid()