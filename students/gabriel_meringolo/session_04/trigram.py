string = open("sherlock.txt", "r").read() # opened txt file as file object
listr = string[:100].split()
start = 0
for words in listr:
    while start < len(listr) - 2:
        print(listr[start], listr[start + 1], " => ", listr[start + 2])
        start += 1