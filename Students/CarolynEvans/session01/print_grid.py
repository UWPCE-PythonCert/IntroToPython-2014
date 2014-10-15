# This was my first attempt.
# This one prints the number of boxes horizontal and vertical based on the 'x' parameter,
# and the size of each box is determined by the 'x' parameter as well.
def grid1(x):

    for a in range(0,x,1):

        for b in range(0,x,1):

            print '+',

            for c in range(0,x,1):
                print '-',

        print '+'

        for b in range(0,x,1):

            for c in range(0,x,1):

                print '|',

                for a in range(0,x,1):
                    print ' ',

            print '|'

    for b in range(0,x,1):

        print '+',

        for c in range(0,x,1):
            print '-',

    print '+'

grid1(4)

# This was my second attempt.
# This one also prints the number of boxes horizontal and vertical based on the 'size' parameter,
# and the size of each box is determined by the 'size' parameter as well.
# The difference is that the code has been simplified by calling a sub-function.
def grid2(size):

    for a in range(0,size,1):

        lineDraw2(size,'+','-')

        for b in range(0,size,1):
            lineDraw2(size,'|',' ')

    lineDraw2(size,'+', '-')

def lineDraw2 (size,border,filler):
    for a in range(0,size,1):

        print border,

        for b in range(0,size,1):
            print filler,

    print border

grid2(4)


# Then I read the homework assignment more thoroughly.
# This one prints a grid with two vertical and two horizontal boxes.
# The size of whole entire grid is determined by the 'size' parameter.
def grid3(size):

    size -= 1
    size /= 2
    size -= 1

    for outerLoop in range(0,2,1):

        lineDraw3(size,'+','-')

        for innerLoop in range(0,size,1):
            lineDraw3(size,'|',' ')

    lineDraw3(size,'+', '-')

def lineDraw3 (size,border,filler):
    for outerLoop in range(0,2,1):

        print border,

        for innerLoop in range(0,size,1):
            print filler,

    print border

grid3(13)


