def generate_trigram_db(filename):
    ''' Returns trigram dict
        f is a file descriptor '''
    db = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            array = line.split(' ')
            for i in range(len(array) - 2):
                if array[i + 2] not in db["{} {}".format(array[i],
                   array[i + 1])]:
                    db["{} {}".format(array[i], array[i + 1])] = array[i + 2]
