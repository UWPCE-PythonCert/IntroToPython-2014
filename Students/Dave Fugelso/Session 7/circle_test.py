'''
These are all the unit test to make sure circle works as expected.

Really taking these seriously as feedback from last homework assignment indicated I should.
I skipped the unit tests and did step tests. Not this time!
'''

import Circle
import unittest
import math

class TestCircleClass (unittest.TestCase): # note didn't save class notes. Wrote this first!

    def test_create_circle(self): 
        # First test, instantiate the circle class 
        c = Circle.Circle (3.)    # note working ahead. I know this need to be a float. Will enforce in class __init__
        print c.radius
        
    def test_get_diameter(self):
        c = Circle.Circle (3.)    # Test fetching diameter
        print c.diameter

    def test_set_diameter(self):
        c = Circle.Circle (3.)    # Test setting diameter
        c.diameter = 7
        print c.diameter
        assert c.diameter == 7.
        assert c.radius == 3.5
        
    def test_area (self):
        c = Circle.Circle (3.)
        print c.area()
        assert c.area() ==  math.pi * 9.
        
    
if __name__ =='__main__':
    unittest.main()
   