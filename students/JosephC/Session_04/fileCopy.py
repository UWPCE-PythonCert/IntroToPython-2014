#Files

"""
write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
"""
import sys

source, dest = sys.argv[1:3]



#   go into binary mode

# define a variable named 'infile' that opens a source file in 'rb' or 'read binary' # mode
infile = open(source, 'rb') # read binary mode
# define a variable 'outfile' that opens a destination file, writing in binary
outfile = open(dest, 'wb') # write 

# what outfile writes is what infile reads; then both files are closed
outfile.write(infile.read())
infile.close()
outfile.close()

#   one line solution
open(dest, 'wb').write(open(source, 'rb').read())
 


      


