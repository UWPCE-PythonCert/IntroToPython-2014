__author__ = 'Ari'

from ack import ackerman
import unittest

# Note to Chris: So, I was experimenting with classes
# and I've had this problem in the past where I try to run
# test_somefunction and I get "You have 3 arguments, only need 2"
# I'd really like to understand why this is (I can surmise it
# is about the 'self'). Also what is 'unittest.TestCase'??

class test_ackerman(unittest.TestCase):

    def test_ack(self):
        # coordinates 0,0
        test_func = ackerman()
        m = 0
        n = 0
        result = test_func.ack(m,n)
        assert_equal(result,1)

    def test_ack(self):
        # coordinates 0,1
        test_func = ackerman()
        result = test_func.ack(0,1)
        assert_equal(result, 2)

    def test_ack(self):
        # coordinates 1,2
        test_func = ackerman()
        result = test_func.ack(1,2)
        assert_equal(result, 4)

    def test_ack(self):
        # coordinates 2,2
        test_func = ackerman()
        result = test_func.ack(2,2)
        assert_equal(result,7)

    def test_ack(self):
        # coordinates 2,3
        test_func = ackerman()
        result = test_func.ack(2,3)
        assert_equal(result,9)

    def test_ack(self):
        # coordinates 1,4
        test_func = ackerman()
        result = test_func.ack(1,4)
        assert_equal(result, 6)





