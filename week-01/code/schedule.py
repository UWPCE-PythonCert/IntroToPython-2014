"""
Schedule students for lightning talks, fall 2011
"""
import random

students = open('students.txt').read()

students = students.split('\n')

students.remove('')

random.shuffle(students)

weeks = range(2,11)

weeks4 = weeks*2

schedule = zip(weeks4, students)

schedule.sort()

outfile = open('schedule.txt', 'w')

print schedule

for week, student in schedule:
    line = 'week %s: %s\n' % (week, student)
    print line, 
    outfile.write(line)
outfile.close()

