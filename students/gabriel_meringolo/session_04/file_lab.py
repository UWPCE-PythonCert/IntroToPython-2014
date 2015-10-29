studs = open("students.txt", "r") # opens files and creates file object
studs.readline() # reads first line of file "skipping" name/ languages
lan_str = "" # enpty string
lan_list = [] # empty list

for i in studs:
    lan_list += (i[i.find(":") + 1:].replace(",","").split())
    """seperating names from languages/ removing comas
    and creating a list from the text doc with only the languages"""
lan_list.sort() # sorting list by alpha

for ii in lan_list:
    if ii not in lan_str:
        lan_str += ii + (int(20 - len(ii)) * " ") + str(lan_list.count(ii)) +  "\n"
        """creating string from list with counter and formatting"""

if __name__ == "__main__":
    print("\nPyCert 2015\nKnown Languages:   AMT:\n----------------------------\n{}".format(lan_str))