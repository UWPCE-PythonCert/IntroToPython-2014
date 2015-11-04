# write a program which prints the full path to all files in the current directory, one per line

import os # imports os module - allows interaction with os?

for i in os.listdir(os.getcwd()): # os.getcwd - gets current dir(pwd) os.listdir - lists contents of dir(ls)
    print(os.path.abspath(i)) # os.path.abspath() - shows full path- absolute path of files