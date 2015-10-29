studs = open("students.txt", "r+")
studs.readline()
for i in studs:
    cleani = i.strip()
    #print(cleani)
    if cleani:
        print(cleani[cleani.find(":") + 1:], end = "")
    #print(i[i.find(":") + 1:].strip("\n"))
    #print((i.split()))
    #print(i[i.find(":") + 1:])
    #print(i[i.find(":") + 1:], end = "")
    #print(i[i.find(":") + 1:].strip())
#print(studs.readlines())

#for i in studs:
#    print(i.split())