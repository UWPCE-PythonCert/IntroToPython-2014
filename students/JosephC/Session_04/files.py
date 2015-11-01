#Files lab

"""
Write a little script that reads the students.txt file, and generates a list of all the languages that have been used.
"""
#   open the file 'students.txt'
f = open('students.txt')

#   iterate though the text file to see and print languages
#   the languages are in the 'languages' column of the file, if that matters

languages = dict()
line = f.readline()
while True:
    line = f.readline()
    if not line:
        break
    line = line.replace(',', ' ')
    line = line.replace('and', ' ')
      
    Line2 = line.split(':')[1] 
    Line3 = Line2.split()
    print(Line3)
    
    
    for lang in Line3:
        lang = lang.capitalize()
        if lang in languages:
            languages[lang] += 1
        else:
            languages[lang] = 1
        
print(languages)
    
    
