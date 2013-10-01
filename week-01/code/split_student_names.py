studentNames = list()
fr = open('C:\Users\Josh\PYTHON100\courseenrollees 9-30-13 - Sheet1.csv')
lines = fr.readlines()[1:]
fr.close()
#print(type(lines))
#print(len(lines))
for line in lines:
	segments = line.split(',')
	studentNames.append(segments[0] + ", " + segments[1])
# Python is smart enough to not keep on appending to this file when run multiple times
fw = open('C:\Users\Josh\PYTHON100\IntroToPython\week-01\students.txt', 'w')
for name in studentNames:
	fw.write(str(name) + '\n')
fw.close()