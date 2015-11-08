#!/usr/bin/python3

import re
import random
import glob


def generate_trigram_db(filename):
    ''' Returns trigram dict
        f is a valid file name of a text Project Gutenberg ebook
        Punctuation is treated as a word
    '''

    db = {}
    l = []

    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line or line.startswith(
                                 '*** END OF THIS PROJECT GUTENBERG'):
                break
            if line.startswith('*** START OF THIS PROJECT GUTENBERG'):
                continue
            l += re.findall(r"[\w']+|[.,!?;]", line)
            for i in range(len(l) - 2):
                try:
                    if l[i + 2] not in db["{} {}".format(l[i], l[i + 1])]:
                        db["{} {}".format(l[i], l[i + 1])].append(l[i + 2])
                except KeyError:
                    db["{} {}".format(l[i], l[i + 1])] = [l[i + 2]]
            l = l[-2:]
    return db


def write_story(db, length):
    ''' Return string containing story created from db and begin of length '''
    story = list(random.choice(begin_story(db)).split(' '))

    cursor = 0

    while cursor < (length - 2):
        # Match on last two words to get db.key
        # choose random option from list
        word_list = db["{} {}".format(story[cursor], story[cursor + 1])]
        story.append(random.choice(word_list))
        cursor += 1

    # story is still a list ans has spaces inserted before punctuation.
    # returning a string with leading space stripped from punctuation
    return re.sub(r'\s([?.!;,"](?:\s|$))', r'\1', ' '.join(story))


def begin_story(db):
    ''' Return list of all dict keys that start with a capital letter. '''
    l = []

    for i in db.keys():
        x = []
        x += i
        if x[0].isupper():
            l.append(i)
    return l

if __name__ == "__main__":
    db = {}
    for i in glob.glob('*.txt'):
        db.update(generate_trigram_db(i))
    print('DB has {} key entries'.format(len(db)))
    print(write_story(db, 500))
