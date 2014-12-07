'''
Test timer context manager.
'''

from timer import * 

def test_timer():
    print 'test'
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
    print t.elapsed_time()
    assert t.elapsed_time() > 0
    
test_timer()