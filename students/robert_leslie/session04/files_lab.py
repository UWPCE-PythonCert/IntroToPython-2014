#!/usr/bin/env python3


langs = []

num_langs = {}

for line in open('../../../Examples/students.txt', 'r'):
    #print(line)
    line = line.split(':')[1]
    line = line.replace(',', '')
    line = line.replace('\n', '')
    line = line.split(' ')
    line.pop(0)
    if len(line) < 1:
        break
    #print(line)
    for lang in line:
        if lang in ('languages', ''):
            pass
        else:
            if not lang in langs:
                langs.append(lang)
            if lang in num_langs.keys():
                num_langs[lang] = num_langs[lang] + 1
            else:
                num_langs[lang] = 1

#print(langs)
#print(num_langs)
print()
for k, v in num_langs.items():
    print("{:20}{}".format(k,v))


