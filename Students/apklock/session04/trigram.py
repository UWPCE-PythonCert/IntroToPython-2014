# infilename = "sherlock_small.txt"
infilename = "sherlock.txt"

import sys
import string
import random


def make_words(text):

    """
    make a list of words from a large bunch of text

    strips all the punctuation and other stuff from a string
    """

    # build a translation table for string.translate:
    # there are other ways to do this:
    #   a_word.strip() works well, too.

    punctuation = string.punctuation
    punctuation = punctuation.replace("'", "") # keep apostropies
    punctuation = punctuation.replace("-", "") # keep hyphenated words
    ## this will replace punctiation with spaces
    ##    -- then split() will remove the extra spaces
    table = string.maketrans(punctuation, " "*len(punctuation))

    # lower-case everything to remove that complication:
    text = text.lower()

    # remove punctuation
    text = text.translate(table)

    # remove "--" -- can't do multiple characters with translate
    text = text.replace("--", " ")

    # split into words
    words = text.split()

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    words2 = []
    for word in words:
        if word != "'": # remove quote by itself
            # "i" by itself should be capitalized
            words2.append("I" if word == 'i' else word)
    ## could be done with list comp too -- next week!
    # words2 = [("I" if word == 'i' else word) for word in words if word != "'"]

    return words2


def read_in_data(infilename):

    infile = open(infilename, 'r') # text mode is default
    # strip out the header, table of contents, etc.
    for i in range(61):
        infile.readline()

    full_text = []
    # read the rest of the file line by line
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
    for i in range(len(words) - 2): # minus 2, 'cause you need a pair'
        pair = tuple( words[i:i+2] )  # a tuple so it can be a key in the dict
        follower = words[i+2]
        word_pairs.setdefault(pair,[]).append(follower)

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
    for i in range(40): # do thirty sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice( word_pairs.keys() ) )

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2,10)):
            pair = tuple(sentence[-2:])
            sentence.append( random.choice(word_pairs[pair]) )
        #capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        #Add the period
        sentence[-1] += "."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


if __name__ == "__main__":

    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print "You must pass in a filename"
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print new_text
	
