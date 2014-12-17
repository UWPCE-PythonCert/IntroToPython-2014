__author__ = 'asimmons'

from simplify_topology import *
from nose.tools import *
import unittest


class test_PreserveTopology(unittest.TestCase):

    """
    Test append_junctions:

    cases to cover:
    1) one line - no junctions
    2) two lines - no junctions
    3) two lines - with junctions
    4) two lines that cross, but do not share a point - no junctions.
    5) two lines that are identical, and on top of each other, but
       because the neighbors are the same - no junctions.

    Test cut_line_by_junctions:

    cases to cover:
    1) one line with a junction in the middle of the line - split into 2 arcs
    2) one line with a junction at the start of the line - 1 arc
    3) one line with a junction at the end of the line - 1 arc
    4) one line with no junctions - 1 arc

    Test quantitize:

    cases to cover:
    1) check if default quantization factor is 10,000 (-q 1e4)
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

    ##        C and X
    ##          /
    ##        /
    ##    B and Y
    ##     /
    ##  A and Z

    def test_two_identical_lines_do_not_have_any_junctions(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # these lines do NOT have a junction because there are no different neighbors
        # LINE ABC
        array = [(3,3),(1,0),(-1,.5)]
        # LINE ZYX
        array2 = [(3,3),(1,0),(-1,.5)]
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
    ##              \
    ##               R

    def test_splitting_lines_2_arcs(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE BCDF & AXDR
        array = [(0,0),(1,0),(2,0),(3,0)]
        array2 = [(1,3),(1.4,2),(2,0),(-1.4,3)]
        # create LINE AXDR as shapely obj
        array2_as_linestring = LineString(array2)
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        # test_dictJunctions == {(2,0): 1}
        # For LINE AXDR if I run cut_line_by_junctions
        # there should now be two LineString obj's
        # LINE AXD & DR
        # which are represented as two lists seperated by a
        # comma
        arcArray2 = g.cut_line_by_junctions(array2_as_linestring, test_dictJunctions)
        result = list([list(i.coords) for i in arcArray2])
        assert result == [[(1,3),(1.4,2),(2,0)],[(2,0),(-1.4,3)]]

    ##  X
    ##  |
    ##  |
    ##  |
    ##  |
    ##  |
    ##  B-----C-----D-----F
    ##

    def test_splitting_line_w_junction_at_start_1_arc(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE XB & BCDF
        array1 = [(0,0),(0,5)]
        array2 = [(0,0),(1,0),(2,0),(3,0)]
        # create LINE BCDF as shapely obj
        array2_as_linestring = LineString(array2)
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array1)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        # test_dictJunctions == {(0,0): 1}
        # For LINE BCDF if I run cut_line_by_junctions
        # there should now be 1 LineString obj's
        # LINE BCDF
        arcArray2 = g.cut_line_by_junctions(array2_as_linestring, test_dictJunctions)
        result = list([list(i.coords) for i in arcArray2])
        assert result == [[(0,0),(1,0),(2,0),(3,0)]]

    ##                    X
    ##                    |
    ##                    |
    ##                    |
    ##                    |
    ##                    |
    ##  B-----C-----D-----F
    ##

    def test_splitting_line_w_junction_at_end_1_arc(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE XF & BCDF
        array1 = [(3,0),(3,5)]
        array2 = [(0,0),(1,0),(2,0),(3,0)]
        # create LINE BCDF as shapely obj
        array2_as_linestring = LineString(array2)
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array1)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array2)
        # test_dictJunctions == {(3,0): 1}
        # For LINE BCDF if I run cut_line_by_junctions
        # there should now be 1 LineString obj's
        # LINE BCDF
        arcArray2 = g.cut_line_by_junctions(array2_as_linestring, test_dictJunctions)
        result = list([list(i.coords) for i in arcArray2])
        assert result == [[(0,0),(1,0),(2,0),(3,0)]]


    ##             C
    ##           /
    ##         /
    ##       B
    ##     /
    ##   A

    def test_one_line_one_arc(self):
        g = PreserveTopology()
        # set the quantitization factor
        g.set_quantitization_factor(1)
        # LINE ABC
        array = [(3,3),(1,0),(-1,.5)]
        # create LINE ABC as shapely obj
        array_as_linestring = LineString(array)
        # create global dictionary
        test_dictJunctions = {}
        test_dictNeighbors = {}
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        g.append_junctions(test_dictJunctions,test_dictNeighbors,array)
        # Create one arc from the junctionless LINE ABC
        arcArray = g.cut_line_by_junctions(array_as_linestring, test_dictJunctions)
        result = list([list(i.coords) for i in arcArray])
        assert result == [[(3,3),(1,0),(-1,.5)]]

    def test_quantitize(self):
        g = PreserveTopology()
        result = g.quantitize((12345,12345))
        assert_equal(result,(10000, 10000))

if __name__ == "__main__":
    unittest.main()