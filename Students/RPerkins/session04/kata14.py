__author__ = 'Robert W. Perkins'


def get_book():
    f = open('secrets.txt')
    secret_data = f.read()
    f.close()


if __name__ == '__main__':
    get_book()