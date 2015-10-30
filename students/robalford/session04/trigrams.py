import random

# create the program from the example


def text_to_trigrams(text):
    wish_list = text.split()
    trigrams = {}
    for i in range(len(wish_list)-2):
        k = (wish_list[i], wish_list[i+1])
        v = [wish_list[i+2]]
        if k in trigrams:
            trigrams[k] = trigrams[k] + v
        else:
            trigrams[k] = v
    return trigrams

text = 'I wish I may I wish I might'
wishes = text_to_trigrams(text)


def trigrams_to_text(trigrams):
    new_text = []
    keys_list = list(trigrams.keys())
    first_key = random.choice(keys_list)

    # maybe there's a simpler way than storing key as a tuple
    # and converting it here?

    new_text.append(str(first_key[0]))
    new_text.append(str(first_key[1]))
    new_text.append(random.choice(trigrams[first_key]))

    next_pair = (new_text[-2], new_text[-1])

    while next_pair in keys_list:
        if len(new_text) >= 200:
            break
        else:
            new_text.append(random.choice(trigrams[next_pair]))
            next_pair = (new_text[-2], new_text[-1])
    new_text = ' '.join(new_text)
    new_text.replace('\\', '')
    return new_text

new_text = trigrams_to_text(wishes)

# feed it Sherlock

with open('sherlock.txt', 'r') as f:
    sherlock = f.read()

sherlock_trigrams = text_to_trigrams(sherlock)
new_sherlock = trigrams_to_text(sherlock_trigrams)

# my favorite randomly generated sentence so far: "I was ten miles of town,
# chemistry eccentric, anatomy unsystematic, sensational literature and
# crime records unique, violin-player, boxer, swordsman, lawyer, and self-poisoner
# by cocaine and tobacco."




# for k, v in wishes.items():
#     new_text.append(k)
#     new_text.append(random.choice(v))


# import random

# trigrams = {}
# sherlock = []
# new_text = []
# f = open('sherlock.txt')
# for line in f:
#     for word in line.split():
#         sherlock.append(word)

# for i in range(len(sherlock)-3):
#     k = str(sherlock[i] + ' ' + sherlock[i+1])
#     # k = str(k.split(', '))
#     v = [sherlock[i+2]]
#     if k in trigrams:
#         trigrams[k] = trigrams[k] + v
#     else:
#         trigrams[k] = v

# just check if it's not a letter instead of this
# end_sentence = ['.', '!', '?']


# for trigram in trigrams:
#     if trigram[0][0].istitle():
#         new_text.append(trigram[0] + ' ' + random.choice(trigram[1]))

# def add_trigram():
#     new_text.append(trigram[0] + ' ' + random.choice(trigram[1]))


# trigram = trigrams.popitem()
# if not new_text and trigram[0][0].istitle():
#     add_trigram()
# for trigram in trigrams:
#     if new_text[-2:-1] == trigram:
#         pass
# for i in range(100):
#     if new_text and new_text[-1].islower and trigram[0][0].islower():
#         add_trigram()
#     if new_text and new_text[-1][-1] in end_sentence and trigram[0][0].istitle:
#         add_trigram()



