import random

txt = open('sherlocksmall.txt')
txt_data = txt.read().split()
txt.close()

#txt_data = txt.read()
#grab the first 3, put them in the list, increment by 1 and grab the next 3
#to create a dictionary
# grouping1 =[]
trigrams = {}
for n in range(len(txt_data)-2):
    pair = " ".join(txt_data[n:n+2])
    following_word = txt_data[n+2]
    trigrams.setdefault(pair, []).append(following_word)

print (trigrams)


#generate new sentance using the dict
#def generate (strText):
new = "he was"
word_pair = new
#strLastTwo in trigrams
new_text = []
new_text.extend(word_pair.split())
for i in range(100):
    try:
        following_word = random.choice(trigrams[word_pair])
    except KeyError:
        word_pair = random.choice(list(trigrams.keys()))
        continue
    new_text.append(following_word)
    word_pair = " ".join(new_text[-2:])
print(" ".join(new_text))

    # strLastTwo = ' '.join(new.split()[-2:])
    # try:
    #     new += " " + ''.join(random.choice(trigrams.get(strLastTwo)))
    # except TypeError:
    #     print(new)
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

