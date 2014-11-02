#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import string


def file_to_list(a_file, start_line=0, end_line=0):
    """Read lines of file into a list. Ignore blank and all cap lines."""

    a_list = []

    ignore_list = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.',
                   'IX.', 'X.', 'XI.', 'XII.']

    for idx, line in enumerate(a_file, start_line):

        # strip whitespace out of line
        line = line.strip()

        # stop reading if reached end_line parameter
        if end_line and idx >= end_line:
            break

        else:
            # check if line starts with text in ignore list
            start_with_ignore = False
            for word in ignore_list:
                if line.startswith(word):
                    start_with_ignore = True
                    break

            # only add line to list if it's non-blank and non-uppercase
            if line and not line.isupper() and not start_with_ignore:
                a_list.append(line)

    return a_list


def build_trigram(all_words):
    """Return a trigram dictionary."""
    trigram_dict = dict()
    for idx, word in enumerate(all_words):

        # only add words to dict if there are three words left
        if idx < len(all_words) - 3:

            # build keys and values for dict
            key = '{:s} {:s}'.format(word, all_words[idx + 1])
            value = all_words[idx + 2]

            # get or set the current_set for the given key
            current_set = trigram_dict.setdefault(key, set([value]))

            # add new value to the current set
            current_set.add(value)

    return trigram_dict


def get_trigram_output(trigram, start_words, num_of_words):
    """Print trigram."""
    trigram_output = start_words.split()
    key_string = '{:s} ' * 2
    key_string = key_string.strip()

    for i in range(num_of_words):
        # build the key to lookup the set of next words from dictionary
        key = key_string.format(*trigram_output[i:i+2])

        # get the set of next words
        try:
            return_set = trigram[key]
        except KeyError:
            break

        # randomly choose and remove a word from the set
        next_word = return_set.pop()

        # add the new work to the output list
        trigram_output.append(next_word)

    return trigram_output


def clean_string(s, lowercase = False, punctuation = False):
    s = s.strip()  # strip whitespce

    if lowercase:
        s = s.lower()  # convert to lowercase

    if punctuation:
        # create list with all punctuation
        delete_characters = list(string.punctuation)

        # exclude some punctuation from being removed
        delete_characters.remove('!')
        delete_characters.remove('.')
        delete_characters.remove('?')
        delete_characters.remove(',')
        delete_characters.remove("'")

        s = s.translate(None, ''.join(delete_characters))

    return s

if __name__ == '__main__':

    path_book = ('/Users/salimhamed/Documents/Documents/School/'
                 'Python (2014)/downloads/sherlock.txt')

    # path_book = ('/Users/salimhamed/Documents/Documents/School/'
    #             'Python (2014)/downloads/sherlock_small.txt')

    start_line = 0  # starting line of the file
    end_line = 0  # ending line of the file

    num_of_words_to_print = 200
    start_words = 'I did'

    # read file to list
    f = open(path_book)
    f_list = file_to_list(f, start_line, end_line)

    # condense list to a single string
    f_string = ' '.join(f_list)

    # strip white space and remove quotes
    f_string = clean_string(f_string, lowercase = False, punctuation = False)

    # split single string into list of words
    words_list = f_string.split()

    # build a trigram
    trigram_dict = build_trigram(words_list)

    # get trigram list
    trigram_list = get_trigram_output(trigram_dict,
                                      start_words,
                                      num_of_words_to_print)

    # print trigram list
    print_string = ('{:s} ' * len(trigram_list))[:-1]
    print 'Trigram of {:d} words:'.format(len(trigram_list))
    print print_string.format(*trigram_list)
