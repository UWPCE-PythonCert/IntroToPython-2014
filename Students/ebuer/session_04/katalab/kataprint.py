"""
Reads the kata_dfile (kata dictionary) and makes a kata from a seed
"""


import ast, csv, random

katadict = dict()

with open('kata_dfile.csv', 'r') as f:
    filecontent = csv.reader(f, delimiter=',', quotechar='|')
    for row in filecontent:
        katadict.setdefault(row[0], ast.literal_eval(row[1]))

seed = ['vanished', 'into']

for n in range(100):
    phrase = seed[-2:]
    new_phrase = katadict.get('{p0} {p1}'.format(p0=phrase[0], p1=phrase[1]))
    new_phrase = random.choice(new_phrase)
    seed.append(new_phrase)

for i, s in enumerate(seed):
    print '{s} '.format(s=s),



# katadict = dict(temp)


