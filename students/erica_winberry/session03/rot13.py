# This module should provide at least one function called rot13 that takes 
# any amount of text and returns that same text encrypted by ROT13.

# This function should preserve whitespace, punctuation and capitalization.

# Your module should include an if __name__ == '__main__': block with tests (asserts) 
# that demonstrate that your rot13 function and any helper functions you add work properly.

# There is a “short-cut” available that will help you accomplish this task.
# Some spelunking in the documentation for strings should help you to find it.
# If you do find it, using it is completely fair game.

# As usual, add your new file to your local clone right away. 
# Make commits early and often and include commit messages that are descriptive and concise.

def translator(l):
    for i in l:
        if i.isalpha:
            i = translate_letter(i)
            return i
        else:
            return i

def translate_letter(l):
    base_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plus13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    switcher = str.maketrans(base_alpha, plus13)
    new = l.translate(switcher)
    print(new)


#if name == __main__:
#    for i in l:
#        assert not i.isnumeric()

# OR
    # take a letter, get the ordinal of that letter.
    # add 13 to the oridinal of that letter.
    # return the character of the new letter.