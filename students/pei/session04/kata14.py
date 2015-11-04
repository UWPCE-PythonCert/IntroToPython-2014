txt = open('sherlocksmall.txt')
txt_data = txt.read().replace("\n", " ").strip().split(' ')
#txt_data = txt.read()
#grab the first 3, put them in the list, increment by 1 and grab the next 3
#to create a dictionary
grouping1 =[ ]
grouping2 ={ } 
for n in range(len(txt_data)-2):
    del grouping1 [:]
    grouping1.append(txt_data[n] + " " + txt_data[n+1])
    grouping1.append(txt_data[n+2]) 
    #print (grouping1[0])
    if grouping1[0] not in grouping2:
        #grouping2[(grouplist1[0])] = (grouping1[1]) 
        grouping2[grouping1[0]] = [grouping1[1]]
    else:
        grouping2[grouping1[0]].append(grouping1[1])

print (grouping2)

#generate new sentance using the dict
#def generate (strText):
import random
new = "he was"
strLastTwo = new
#strLastTwo in grouping2
while strLastTwo in grouping2:
    strLastTwo = ' '.join(new.split()[-2:])
    try: 
        new += " " + ''.join(random.choice(grouping2.get(strLastTwo)))
    except TypeError:
        print(new)
#else:
    #print (new)
    #break

txt.close()

"""
Result
he was employing his extraordinary powers. 
His rooms were brilliantly lit, and, even as I looked up, 
I saw his tall, spare figure pass twice in a dark silhouette 
against the blind. He was pacing the room swiftly, eagerly, 
with his head sunk upon his chest and his hands clasped behind him. 
To me, who knew his every mood and habit, 
his attitude and manner told their own story. 
He was at work again. He had risen out of his drug-created dreams 
and was hot upon the scent of some new problem. 
I rang the bell and was shown up to the chamber which had formerly 
been in part my own.
"""





