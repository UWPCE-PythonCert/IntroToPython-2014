string = open("sherlock.txt", "r").read()
listr = string[1151:3956].replace(",","").replace(".","").split()


trigram_dict = {}
pair = ()
for i in range(len(listr) - 2):
    pair = str(listr[i:i+2])
    follower = listr[i+2]
    if pair in trigram_dict:
        #print("found")
        trigram_dict[pair] = trigram_dict.get(pair) + follower + " "
        #continue
    else:
        trigram_dict[pair] = follower + " "
    #for i in trigram_dict:
        #print(i)
        #print(pair)
        #if i == pair:
            #trigram_dict[i] = follower





    #trigram_dict.append(list((tuple(pair),follower)))

#for i in trigram_dict:
#    print(trigram_dict.get(i))
for keys, values in trigram_dict.items():
    print(keys, " => ", values)
#print(trigram_dict.items())
#for i in trigram_dict:
    #print(i[0])
    #print(" ".join(i[0]), " => ", i[1:])