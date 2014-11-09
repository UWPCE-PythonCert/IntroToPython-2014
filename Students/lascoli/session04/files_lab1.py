#read file into variable line
f = open('C:\Users\LA7383\Desktop\Python\UW_Python\IntroToPython\Examples\Session01\students.txt')
the_set = set()
for line in f:
           
    #convert all text to lower case
    line = line.lower()
    # print('Output 2', line)

    #remove white spaces
    line = line.replace(" ", "")
    # print('Output 3', line)

    #replace commas with new line value
    line = line.strip()
    # print('Output 4', line)

    #partition each entry by :
    head, sep, tail = line.partition(':')
    # print('Output 5', line)

    #remove names and stip leading white space
    line2 = tail
    # print('Output 6', line) 

    # split each entry by ,
    list1 =line2.split(',')
    # print('Output 7' ,line2)
    
    the_set.update(list1)

f.close

the_set.remove('languages')
# print(the_set) 
outfile = open("languages.txt","w")

for x in the_set:
    outfile.write ("%s\n" %x)

outfile.close()

