studs = open("students.txt", "r+") # opens files and creates file object
studs.readline() # reads first line of file "skipping" name/ languages
lan_str = "" # enpty string
lan_list = [] # empty list

for i in studs:
    lan_list += (i[i.find(":") + 1:].replace(",","").split())
lan_list.sort()
for ii in lan_list:
    if ii not in lan_str:
        lan_str += ii + " " +  "\n"


print("PyCert 2015 known languages:\n{}".format(lan_str))
