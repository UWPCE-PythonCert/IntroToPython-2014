__author__ = 'Robert W. Perkins'


def get_book(target):
    """ Open target file and read contents into book_data"""
    f = open(target)
    book_data = f.read()
    f.close()
    return book_data


def strip_lines(in_text):
    """ Replace newlines with spaces"""
    return in_text.replace('\n', ' ')


def mk_wordlist(in_list):
    """Split input string at ' ' and return word list"""
    return in_list.split(' ')


def create_dict(orig_text):
    """ Create trigram dictionary from orig_text"""
    trigram = {}
    word_list = mk_wordlist(strip_lines(orig_text))
    for word in word_list:
        trigram_key = word_list[word] + " " + (word_list[word + 1])
        trigram[trigram_key] = word_list[word + 2]

    print word_list
    print trigram


if __name__ == '__main__':
    source_text = '/intropython/data/sherlock_small.txt'
    d = get_book(source_text)
    create_dict(d)
