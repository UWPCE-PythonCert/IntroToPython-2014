import random
import textwrap

string = open("sherlock.txt", "r").read()

listr = string[1151:-2938].replace('"', "").replace("(", "").replace(")", "").split()

trigram_dict = {}

for i in range(len(listr) - 2):
    pair = tuple(listr[i:i+2]) #str(listr[i:i+2])
    follower = listr[i+2]
    if pair in trigram_dict:
        trigram_dict[pair] = trigram_dict.get(pair) + follower + " "
    else:
        trigram_dict[pair] = follower + " "

new_story = []
start_pair = random.choice(list(trigram_dict.keys())) # get random key pair and start a new story..

new_story.extend(start_pair)

for i in range(300):
    new_story.append(random.choice(trigram_dict.get(start_pair).split()))
    start_pair = tuple(new_story[-2:])
new_book = " ".join(new_story).capitalize()
print(textwrap.fill(new_book, 70), end= ".")

