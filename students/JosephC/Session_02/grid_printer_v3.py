# grid printer

def printer():
    print('+', '-'*4, '+', '-'*4, '+')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('|', ' '*4, '|', ' '*4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
#the above is the stupid way

printer()

#create a line to differentiate the boxes
print("----------------------")


#Putting this on the back burner for now . . .
#SOLUTION:
def print_grid(size):
    """ Print a 2x2 grid with a total size of size
        :param size: total size of grid -- it will be rounded if not one more than a multiple of 2 """

    number = 2
    box_size = int((size - 1) // 2) #size of one grid box: integer division

    print("box size:", box_size)
    
    #top row
    top = ('+ ' + '- ' * box_size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * box_size) * number + '|' + '\n'

    row = top + middle * box_size

    grid = row * number + top

    print(grid)

def print_grid2(number, size):
    """ Print a number x number grid with each box of size width and height
    :param number: number of grid boxes (row and column)
    :param size: size of each grid box """

    #top row
    top = ('+ ' + '- ' * size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * size) * number + '|' + '\n'

    row = top + middle * size

    grid = row * number + top

def print_grid3(size):
    """ Same as the above but calling print_grid2 to do the work """
    
    number = 2

    box_size = (size - 1) // 2 #size of one grid box, with integer division
    print_grid2(number, box_size)

print_grid(11)
print_grid(7)

print_grid2(2,3)
print_grid2(3,5)

print_grid3(11)
