#write a program which copies a file from a source,
# to a destination (without using shutil, or the OS copy command)

#advanced: make it work for any size file: i.e. don’t read the
# entire contents of the file into memory at once.

#Note that if you want it to do any kind of file,
# you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing.)


def copy_file(original_file, new_file):
    file_original = open(original_file) # creates file object from txt file
    file_copy = open(new_file, "w") # creates empty new file
    file_copy.write(file_original.read()) # reads the file object and 'writes' it to new file
    file_original.close() # closes old file
    file_copy.close() # closes new file
    print("Copied contents of {} to {}".format(original_file, new_file))

copy_file("sherlock.txt","copy.txt")