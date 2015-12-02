from string_times import string_times

def test1():
    assert(string_times('Hi',2)) == "HiHi"
    
def test2():
    assert(string_times('Hi',3)) == "HiHiHi" 

def test3():
    assert(string_times('Hi', 0)) == ""