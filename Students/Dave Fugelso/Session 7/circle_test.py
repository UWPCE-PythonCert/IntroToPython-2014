'''
These are all the unit test to make sure circle works as expected.

Really taking these seriously as feedback from last homework assignment indicated I should.
I skipped the unit tests and did step tests. Not this time!
'''

# First test, instantiate the circle class 
import Circle
def test_circle(): # note didn't save class notes. Wrote this first!
    c = Circle (3.)    # note working ahead. I know this need to be a float. Will enforce in class __init__
    print c.radius

    
test_circle()