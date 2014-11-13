#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python


def read_file_to_list(a_file):
    """Return a list of the lines in a file with newlines removed"""
    # move file to begining
    a_file.seek(0)

    # add lines to list
    a_list = []
    for line in a_file:
        a_list.append(line.strip())

    return a_list


def parse_languages(a_list):
    """Return a list of distinct languages."""
    a_set = set()

    # parse text file
    for item in a_list:
        # split students and languages
        student_lang = item.split(':')

        # split languages
        lang = student_lang[1].split(',')

        # add languages to set
        for l in lang:
            if len(l.strip()) > 0:
                a_set.add(l.strip())

    # convert to list
    b_list = []
    for language in a_set:
        b_list.append(language)

    # sort list
    b_list.sort()

    return b_list


path_students = '../../../Examples/Session01/students.txt'
file_students = open(path_students, 'r')
list_students = read_file_to_list(file_students)
list_languages = parse_languages(list_students)
