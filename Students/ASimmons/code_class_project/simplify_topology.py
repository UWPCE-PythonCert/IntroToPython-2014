__author__ = 'asimmons'


import fiona
from shapely.geometry import shape, mapping, LineString, Polygon, MultiLineString, MultiPolygon
import heapq
import sys

# Note: to change the quantitization from the default, you will have to do it before running process file

# Linestring test:
# g = PreserveTopology();g.process_file(r'I:\It_23\simplify\test_lines_simplify_topology\sample_lines.shp',r'I:\It_23\simplify\test_lines_simplify_topology\simplified_sample.shp', 1000000, True)

# Multilinestring test:
#  g = PreserveTopology();g.process_file(r'I:\It_23\simplify\test_multi\four_lines_dis.shp', r'I:\It_23\simplify\test_multi\four_lines_test_simp.shp', 1000000, True)


class TriangleCalculator(object):
    """
    TriangleCalculator() - Calculates the area of a triangle using the cross-product.

    """
    def __init__(self, point, index):
        # Save instance variables
        self.point = point
        self.ringIndex = index
        self.prevTriangle = None
        self.nextTriangle = None

    # enables the instantiation of 'TriangleCalculator' to be compared
    # by the calcArea().
    def __cmp__(self, other):
        return cmp(self.calcArea(), other.calcArea())

    ## calculate the effective area of a triangle given
    ## its vertices -- using the cross product
    def calcArea(self):
        # Add validation
        if not self.prevTriangle or not self.nextTriangle:
            print "ERROR:"

        p1 = self.point
        p2 = self.prevTriangle.point
        p3 = self.nextTriangle.point
        area = abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0
        #print "area = " + str(area) + ", point = " + str(self.point)
        return area


