#Paths 

"""
write a program which prints the full path to all files in the current directory, one per line
"""
import pathlib

foo = pathlib.Path('./')

print("Here are all the files in my current Session_04, printed with their full directory paths.  Yay."  )
for f in foo.iterdir():
    print(f.absolute())
