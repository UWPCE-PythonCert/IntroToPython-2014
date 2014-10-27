"""
Functions for kata
"""


def linebreak(line):
    """Return list of words from line, split on spaces
    """
    l = line.strip('\n')
    l = l.split(' ')
    return l


def bookbreak(book):
    """ Returns list of all words from book file

        Input is a list of lines each in a list.
    """
    booklist = []
    for line in book:
        l = line.split(' ')
        for w in l:
            booklist.append(w)

    return booklist


def stringbreak(word, sep):
    """Returns list of words separated by 'sep
    """
    if word.find(sep) != -1:
        return word.split(sep)
    else:
        return word


def sanitize(word):
    """Returns string without punctuation
    """
    word = word.strip('."?!')
    word = word.strip("',() :;")

    for s in ['"', '?', '.', ':', ';', ',', "'"]:  # stuff to get rid of
        if word.find(s):
            word = word.replace(s, '')

    for s in ['--']:  # stuff to substitute with a space
        if word.find(s):
            word = word.replace(s, ' ')
    return word
