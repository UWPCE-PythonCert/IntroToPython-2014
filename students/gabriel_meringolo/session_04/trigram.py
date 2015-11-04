import random

string = open("sherlock.txt", "r").read()
#for i in range(random.randint(20, 1000)):
#    string.readline()

listr = string[1151:-2938].replace('"', "").split()

trigram_dict = {}
pair = ()

for i in range(len(listr) - 2):
    pair = str(listr[i:i+2]) #str(listr[i:i+2])
    #print(pair)
    #print(type(pair))
    #raise Exception
    follower = listr[i+2]
    if pair in trigram_dict:
        trigram_dict[pair] = trigram_dict.get(pair) + follower + " "
    if pair not in trigram_dict:
        trigram_dict[pair] = follower + " "
    #if len(trigram_dict) == 200:
    #    break

#for keys, values in trigram_dict.items():
#    print(keys.replace("'", "").replace("[", "").replace("]", "").replace(",", ""), " => ", values)


new_story = []
start_pair = random.choice(list(trigram_dict.keys())) # get random key pair and start a new story..

print(start_pair)
#print((" ".join(start_pair.split())))
#new_story.append(start_pair.split())
#print(new_story)
#for i in range(250):

