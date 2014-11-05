'''
Paths and File Processing
--------------------------

  * write a program which prints the full path to all files in the current directory, one per line

  * write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
'''

import os

def myFileCopy (source, destination):
    '''
    Copy a file by reading the content and then writing them.
    '''
    try:
        file_in = open(source, 'r')
    except FileNotFoundError:
        print 'File not found'
        return
 
    try:
        file_out = open(destination, 'w')
    except FileExistsError:
        print 'Unable to create file'
        return 
        
        
    for line in file_in:
        file_out.write(line)
        
    file_out.close()
    file_in.close()
        
    
def printFullPathInCurrentDirectory():
    '''
    Print all filenames in the current directory.
    '''
    path = os.path.dirname(os.path.abspath(__file__))
    for (dirpath, dirnames, filenames) in os.walk(path):
        for  fname in filenames:
            print os.path.join(path, fname)

if __name__ == "__main__":
    printFullPathInCurrentDirectory()
    myFileCopy ('t.t', 't.a')
    

