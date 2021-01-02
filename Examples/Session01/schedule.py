"""
Schedule students for lightning talks, fall 2014
"""
import random
students = open('C:/Users/Jerry-mining/GitHub/IntroToPython/Examples/Session01/students.txt').readlines()
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
weeks = range(2,38)
# weeks = 4
# weeks4 = weeks*4
schedule = zip(weeks, students)
# schedule.sort()
outfile = open('C:/Users/Jerry-mining/GitHub/IntroToPython/Examples/Session01/schedule.txt', 'w')
for week, student in schedule:
    line = 'week %s: %s\n' % (week, student)
    print (line),
    outfile.write(line)
outfile.close()
