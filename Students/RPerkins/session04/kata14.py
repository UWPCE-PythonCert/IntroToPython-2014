__author__ = 'Robert W. Perkins'
import random


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
    """Split input string at spaces and return word list"""
    return in_list.split(' ')


def create_dict(orig_text):
    """ Create trigram dictionary"""
    trigram = {}
    word_list = mk_wordlist(strip_newlines(orig_text))
    for idx, word in enumerate(word_list):
        if idx > (len(word_list) - 3):
            break
        else:
            trigram_key = '%s %s' % (word_list[idx], word_list[idx + 1])
            if trigram_key in trigram:
                trigram[trigram_key].append(word_list[idx + 2])
            else:
                trigram[trigram_key] = [word_list[idx + 2]]
    return trigram


def get_randomkey(t_gram):
    """Return a random key"""
    return random.choice(list(t_gram.keys()))


def get_newword(word_key, word_dict):
    """Return a random word from the list at the provided key"""
    new_wordlist = word_dict.get(word_key)
    return random.choice(new_wordlist)


def create_newbook(trigram_dict, word_limit, w_line):
    """Create random output of num_words words, using trigram_dict keys to generate new words"""
    start_key = get_randomkey(trigram_dict)
    new_word = get_newword(start_key, trigram_dict)
    out_list = start_key.split(' ')
    out_list.insert(0, '...')
    out_list.append(new_word)
    left_frame = 0

    for i in range(word_limit):
        for j in range(w_line):
            next_key = '%s %s' % (out_list[left_frame+1], out_list[left_frame + 2])
            while not next_key in trigram_dict:
                next_key = get_randomkey(trigram_dict)
            next_word = get_newword(next_key, trigram_dict)
            out_list.append(next_word)
            left_frame += 1
        out_list.append('\n')
    out_list.append('...')
    out_string = ' '.join(out_list)
    return out_string


if __name__ == '__main__':
    # num_words gives the number of words to be generated
    # words_line gives the number of words per line
    num_words = 200
    words_line = 20
    #source_text = '/intropython/data/sherlock_small.txt'
    source_text = '/intropython/data/sherlock.txt'

    new_inbook = get_book(source_text)
    new_dict = create_dict(new_inbook)
    new_outbook = create_newbook(new_dict, num_words, words_line)
    print new_outbook