__author__ = 'asimmons'

import shapely
import fiona
from shapely.geometry import shape, LineString, Polygon, MultiLineString, MultiPolygon
import math


# g = PreserveTopology();g.find_junctions(r'I:\It_23\simplify\test_lines_simplify_topology\sample_lines.shp')

class PreserveTopology:

    quantitizationFactor = (10000,10000)

    def set_quantitization_factor(self, quantValue):
        self.quantitizationFactor = (quantValue, quantValue)

    def find_junctions(self, inFile):
        """
        Takes an 'inFile' of an ESRI shapefile, converts it into a Shapely geometry,
        returns a dictionary of junction points found in all shapes.

        - A point is considered a junction if it shares the same point
        with another shape AND has different neighbors.

        - Identical features on top of one another DO NOT have different
        neighbors, and therefor DO NOT have any junctions.
        """

        # key = quantitized junction points, value = 1
        dictJunctions = {}
        # key = checked quantitized points, value = array of quantitized neighbors
        dictNeighbors = {}

        #Open input file

        # loop over each
        with fiona.open(inFile, 'r') as input:

            # Read shapely geometries from file
            # Loop through all shapely objects
                for myGeom in input:

                    myShape = shape(myGeom['geometry'])

                    if isinstance(myShape, Polygon):
                        myShape = self.find_junctions_polygon(myShape, dictJunctions, dictNeighbors)
                    elif isinstance(myShape, MultiPolygon):
                        myShape = self.find_junctions_multipolygon(myShape, dictJunctions, dictNeighbors)
                    elif isinstance(myShape, LineString):
                        myShape = self.find_junctions_line(myShape, dictJunctions, dictNeighbors)
                    elif isinstance(myShape, MultiLineString):
                        myShape = self.find_junctions_multiline(myShape, dictJunctions, dictNeighbors)
                    else:
                        raise ValueError('Unhandled geometry type: ' + repr(myShape.type))

        return dictJunctions

    def quantitize(self, point):
        # the default quantization factor is 10,000 (-q 1e4)
        # Divide by quantitiztion factor, round(int), multiply by quantitization factor
        x_quantitized = int(round(point[0]/self.quantitizationFactor[0]) * self.quantitizationFactor[0])
        y_quantitized = int(round(point[1]/self.quantitizationFactor[1]) * self.quantitizationFactor[1])

        return (x_quantitized,y_quantitized)

    def append_junctions(self, dictJunctions, dictNeighbors, pointsList):
        """

        Builds a global dictionary of all the junctions and neighbors found in all
        the shapes. It determines if a point is a junction based on if it shares the same
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



    def find_junctions_line(self, myShape, dictJunctions, dictNeighbors):

        pointsLineList = list(myShape.coords)

        self.append_junctions(dictJunctions, dictNeighbors, pointsLineList)


    def find_junctions_multiline(self, dictJunctions, dictNeighbors):

        raise ValueError('simplify_topology not implemented yet for: ' + repr(myShape.type))

    def find_junctions_polygon(self, dictJunctions, dictNeighbors):

        raise ValueError('simplify_topology not implemented yet for: ' + repr(myShape.type))

    def find_junctions_multipolygon(self, dictJunctions, dictNeighbors):

        raise ValueError('simplify_topology not implemented yet for: ' + repr(myShape.type))

#    def ring_coords(self, inFile):


#        return ringPts

#    def lines_2_arcs(self):
    # break lines into arcs by junctions
#        return

#    def polygons_2_arcs(self):
#        return
    # break polygon rings into arcs by junctions


#    def delete_dup_ring_arcs(self):

    # delete ring arcs that are duplicate boundaries
#        return

#    def simplify_arcs(self):
    # simplify lines and rings by arc segments
#        return
