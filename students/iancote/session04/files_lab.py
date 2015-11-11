languages = {}

with open("../../../Examples/students.txt", 'r') as f:
    for line in f:
        line = line.rstrip()
        student, lingos = line.split(":")
        lingos = lingos.strip()
        for l in lingos.split(" "):
            if l == '':
                continue
            if l in languages:
                languages[l] += 1
            else:
                languages[l] = 1

index = list(languages.keys())
index.sort()

for i in index:
    print("{} : {}".format(i, languages[i]))
