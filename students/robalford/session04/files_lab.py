#
students = open('../../../Examples/students.txt')

languages = []
for line in students:
    line = line.split(': ')
    line.pop(0)
    if line:
        line[0] = line[0][:-1]
        line[0] = line[0].split()
    languages += line
students.close()
languages.pop(0)

language_list = []
language_frequency = {}
for student in languages:
    for language in student:
        language = language.lower()
        if language[-1] == ',':
            language = language[:-1]
        if language not in language_list:
            language_list.append(language)
        if language not in language_frequency:
            language_frequency[language] = 1
        else:
            language_frequency[language] += 1

print(language_list)
print(language_frequency)
