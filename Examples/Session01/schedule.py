"""
Schedule students for lightning talks, fall 2014
"""
import random

students = open('students.txt').readlines()

# remove the header line
del students[0]

# clean it up a bit:

# remove the languages, colon, etc.
students = [line.split(":")[0] for line in students]

# reverse the first, last names

# separate them:
students = [line.split(",") for line in students]

# put them back together
students = [first + last for last, first in students]

random.shuffle(students)

weeks = range(2,11)

weeks4 = weeks*4

schedule = zip(weeks4, students)

schedule.sort()

outfile = open('schedule.txt', 'w')

for week, student in schedule:
    line = 'week %s: %s\n' % (week, student)
    print line,
    outfile.write(line)
outfile.close()
