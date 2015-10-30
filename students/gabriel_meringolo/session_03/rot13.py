


def rot13(i):
    one = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    another = "nNoOpPqQrRsStTuUvVwWxXyYzZaAbBcCdDeEfFgGhHiIjJkKlLmM"
    transtab = str.maketrans(one, another)
    print(i.translate(transtab))

if __name__ == "__main__":
    print("main")
    assert rot13("a") == "n"
    assert rot13("A") == "N"



rot13("abcdefghijklmnopqrstovwxyz")