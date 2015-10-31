book_str = open("sherlock.txt", "r").read() # opened txt file as file object
book_list = book_str.split()

#first_twoStr = " ".join(book_str.split()[:2]) # isolating first two words as a string
first_twolst = book_list[:2] # first two words as a list


def string_maker(sub_list):
    """
    makes a string out of a list for formating
    :param sub_list: list to be turned into a string
    :return: string
    """
    return " ".join(sub_list)

def list_maker(string):
    """
    turns a string into a list for formatting
    :param string: a string
    :return: list
    """
    return string.split()


def follower(index):
    """
    returns the next item in the list
    :param index: item you want followed
    :return: next item in list
    """
    return book_list[index + 1]

print(first_twolst)
print(list_maker(follower(0)))

print(type(string_maker(first_twolst)))


#for index, word in enumerate(book_list[:10]):
#    if index is 9:
#        print(word, book_list[9 + 1])


print(first_twolst)
print(first_twoStr, " is a ", type(first_twoStr))


start_point = (book_str.index(first_twoStr) + len(first_twoStr))
next_word = [" ".join(book_str[start_point:].split()[:1])]
print(next_word, " is a ", type(next_word))
next_two = first_twoStr.split()[1] + " " + "".join(next_word)
#print(x.index())
print(next_two)
print(next_word)

#print(x[start_point])