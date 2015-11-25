from first_last6 import first_last6

def test1():
    assert(first_last6([1,2,6])) == True

def test2():
    assert(first_last6([6,1,2,6])) == True

def test3():
    assert(first_last6([2,6,1,2,6,8])) == False