string = open("sherlock.txt", "r").read()
listr = string[1151:3956].replace(",","").replace(".","").split()


trigram_list = []
pair = ()
for i in range(len(listr) - 2):
    pair = listr[i:i+2]
    follower = listr[i+2]
    for i in trigram_list:
        if i[0] == tuple(pair):
            i.append(follower)



    trigram_list.append(list((tuple(pair),follower)))


for i in trigram_list:
    print(" ".join(i[0]), " => ", i[1:])