class PreserveTopology(object):

    quantitizationFactor = (10000,10000)

    def set_quantitization_factor(self, quantValue):
        self.quantitizationFactor = (quantValue, quantValue)

    def process_file(self, inFile, outFile, threshold, Topology = False):
        """
        Takes an 'inFile' of an ESRI shapefile, converts it into a Shapely geometry - simplifies.
        Returns an 'outFile' of a simplified ESRI shapefile.

        IF Topology = True
        The object to be simplified is cut into junctions.

        IF Topology = False
        The object is simplified as is.

        Note:
        - A point is considered a junction if it shares the same point
        with another shape AND has different neighbors.

        - Identical features on top of one another DO NOT have different
        neighbors, and therefor DO NOT have any junctions.

        """
        # declare dictJunctions as a global variable
        # key = quantitized junction points, value = 1
        dictJunctions = {}

        # create an instance of GeomSimplify()

        simplify = GeomSimplify()

        # Open input file
        # loop over each
        with fiona.open(inFile, 'r') as input:

            meta = input.meta

            # create dictionary of all junctions in all shapes
            self.find_all_junctions(inFile, dictJunctions)

            # create an outFile has the same crs, schema as inFile
            with fiona.open(outFile, 'w', **meta) as output:
            # Read shapely geometries from file
            # Loop through all shapely objects
                for myGeom in input:

                    myShape = shape(myGeom['geometry'])

                    if isinstance(myShape, LineString):
                        if Topology is True:
                            simplifiedShapes = []
                            lineList = self.cut_line_by_junctions(myShape, dictJunctions)
                            for line in lineList:
                                simplifiedShapes.append(simplify.simplify_line(line, threshold))
                        else:
                            line = myShape
                            simplifiedShapes = [simplify.simplify_line(line, threshold)]

                    elif isinstance(myShape, MultiLineString):
                        if Topology is True:
                            simplifiedShapes =[]
                            # mlineArray array of MultiLineString
                            mlineArray = self.cut_mline_by_junctions(myShape, dictJunctions)
                            #mline = MultiLineString shapely obj
                            for mline in mlineArray:
                                simplifiedShapes.append(simplify.simplify_multiline(mline, threshold))
                        else:
                            mline = myShape
                            simplifiedShapes = [simplify.simplify_multiline(mline, threshold)]
                    else:
                        raise ValueError('Unhandled geometry type: ' + repr(myShape.type))


                    # write to outfile
                    for simpleShape in simplifiedShapes:
                        if simpleShape is not None:
                            output.write({'geometry':mapping(simpleShape), 'properties': myGeom['properties']})

    def quantitize(self, point):
        # the default quantization factor is 10,000 (-q 1e4)
        # Divide by quantitiztion factor, round(int), multiply by quantitization factor
        x_quantitized = int(round(point[0]/self.quantitizationFactor[0]) * self.quantitizationFactor[0])
        y_quantitized = int(round(point[1]/self.quantitizationFactor[1]) * self.quantitizationFactor[1])

        return (x_quantitized,y_quantitized)

    def append_junctions(self, dictJunctions, dictNeighbors, pointsList):

        """

        Builds a global dictionary of all the junctions and neighbors found in a
        single geometry within a shapefile. It determines if a point is a junction based on if it shares the same
        point AND has different neighbors.

        """
        # updates dictJunctions & dictNeighbors
        for index, point in enumerate(pointsList):
            quant_point = self.quantitize(point)
            quant_neighbors = []
            # append the previous neighbor
            if index - 1 > 0:
                quant_neighbors.append(self.quantitize(pointsList[index - 1]))
            # append the next neighbor
            if index + 1 < len(pointsList):
                quant_neighbors.append(self.quantitize(pointsList[index + 1]))

            # check if point is in dictNeighbors, if it is
            # check if the neighbors are equivalent to what
            # is already in there, if not equiv. append to
            # dictJunctions

            if quant_point in dictNeighbors:
                # check if neighbors are equivalent
                if set(dictNeighbors[quant_point]) != set(quant_neighbors):
                    dictJunctions[quant_point] = 1
            else:
                # Otherwise, add to neighbors
                dictNeighbors[quant_point] = quant_neighbors

    def find_all_junctions(self, inFile, dictJunctions):

        """

        Builds a global dictionary of all the junctions and neighbors found in a shapefile.

        """

        # declare dictNeighbors as a global
        # key = checked quantitized points, value = array of quantitized neighbors
        dictNeighbors = {}

        # loop over each

        with fiona.open(inFile, 'r') as input:

            # read shapely geometries from file

            for myGeom in input:

                myShape = shape(myGeom['geometry'])

                if isinstance(myShape, LineString):
                    myShape = self.find_junctions_line(myShape, dictJunctions, dictNeighbors)

                elif isinstance(myShape, MultiLineString):
                    myShape = self.find_junctions_mline(myShape, dictJunctions, dictNeighbors)

                else:
                    raise ValueError('Unhandled geometry type: ' + repr(myShape.type))


    def find_junctions_line(self, myShape, dictJunctions, dictNeighbors):

        pointsLineList = list(myShape.coords)

        self.append_junctions(dictJunctions, dictNeighbors, pointsLineList)


    def find_junctions_mline(self, myShape, dictJunctions, dictNeighbors):

        lineList = myShape.geoms

        for line in lineList:
            pointsLineList = list(line.coords)
            self.append_junctions(dictJunctions, dictNeighbors, pointsLineList)


    def cut_line_by_junctions(self, myShape, dictJunctions):

        """
        Returns Arcs from LineStrings.

        AN arc is a LineString between two junctions (note: junctions are end/start points & cannot be simplified)
        IF a LineString has no found junctions then it is written as is into a list of lists.

        Returns 'arcs', LineString objects. By definiton a linestrings must have at least 2 points.

        arcs = List of list (all of the [arc]'s found in a single line segment)

        arc = a single arc being built from a linestring (arc ends when a junction is found)

        """

        arcs = []

        arc = []

        pointsLineList = list(myShape.coords)
        # split lines into arcs by junctions
        for point in pointsLineList:
            # quantitize the point
            # self.quantitize(point)
            quant_pt = self.quantitize(point)
            # add the point to the 'arc' list till a
            # junction point is identified
            arc.append(point)
            length_of_arc = len(arc)
            #print length_of_arc
            if quant_pt in dictJunctions and length_of_arc >= 2:
                # if the junction is in the
                # list add to arcs
                arcs.append(arc)
                arc = [point]
        # make sure you have at least 2 pt for line
        # also ensures that if the starting point
        # of a line is a junction the line
        # cannot be cut there (because it would be an invalid line, < 2 pts)
        if len(arc) > 1:
            arcs.append(arc)
        # create a shapely Linestring object of arcs
        arcsLine = [LineString(ar) for ar in arcs]
        return arcsLine

    def cut_mline_by_junctions(self, myShape, dictJunctions):

        """
        Returns MultiLineStrings divided as arcs at junction points from MultiLineStrings.

        lineList = shapely geom collection, Multilinestring
        """


        lineList = myShape.geoms
        junctionedLines = []
        multiJunctionedLines = []
        for line in lineList:
            # breaks the MultiLine Geom collection into LineStrings
            # finds the junctions in the LineStrings and cuts them
            # accordingly
            junctionedLines.append(self.cut_line_by_junctions(line, dictJunctions))
        for cut_mline in junctionedLines:
            # writes the re-junctioned Linestrings back as a MultiLineString
            multiJunctionedLines.append(MultiLineString(cut_mline))

        #multiLineArc = MultiLineString(multiJunctionedLines)

        return multiJunctionedLines


