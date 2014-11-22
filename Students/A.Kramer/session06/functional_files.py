import os
import sys

def clense(path_to_a_file):
    """Strip all the white space from around the lines of text"""
    
    # Intercept if command line argument is passed in
    if len(sys.argv) > 1:
        path_to_a_file = sys.argv[1]
    else:
        print "Using default file 'text.txt' located in the same directory with '%s' script" % os.path.basename(sys.argv[0])
    
    # Prompt for a file name (if any)
    new_file_name = ""
    answer = raw_input("Would you like to create a new file [Y/N]: ")
    if answer.lower() == "y":
        new_file_name = raw_input("Enter new file name (no spaces): ")
        if len(new_file_name.split()) > 1:
            print "You have entered a filename containing space. Buy. Try better next time. \nBye."
            # force to restart if space is detected in the filename
            return
    
    # Create temporary file
    temp_file = os.path.join(os.getcwd(), "temp.temp.txt")
    
    # Open files for reading/writing    
    try:
        with open(path_to_a_file, "rb") as f:
            lst = f.read().splitlines()
            
        # strip white space
        g = map(lambda x: x.strip(), lst) # g = [x.strip() for x in lst] # comprehension
        
        # write stripped lines into the temp.temp.txt file
        with open(temp_file, "wb") as nf:
            for item in g:
                if item:
                    nf.write(item)
                   
    # handle IOErrors                
    except IOError as e:
        print "IOError, debugging required", e
        return

    # if new name is given, rename temp file to the new name
    # if no new name, override the existing file
    if new_file_name:
        os.rename(temp_file, new_file_name)
    else:
        basename = os.path.basename(path_to_a_file)
        os.unlink(path_to_a_file)
        os.rename(temp_file, basename)
        
    print "Done!!!"
    
if __name__ == "__main__":
    clense("test.txt")