# This module should provide at least one function called rot13 that takes
# any amount of text and returns that same text encrypted by ROT13.

# This function should preserve whitespace, punctuation and capitalization.



# There is a “short-cut” available that will help you accomplish this task.
# Some spelunking in the documentation for strings should help you to find it.
# If you do find it, using it is completely fair game.

# As usual, add your new file to your local clone right away.
# Make commits early and often and include commit messages that are descriptive and concise.



def rot13_translate(l):
    base_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plus13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    switcher = str.maketrans(base_alpha, plus13)
    new = l.translate(switcher)
    print(new)

def rot13_encode(l):
    base_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    plus13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    switcher = str.maketrans(plus13, base_alpha)
    new = l.translate(switcher)
    print(new)


# Your module should include an if __name__ == '__main__': block with tests (asserts)
# that demonstrate that your rot13 function and any helper functions you add work properly.

if __name__ == "__main__":
    assert rot13_translate("A") == "N"
    assert rot13_translate("a") == "n"
    assert rot13_encode("N") == "A"
    assert rot13_encode("n") == "a"
    assert rot13_translate("Zntargvp sebz bhgfvqr arne pbeare") == "Magnetic from outside near corner"