


def rot13(text_to_trans):
    one = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    another = "nNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmM"
    transtab = str.maketrans(one, another)
    return text_to_trans.translate(transtab)

if __name__ == "__main__":
    print("main")
    assert rot13("a") == "n"
    assert rot13("A") == "N"



print(rot13("abcdefghijklmnopqrstovwxyz"))