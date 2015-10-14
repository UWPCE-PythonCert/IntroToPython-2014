def makegrid():
    top = "+ - - - - " * 2 + "+\n"
    side = (("|" + " " * 9) * 2) + "|\n"
    return top + side * 4 + top + side * 4 + top

print(makegrid())
