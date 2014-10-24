__author__ = 'Robert W. Perkins'


def get_book(target):
    f = open(target)
    book_data = f.read()
    f.close()
    return book_data


if __name__ == '__main__':
    source_text = '/intropython/data/sherlock_small.txt'
    print get_book(source_text)