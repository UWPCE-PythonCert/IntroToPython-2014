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

import random

# Fuction #1: trigram_prep
# open a text file
# read the text file
    # split the text file into a series of strings (split on " ")
    # replace m-dashes with spaces.
# save the first two words as a key, and the next word as a value
    # repeat this for the entire text.


def trigram_prep(source_file):
    word_list = []
    trigram_dict = {}
    with open(source_file, "r") as f:
        for line in f: # later: use dict comprehension to shorten this
            line = line.replace("--", " ").replace("(", "").replace(")", "").split()
            word_list.extend(line)
        for word in range(len(word_list)-2):
            pair = " ".join(word_list[word:word+2])
            value = word_list[word+2]
            trigram_dict[pair] = value
#            trigram_dict[" ".join(word_list[0:2])] = word_list[+2]
        return trigram_dict

# Function #2: create trigram text
# Randomly select a key:value pair to start; capitalize first letter.
# Find the key that matches the last two words of the above string
    # add the value from that key to the string
    # LRR
# Set the loop to end after a set number of tries, if the last value 
# a period at the end.


def create_trigram_text(source_dict, length):
    trigram = ["I", "was"]
    # trigram = [random.choice(list(source_dict.keys()))]
    for i in range(length):
        pair = " ".join(trigram[-2:])
        # print(pair)
        new_word = source_dict[pair]
        trigram.append(new_word)
    final_output = " ".join(trigram)
    print(final_output)

    # trigram = [random.choice(list(source_dict.keys()))]
    # try:
    #     pair.lower() in source_dict
    # except KeyError:
    #     print("KeyError: The phrase '" + pair + "' doesn't exist in the text!")
    # first_pair = " ".join(trigram)
    # first_v = source_dict[first_pair]
    # trigram.append(first_v)
    # print(type(trigram))
    # trigram[0] = trigram[0].capitalize()




    # try:
        # trigram.append(source_dict[start.lower()])
    # except KeyError:
        # print("KeyError: The phrase '" + start + "' doesn't exist in the text!")
    # trigram = start.capitalize() + " " + source_dict[start]

# def format_test(source_dict):
#     # An attempt to make the initial language of the trigram generated 
#     # text more likely to be grammatically correct.
#     format_test = 0
#     while format_test < 1:
#         starter = [random.choice(list(source_dict.keys()))]
#         if "." in starter:
#             pass
#         elif "," in starter:
#             pass
#         elif '"' in starter:
#             pass
#         else:
#             starter[0] = starter[0].capitalize()
#             format_test = 1
#     return starter


create_trigram_text(trigram_prep("sherlock_small.txt"), 20)

# trigram_prep("sherlock_small.txt")










