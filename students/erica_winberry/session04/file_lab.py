import os

os.chdir("../../../Examples")
student_data = []
f = open("students.txt", "r")
for line in f:
    line = line.split(":")
    student, langs = line
    if "\n" in langs:
        langs = langs.replace("\n", "")
    if "," in langs:
        langs = langs.replace(",", "")
    langs = langs.split(" ")
    student_data.append(langs)
f.close()

for i in student_data:
    for t in i:
        if t == "and":
            i.remove(t)
        if t == "":
            i.remove(t)
        if "," in t:
            t.replace(",", "")

def count_langs(l):
    languages = {}
    for t in l:
        for item in t:
            if item not in languages:
                languages[item] = 1
            else:
                languages[item] += 1
    return languages

for k, v in (count_langs(student_data)).items():
    print(v, k)

os.chdir("../students/erica_winberry/session04")



# for t in student_data:
#     get_count(t)

# print(student_data)
