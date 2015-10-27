GridType = 1
Length = 4
XLength = 4
YLength = 4

# Two Column Function
def print_grid(Length):
   print("Generate a grid for grid selection Length =", Length)
   print('+' + (int(Length) * '-') + '+' + (int(Length) * '-') + '+')
   # Upper Block Grid Build
   for rows in range(0, int(Length)):
      print('|' + (int(Length) * ' ') + '|' + (int(Length) * ' ') + '|')
   # end for
   print('+' + (int(Length) * '-') + '+' + (int(Length) * '-') + '+')
   # Lower Block Grid Build
   for rows in range(0, int(Length)):
      print('|' + (int(Length) * ' ') + '|' + (int(Length) * ' ') + '|')
   # end for
   print('+' + (int(Length) * '-') + '+' + (int(Length) * '-') + '+')
# end func print_grid

# Multi Column Function
def print_grid1(XLength, YLength):
   print("Generate a grid for grid selection X =", XLength, "Y =", YLength)
   print('+' + (int(XLength) * '-') + '+' + (int(XLength) * '-') + '+')
   # Upper Block Grid Build
   for rows in range(0, int(YLength)):
      print('|' + (int(XLength) * ' ') + '|' + (int(XLength) * ' ') + '|')
   # end for
   print('+' + (int(XLength) * '-') + '+' + (int(XLength) * '-') + '+')
   # Lower Block Grid Build
   for rows in range(0, int(YLength)):
      print('|' + (int(XLength) * ' ') + '|' + (int(XLength) * ' ') + '|')
   # end for
   print('+' + (int(XLength) * '-') + '+' + (int(XLength) * '-') + '+')
# end print_grid1

# Multi Column Function
def print_grid2(XLength, YLength, Rows, Columns):
   for Rowsize in range(0, int(Rows)):
      if (Rowsize == 0): 
         print(int(Columns) * (('+' + (int(XLength) * '-') )) + '+')
      # else
      # Upper Block Grid Build
      for rowwwidth in range(0, int(YLength)):
         print(int(Columns) * (('|' + (int(XLength) * ' ') )) + '|')
      # end for
      print(int(Columns) * (('+' + (int(XLength) * '-') )) + '+')
   # end Row Build
# end print_grid1

GridType= input("Enter The grid type you want (1 = two columns (fixed size), 2 = multiple columns (variable x, y), 3 = variables rows, columns (fixed size):")

if (int(GridType) == 1):
   Length = input("Enter The Grid size You Want:")
   print ("The size you selected (Length) ", Length)
   print_grid(Length)
elif (int(GridType) == 2):
   XLength = input("Enter The Grid size You Want in X Dimention:")
   YLength = input("Enter The Grid size You Want in Y Dimention:")
   print ("The size you selected (X, Y) ", XLength, YLength)
   print_grid1(XLength, YLength)
elif (int(GridType) == 3):
   XLength = 4
   YLength = 4
   Rows = input("Enter the number of rows you would like:")
   Columns = input("Enter the number of columns you would like:")
   print ("The size you selected (Rows, Columns) ", Rows, Columns)
   print_grid2(XLength, YLength, Rows, Columns)
else:
   GridType = 4
   print("Hmm maybe you should try again.  Try entering 1 or 2 for the selection type")
# End if  


