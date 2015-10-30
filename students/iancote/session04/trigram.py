import re


def generate_trigram_db(filename):
    ''' Returns trigram dict
        f is a valid file name of a text Project Gutenberg ebook
        Punctuation is treated as a word
    '''

    db = {}
    l = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith('*** START OF THIS PROJECT GUTENBERG'):
                continue
            if line.startswith('*** END OF THIS PROJECT GUTENBERG'):
                break
            l += re.findall(r"[\w']+|[.,!?;]", line)
            for i in range(len(l) - 2):
                try:
                    if l[i + 2] not in db["{} {}".format(l[i], l[i + 1])]:
                        db["{} {}".format(l[i], l[i + 1])].append(l[i + 2])
                except KeyError:
                    db["{} {}".format(l[i], l[i + 1])] = [l[i + 2]]
            l = l[-2:]
    return db
