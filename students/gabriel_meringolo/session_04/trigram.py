string = open("sherlock.txt", "r").read() # opened txt file as file object
listr = string[1151:3550].replace(",","").replace(".","").split()
#start = 0
#for words in listr:
#    while start < len(listr) - 2:
#        print(str(listr[start]), str(listr[start + 1]), " => ", listr[start + 2])
#        start += 1
#print(listr)


trigram_list = [] # this is the list of trigrams
pair = () # these are the pair of words
for i in range(len(listr) - 2): #this is going through list
    #trigram = []
    pair = listr[i:i+2] # making pairs and followers
    follower = listr[i+2]
    #print(trigram_list[0])
    #print(i, pair, follower)
    for i in trigram_list: # i is each trigram in the list
        if i[0] != tuple(pair):
            trigram = []
            trigram.append((tuple(pair),follower))
        print(trigram)
        #elif i[0] == tuple(pair): # i[0] is the pairs in the list checking against new pairs
            #print(tuple(pair))
        #    i.append(follower) # if the same appending the existing trigram

            #print(i)

            #print(i[0], "here")
            #print("same")     # isolating matching pairs!!! need to append to the match figure it out!!!
    #print(pair)


    trigram_list.append(list((tuple(pair),follower)))


#for i in trigram_list:
 #   print(i)
#print(trigram)
#for i in trigram:
#    print(i)
    # print(trigram[0][0])
#for i in trigram:
#    print(" ".join(i[0]), " => ", i[1:])
#for i in trigram:
 #   print(pair)
#print(pair)
#for i in trigram:

#for i in trigram:
#    print(i[0])
#for i in trigram:
#    print(trigram[i], " => ", trigram[i + 1])
#for i in trigram:
#    print





#    trigram_list.append(list((tuple(listr[i:i+2]),listr[i+2])))
#for i in trigram_list:
#    print(i)