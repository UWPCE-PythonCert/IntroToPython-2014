studs = open("students.txt", "r+")
for i in studs:
    print(i[i.find(":") + 1:], end = "")
    #print(i[i.find(":") + 1:].strip())
#print(studs.readlines())

#for i in studs:
#    print(i.split())