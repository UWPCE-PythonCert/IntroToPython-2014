"""
Look at each set of three adjacent words in a document.
Use the first two words of the set as a key, and remember the fact
that the third word followed that key.

For this kata, try implementing a trigram algorithm that generates a
couple of hundred words of text using a book-sized file as input.

Be warned that these files have DOS line endings (carriage return
followed by newline).

Kata’s are about trying something many times. In this one, what we’re
experimenting with is not just the code, but the heuristics of
processing the text. What do we do with punctuation? Paragraphs?
Do we have to implement backtracking if we chose a next word that turns
out to be a dead end?
"""

# open a text file
# read the text file
    # split the text file into a series of strings (split on " ")
    # replace m-dashes with spaces.
# save the first two words as a key, and the next word as a value
    # repeat this for the entire text.

# Randomly select a key:value pair to start (select by capitalization?)
    # Convert all three into a string
# Find the key that matches the last two words of the above string
    # add the value from that key to the string
    # LRR
# Set the loop to end after a set number of tries, if the last value 
# a period at the end.

def trigram_prep(source_file):
    trigram_dict = {}
    with open(source_file, "r") as f:
        for line in f.read(): # use dict comprehension to shorten this
            line = line.replace("--", " ").split()
        
