student_data = []
f = open("students.txt", "r")
for line in f:
    line = line.split(":")
    student, langs = line
    if "\n" in langs:
        langs = langs.replace("\n", "")
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


def get_count(l):
    for t in l:
        if t == []:
            pass
        else:
            num = l.count(t)
            return(num)

for i, item in enumerate(student_data):
    for t in item:
        x = get_count(t)
        print(t, x)




# for t in student_data:
#     get_count(t)

# print(student_data)
