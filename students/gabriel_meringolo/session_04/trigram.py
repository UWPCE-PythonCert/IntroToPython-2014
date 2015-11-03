import random

string = open("sherlock.txt", "r")
for i in range(random.randint(20,1000)):
    string.readline()

listr = string.read().replace(",","").replace('"',"").replace(".","").split()


trigram_dict = {}
pair = ()

for i in range(len(listr) - 2):
     pair = str(listr[i:i+2])
     follower = listr[i+2]
     if pair in trigram_dict:
         trigram_dict[pair] = trigram_dict.get(pair) + follower + " "
     if pair not in trigram_dict:
         trigram_dict[pair] = follower + " "
     if len(trigram_dict) == 101:
         break



for keys, values in trigram_dict.items():
    print(keys.replace("'","").replace("[","").replace("]","").replace(",",""), " => ", values)
