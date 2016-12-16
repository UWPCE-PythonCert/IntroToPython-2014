#!/usr/bin/env python

"""
Trigram.py

A solution to the trigram coding Kata:

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

Chris Barker's Solution -- with improvements by Maria Mckinley

This one is pretty straight forward -- really a quickie script

There is lots of room to make it fancier of you want
"""

import sys
import random


def make_words(text):
    """
    make a list of words from a large bunch of text

    Strips all the punctuation and other stuff from a
    large string, and returns a list of words
    """
    replace_punc = [('-', ' '),
                    (',', ''),
                    (',', ''),
                    ('.', ''),
                    (')', ''),
                    ('(', ''),
                    ('"', '')]

    # make a translation table for str.translate
    table = {}
    for orig, replace in replace_punc:
        table[ord(orig)] = replace
    text = text.translate(table)
    # lower-case everything to remove that complication:
    text = text.lower()

    # split into words
    words = text.split()

    # remove the bare single quotes: "'" is both a quote and an apostrophe
    # and capitalize "i"
    words2 = []
    for word in words:
        if word != "'":  # remove quote by itself
            # "i" by itself should be capitalized
            words2.append("I" if word == 'i' else word)
    # could be done with list comprehension too -- next week!
    # words2 = [("I" if word == 'i' else word) for word in words if word != "'"]
    return words2
    print(words)
    return words


def read_in_data(infilename):
    """
    read the contents of a project Gutenberg book

    returns it as one big string
    """
    with open(infilename, 'r') as infile:  # text mode is default
        # strip out the header, table of contents, etc.
        for i in range(61):
            infile.readline()

        full_text = []
        # read the rest of the file line by line -- stopping at the footer
        for line in infile:
            if line.startswith("End of the Project Gutenberg EBook"):
                break
            full_text.append(line)

    # put all the lines together into one big string:
    return " ".join(full_text)


def build_trigram(words):
    """build a trigram dict from the passed-in list of words"""

    # Dictionary for trigram results:
    # The keys will be all the word pairs
    # The values will be a list of the words that follow each pair
    word_pairs = {}

    # loop through the words
    # (rare case where using the index to loop is easiest)
    for i in range(len(words) - 2):  # minus 2, 'cause you need a pair
        pair = tuple(words[i:i + 2])  # a tuple so it can be a key in the dict
        follower = words[i + 2]
        word_pairs.setdefault(pair, []).append(follower)

        # setdefault() returns the value if pair is already in the dict
        #    if it's not, it adds it, setting the value to a an empty list
        #    then it returns the list, which we then append the following
        #    word to -- cleaner than:
        # if pair in word_pairs:
        #     word_pairs[pair].append(follower)
        # else:
        #     word_pairs[pair] = [follower]
    return word_pairs


def build_text(word_pairs):

    """
    Build some new text from the word_pair dict supplied

    A bit of fancy stuff to make them look like sentences..
    """

    new_text = []
    for i in range(10):  # do ten sentences
        # pick a word pair to start the sentence
        # need to make dict.keys() a list to randomly select from it
        sentence = list(random.choice(list(word_pairs.keys())))
        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])  # the next word pair is the last two words
            sentence.append(random.choice(word_pairs[pair]))

        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()

        # Add the period
        sentence[-1] += "."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
