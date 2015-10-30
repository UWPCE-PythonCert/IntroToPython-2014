import random


def text_to_trigrams(text):
    text_as_list = text.split()
    trigrams = {}
    for i in range(len(text_as_list)-2):
        k = (text_as_list[i], text_as_list[i+1])
        v = [text_as_list[i+2]]
        if k in trigrams:
            trigrams[k] = trigrams[k] + v
        else:
            trigrams[k] = v
    return trigrams


def trigrams_to_text(trigrams):
    new_text = []
    keys_list = list(trigrams.keys())
    first_key = random.choice(keys_list)

    # maybe there's a simpler way than storing key as a tuple
    # and converting it back to strings here?

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
    # prettify the text here before converting to string?
    new_text = ' '.join(new_text)
    return new_text

# feed it Sherlock

with open('sherlock.txt', 'r') as f:
    sherlock = f.read()

sherlock_trigrams = text_to_trigrams(sherlock)
new_sherlock = trigrams_to_text(sherlock_trigrams)

# my favorite randomly generated sentence so far: "I was ten miles of town,
# chemistry eccentric, anatomy unsystematic, sensational literature and
# crime records unique, violin-player, boxer, swordsman, lawyer, and
# self-poisoner by cocaine and tobacco."
