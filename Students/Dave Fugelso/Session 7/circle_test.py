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
        c = Circle.Circle (3)    
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
        
    def test_alternate_constructor(self):
        c = Circle.Circle.from_diameter(8)
        print c.diameter
        print c.radius
        assert c.diameter == 8
        assert c.radius == 4
        
    def test_repr_and_str_builtins(self):
        c = Circle.Circle(4)
        print c 
        print 'Expected: "Circle with radius: 4.000000"'

        print repr(c)
        print 'Expected: "Circle(4)"'

        d = eval(repr(c))
        print d
        print 'Expected: "Circle(4)"'        
 
    def test_add_and_mul(self):
        c1 = Circle.Circle(2)
        c2 = Circle.Circle(4)
        print c1 + c2
        print 'Expected: "Circle(6)"'
        print c2 * 3
        print 'Expected: "Circle(12)"'
        print 3 * c2
        print 'Expected: "Circle(12)"'
        
    def test_comparisons (self):
        c1 = Circle.Circle(2)
        c2 = Circle.Circle(4)
        c3 = Circle.Circle(4)
        
        assert c1 < c2
        assert not c1 > c3
        assert not c1 == c2
        assert c2 == c3
        
    def test_sort(self):
        circles = [Circle.Circle(6), Circle.Circle(7), Circle.Circle(8), Circle.Circle(4), Circle.Circle(0), Circle.Circle(2), Circle.Circle(3), Circle.Circle(5), Circle.Circle(9), Circle.Circle(1)]
        print circles
        print circles.sort()
    
if __name__ =='__main__':
    unittest.main()
   