class GeomSimplify(object):


    def simplify_line(self, line, threshold):
        """

        Simplifies LineString objects. Returns a shapely LineString obj.

        Note: unlike rings, we need to keep beginning and end points static throughout the simplification process

        """
        # Build list of Triangles from the line points
        triangleArray = []
        ## each triangle contains an index and a point (x,y)
        # handle line 'interior' (i.e. the vertices
        #  between start and end) first -- explicitly
        # defined using the below slice notation
        # i.e. [1:-1]
        for index, point in enumerate(line.coords[1:-1]):
            triangleArray.append(TriangleCalculator(point, index))

        # then create start/end points separate from the triangleArray (meaning
        # we cannot have the start/end points included in the heap sort)
        startIndex = 0
        endIndex = len(line.coords)-1
        startTriangle = TriangleCalculator(line.coords[startIndex], startIndex)
        endTriangle = TriangleCalculator(line.coords[endIndex], endIndex)

        # Hook up triangles with next and prev references (doubly-linked list)
        # NOTE: linked list are composed of nodes, which have at
        # least one link to another node (and this is a doubly-linked list..pointing at
        # both our prevTriangle & our nextTriangle)
        # NOTE: in this code block the 'triangle' is our 'triangle node'

        for index, triangle in enumerate(triangleArray):
            # set prevIndex to be the adjacent point to index
            prevIndex = index - 1
            nextIndex = index + 1

            if prevIndex >= 0:
                triangle.prevTriangle = triangleArray[prevIndex]
            else:
                triangle.prevTriangle = startTriangle

            if nextIndex < len(triangleArray):
                triangle.nextTriangle = triangleArray[nextIndex]
            else:
                triangle.nextTriangle = endTriangle

        # Build a min-heap from the TriangleCalculator list
        # print "heapify"
        heapq.heapify(triangleArray)


        # Simplify steps...


        # Note: in contrast
        # to our function 'simplify_ring'
        # we can allow our array to go down to 0 and STILL have a valid line
        # because we will still have the start and end points
        while len(triangleArray) > 0:
            # if the smallest triangle is greater than the threshold, we can stop
            # i.e. loop to point where the heap head is >= threshold
            if triangleArray[0].calcArea() >= threshold:
                #print "break"
                break
            else:
                # print statement for debugging - prints area's and coords of deleted/simplified pts
                #print "simplify...triangle area's and their corresponding points that were less then the threshold"
                #print "area = " + str(triangleArray[0].calcArea()) + ", point = " + str(triangleArray[0].point)
                prev = triangleArray[0].prevTriangle
                next = triangleArray[0].nextTriangle
                prev.nextTriangle = next
                next.prevTriangle = prev
                # This has to be done after updating the linked list
                # in order for the areas to be correct when the
                # heap re-sorts
                heapq.heappop(triangleArray)


        # Create an list of indices from the triangleRing heap
        indexList = []
        for triangle in triangleArray:
            # add 1 b/c the triangle array's first index is actually the second point
            indexList.append(triangle.ringIndex + 1)
        # Append start and end points back into the array
        indexList.append(startTriangle.ringIndex)
        indexList.append(endTriangle.ringIndex)

        # Sort the index list
        indexList.sort()

        # Create a new simplified ring
        simpleLine = []
        for index in indexList:
            simpleLine.append(line.coords[index])

        # Convert list into LineString
        simpleLine = LineString(simpleLine)

        return simpleLine

    def simplify_multiline(self, mline, threshold):
        """
        Simplifies MultiLineStrings. Returns a shapely MultiLineString obj.

        """
         # break MultiLineString into lines
        lineList = mline.geoms
        simpleLineList = []

        # call simplify_line on each
        for line in lineList:
            simpleLine = self.simplify_line(line, threshold)
            #if not none append to list
            if simpleLine:
                simpleLineList.append(simpleLine)

        # check that line count > 0, otherwise return None
        if not simpleLineList:
            return None

        # put back into multilinestring
        return MultiLineString(simpleLineList)

def str2bool(v):
    """
    Converts strings (which all command line passed argument are) to booleans.

    """
    return v.lower() in ("yes", "true", "t", "1")


def main():
    print "number of arguments (incl. py file name): " + str(len(sys.argv))
    if len(sys.argv) != 5:
        print "Wrong amount of arguments!"
        usage()
        exit()

    geomSimplifyObject = PreserveTopology()

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    threshold = sys.argv[3]
    topology = sys.argv[4]
    topology_convert = str2bool(topology)

    if topology_convert is False:
        geomSimplifyObject.process_file(inputFile, outputFile, float(threshold), topology_convert)
        print "Finished simplifying file (with topology NOT preserved)!"
    elif topology_convert is True:
        geomSimplifyObject.process_file(inputFile, outputFile, float(threshold), topology_convert)
        print "Finished simplifying file (topology was preserved)!"

def usage():
    print "python simplify_topology.py <input file path> <output file path> <threshold> Topology= <True> or <False>"


if __name__ == "__main__":
    main()
