__author__ = 'Robert W. Perkins'


def get_book(target):
    """ Open target file and read contents into book_data"""
    f = open(target)
    book_data = f.read()
    f.close()
    return book_data


def strip_newlines(in_text):
    """ Replace newlines with spaces"""
    return in_text.replace('\n', ' ')


def mk_wordlist(in_list):
    """Split input string at ' ' and return word list"""
    return in_list.split(' ')


def create_dict(orig_text):
    """ Create trigram dictionary from orig_text"""
    trigram = {}
    word_list = mk_wordlist(strip_newlines(orig_text))
    for idx, word in enumerate(word_list):
        if idx > (len(word_list) - 3):
            break
        else:
            trigram_key = '%s %s' % (word_list[idx], word_list[idx + 1])
            print trigram_key
            print idx
            if trigram_key in trigram:
                trigram[trigram_key].append(word_list[idx + 2])
            else:
                trigram[trigram_key] = [word_list[idx + 2]]

    print trigram


if __name__ == '__main__':
    source_text = '/intropython/data/sherlock_small.txt'
    d = get_book(source_text)
    create_dict(d)
