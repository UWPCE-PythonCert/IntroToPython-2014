
import collections

# initialize variables.
language_list = []
language_list_1 = []
language_list_stripped = []
#
# open students.txt
file = open('students.txt')
# remove students name from string_name_language list, and add all languages to a new list called language_list.
string_name_language = file.readlines()
for item in string_name_language:
    language_start_position = item.index(':')
    language_items = item[language_start_position + 1: -1]
    language_list.append(language_items)

# remove first element, strip whitespace from elements and remove empty elements from language_list list.
# make a list called language_list_stripped, in which each element contains one or multiple languages.
for item1 in language_list:
    item2 = item1.strip()
    if item2 != 'languages' and item2 != '':
        language_list_stripped.append(item2)

# make a new list called language_list_1, in which, each element is a list, and each element in the inner list contains ONE language.
for item3 in language_list_stripped:
    item4 = item3.split()
    language_list_1.append(item4)

# convert language_list_1 to a new list called language_list_2, in which, each element is a language.
item7 = ''
for item5 in language_list_1:
    # convert a list to a string
    item6 = ''.join(item5)
    if not item6.endswith(','):
        item6 = item6 + ','
    item7 = item7 + item6

# convert a string called item7 to a list called language_list_2.
# convert language_list_2 to a set, and then convert the set to a new list called language_list_3, and so the elements in language_list_3 are unique.
language_list_2 = item7.split(',')

# remove all empty elements from the list: language_list_2.
while True:
    try:
        empty_element_positon = language_list_2.index('')
        language_list_2.pop(empty_element_positon)
    except ValueError:
        break

language_list_3 = list(set(language_list_2))

print 'List all languages that students know :\n'
for item9 in language_list_3:
    print item9

# get the number of students on each language listed in language_list_3.
counter = collections.Counter(language_list_3)

print '\n\nList how many students know on each language :\n'
for keys,values in counter.items():
    print(keys)
    print(values)
