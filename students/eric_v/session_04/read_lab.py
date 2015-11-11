f = open('../../../Examples/students.txt', "r")
line = f.readline()
program_list = []
while line:

# Separate  programs from student name
    if(line.split(": ")):
        file_strings = line.split(": ")
        print('\n\n',file_strings)
        if(len(file_strings) > 1):
            file_programs = file_strings[1]
        else:
            file_programs = "null_string\n"
# Trim off newline from end of string
    file_programs_trimmed = file_programs[:-1]

# Split each program into its own string
    program_strings = file_programs_trimmed.split(" ")
    print(program_strings)

# Iterate over list of programs for each student and if a new program add to total list
    for individual_programs in program_strings:
        print (individual_programs)
        if (individual_programs != "languages" and individual_programs != "null_string" and individual_programs != ''):
            if (individual_programs not in program_list):
                program_list.append(individual_programs)

# Move to next line
    line = f.readline()

#Close file
f.closed

# Print final list of programs
print (program_list)