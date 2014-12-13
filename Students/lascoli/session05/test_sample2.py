def makes10(a, b):
    if a==10 or b==10 or a+b==10:
        return True
    else:
        return False

def test_answer():
    assert makes10(9,10) == True
    assert makes10(9,9) == False
    assert makes10(1,9) == True