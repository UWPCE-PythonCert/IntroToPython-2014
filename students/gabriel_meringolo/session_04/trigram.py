string = open("sherlock.txt", "r").read()
listr = string[1151:3956].replace(",","").replace(".","").split()


trigram_dict = {}
pair = ()
for i in range(len(listr) - 2):
    pair = str(listr[i:i+2])
    follower = listr[i+2]
    if pair in trigram_dict:
        trigram_dict[pair] = trigram_dict.get(pair) + follower + " "
    else:
        trigram_dict[pair] = follower + " "

for keys, values in trigram_dict.items():
    print(keys.replace("'","").replace("[","").replace("]","").replace(",",""), " => ", values)
