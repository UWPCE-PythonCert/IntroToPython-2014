studs = open("students.txt", "r+") # opens files and creates file object
studs.readline() # reads first line of file "skipping" name/ languages
lan_str = ""
for i in studs:
    lan_str += i.strip()[i.find(":") + 1:]
print(lan_str.replace(" ","\n").replace(",","")) # replaces spaces with \n and removes ,

    #print(type(i.strip()[i.find(":") + 1:]), end="")
    #print(i[i.find(":") + 1:], end = "") # prints languages
    #cleani = i.strip()
    #print(cleani)
    #if cleani:
    #    print(cleani[cleani.find(":") + 1:].strip(","), end = "")
    #print(i[i.find(":") + 1:].strip("\n"))
    #print((i.split()))
    #print(i[i.find(":") + 1:])
    #print(i[i.find(":") + 1:], end = "")
    #print(i[i.find(":") + 1:].strip())
#print(studs.readlines())

#for i in studs:
#    print(i.split())