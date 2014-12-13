__author__ = 'asimmons'

from simplify_topology import *
from nose.tools import *
import unittest


## Test to Identify Junctions - Shared points where two or more lines intersect
class test_PreserveTopology(unittest.TestCase):

    """
    cases to cover:
    1) one line - no junctions
    2) two lines - no junctions
    3) two lines - with junctions
    4) two lines that cross, but do not share a point - no junctions.
    5) two lines that are identical, and on top of each other, but
       because the neighbors are the same - no junctions.
    """

    ##      A
    ##       \
    ##        \
    ##         X
    ##          \
    ##           \
    ##            D

    def test_one_line_no_junction_append_junctions(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # Line AXD
        array = [(1,3),(1.4,2),(2,0)]
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        assert(not test_dictJunctions ==True) # test that test_dictJunctions is empty
        assert(not test_dictNeighbors ==True) # test that test_dictNeighbors is empty

    ##      A
    ##       \
    ##        \
    ##         X
    ##
    ##
    ## B-----C

    def test_two_lines_no_junctions_append_junctions(self):

        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE BC & AX
        array = [(0,0),(1,0)]
        array2 = [(1,3),(1.4,2)]
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        assert(not test_dictJunctions ==True) # test that test_dictJunctions is empty
        assert(not test_dictNeighbors ==True) # test that test_dictNeighbors is empty

    ##      A
    ##       \
    ##        \
    ##         X
    ##          \
    ##           \
    ## B-----C-----D-----F

    def test_two_lines_one_junction(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE BCDF & AXD
        array = [(0,0),(1,0),(2,0),(3,0)]
        array2 = [(1,3),(1.4,2),(2,0)]
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        assert test_dictJunctions == {(2,0): 1}

    ##
    ##            X
    ##          /
    ##        /
    ## B-----C-----D-----F
    ##     /
    ##   Y

    def test_two_lines_cross_but_do_not_intersect_no_junctions(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # these lines do NOT have a junction because there is no shared point
        # LINE BCDF
        array = [(0,0),(1,0),(2,0),(3,0)]
        # LINE XY
        array2 = [(3,3),(-1,.5)]
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        assert(not test_dictJunctions ==True) # test that test_dictJunctions is empty
        assert(not test_dictNeighbors ==True) # test that test_dictNeighbors is empty


    def test_quantitize(self):
        g = PreserveTopology()
        result = g.quantitize((12345,12345))
        assert_equal(result,(10000, 10000))


if __name__ == "__main__":
    unittest.main()