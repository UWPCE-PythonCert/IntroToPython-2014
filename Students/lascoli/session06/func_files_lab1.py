
"Removing leading and trailing whitespaces "
user_input1 =raw_input('Please provide the file name of the target input file in the local directory :\n\n')
f = open('%s'%user_input1)
f.readline()

outfile_data = map(str.strip,f) 


user_input2 =raw_input('Please output file name:\n\n')
while True:
    if user_input2 == user_input1:
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
