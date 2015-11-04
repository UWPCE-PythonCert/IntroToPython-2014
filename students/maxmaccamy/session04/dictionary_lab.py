__author__ = 'Max'

import copy

def main():
    d = dict({'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'})
    dictExercise1(copy.deepcopy(d))
    dictExercise2(copy.deepcopy(d))
    setExercise1()
    setExercise2()


def dictExercise1(d):
    print(d) #Display the dictionary
    d.pop('cake')
    print(d) #Display the dictionary
    d['fruit'] = 'Mango'

    for keys in d.keys():
        print(keys)

    for values in d.values():
        print(values)

    if 'cake' in d.keys():
        print("cake is a key in dictionary")
    else:
        print("cake is not a key in dictionary")

    if 'Mango' in d.values():
        print("Mango is a value in dictionary")
    else:
        print("cake is not a value in dictionary")

def dictExercise2(d):
    for keys in d:
        d[keys] = str(d[keys]).upper().count("T")
    print(d)

def setExercise1():
    s2 = set([])
    s3 = set([])
    s4 = set([])

    for i in range(21):
        if 0 == i % 2:
            s2.add(i)
        if 0 == i % 3:
            s3.add(i)
        if 0 == i % 4:
            s4.add(i)
    #s2 = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    #s3 = set([0, 3, 6, 9, 12, 15, 18])
    #s4 = set([0, 4, 8, 12, 16, 20])

    print("S2: " + str(s2))
    print("S3: " + str(s3))
    print("S4: " + str(s4))

    if s3.issubset(s2):
        print("S3 is a subset of S2")
    else:
        print("S3 is not a subset of S2")

    if s4.issubset(s2):
        print("S4 is a subset of S2")
    else:
        print("S4 is not a subset of S2")

def setExercise2():
    s1 = set("Python")
    s1.add("i")
    print(str(s1))

    s2 = frozenset("marathon")

    #Display the union and intersection of the two sets
    print(str(s1.union(s2)))
    print(str(s1.intersection(s2)))


main()