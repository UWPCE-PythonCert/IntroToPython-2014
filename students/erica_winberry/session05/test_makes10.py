from codingbat import makes10

def test_is10():
    assert makes10(9,10)

def test_isnot10():
    assert makes10(9,9) is False

def test_addsto10():
    assert makes10(1, 9)



# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True