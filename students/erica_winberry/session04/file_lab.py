import os

os.chdir("../../../Examples")


def read_student_data(filename):
    student_data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(":")
            student, langs = line
            langs = langs.replace(",", "")
            langs = langs.replace("and", "")
            langs = langs.split(" ")
            student_data.append(langs)
        for item in student_data:
            for t in item:
                if t == "":
                    item.remove(t)
        return student_data


def count_langs(lang_source):
    languages = {}
    for t in lang_source:
        for item in t:
            if item not in languages:
                languages[item] = 1
            else:
                languages[item] += 1
    return languages

for k, v in (count_langs(read_student_data("students.txt"))).items():
    print(v, k)

os.chdir("../students/erica_winberry/session04")
