
"Removing leading and trailing whitespaces "
import sys
filename = sys.argv[1]
f = open(filename)
f.readline()

outfile_data = [x.strip() for x in f]



user_input2 =raw_input('Please specify the output file name:\n\n')
while True:
    if user_input2 == sys.argv[1]:
        user_input3 =raw_input('Do you want to overwrite an existing file, please answer "yes" or "no"\n\n')
        if user_input3 == 'yes':
            outfile_name = user_input2
            print("overwriting %s"%user_input2)
            print (user_input2)
            break

        elif user_input3 == 'no':
            user_input2 =raw_input('Please choose a new output file name:\n\n')
            outfile_name = user_input2
            print (user_input2)
            break
        continue
            
    
    outfile_name = user_input2
    break

f.close()

outfile = open("%s"%outfile_name,"w")

for x in outfile_data:
    outfile.write ("%s\n" %x)

outfile.close()
