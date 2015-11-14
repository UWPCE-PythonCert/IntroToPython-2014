__author__ = 'Max'

def main():
    filesLab()

def filesLab():
    with open('C:/Users/Max/Documents/workspace/Python/IntroPython2015/Examples/students.txt', 'r') as f:
        lines = f.readline(); # Skip the first line

        # Create a dictionary of all the languages that have been
        # used with the number of occurrences.
        d = dict()

        for lines in f:
            #lines = lines.upper().strip(",")
            #print(lines)
            lines.translate(",") #Remove all commas
            lines = lines.replace('\n', "") # Remove all newlines
            lines = lines.split(": ") # Split the colon delineated name from the languages
            #lines = lines.split(" ")
            lines = lines[1:].split(" ")
            print(lines)

            for language in lines:
                # Add language to dictionary.
                if language in d.values():
                    d[language] = d[language] + 1
                else:
                    d[language] = 0

        for items in d.keys():
            print("{lang} {count}".format(lang=items, count=d[items]))

main()