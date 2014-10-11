def Rowline(size, column):
# prints an "x", then a number of "-"s (scaled by the "size" parameter),
# for each count of the "column" parameter
    for i in range(column):
        print "+",
        for x in range(4 + (size-1)):
            print "-",
    print "+" # the "bookend" character
    return

def Columnline(size, column):
# prints an "|", then a number of " "s (scaled by the "size" parameter),
# for each count of the "column" parameter
    for i in range(column):
        print "|",
        for x in range(4 + (size-1)):
            print " ",
    print "|" # the "bookend" character
    return

def PrintGrid(size, row, column):
# the outer loop prints a "row" number of rowlines
# the inner loop prints a number of column lines scaled
# by the "size" parameter
    for i in range(row):
        Rowline(size, column)
        for i in range(4 + (size-1)):
            Columnline(size, column)
    Rowline(size, column) # the "bookend" row

PrintGrid(1,2,2)