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