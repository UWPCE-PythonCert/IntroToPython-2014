"""
pathlab

write a program which prints the full path to all files in the current directory, one per line

write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)

"""
import os
newset = [[root, dirs, files] for root, dirs, files in os.walk(".", topdown=False)]