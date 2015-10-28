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
#use an arugment to define the size of the grid

def print_grid(n):

    column = '+' + ' ' + 4*'-' + ' ' + '+'

    row = '|' + 4*' ' + '|' + 4*' ' + ' '+ '|\n' #change " n*' ' " to "4*' ' "
    
    # print( column*2 + '\n' + 4*row + column*2 + '\n' + 4*row + column*2 ) #this shit works

    #only produces three columns though    
    #print( column*2 + '\n' + 8*row + column*2 + '\n' + 8*row + column*2 ) 
    
    cell = column + '\n' + 4*row + column
    print(cell)

#go work with the above building blocks 

print_grid(1)


#enter n
#n number of columbs are created
#n number of rows are created

