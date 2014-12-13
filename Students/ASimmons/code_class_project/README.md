
<html>
<head>
</head>
<body>
# Table of Contents
[Team Members](#team-members)

[Project Summary](#project-summary)

# <a name="team-members"></a>Team Members
* "Arielle Simmons" <ari.ucb.fire@gmail.com>
	- Data Engineer 
	
# <a name="project-summary"></a>Project Summary

Using the following Python packages:

	1) Fiona (1.4+) [1] 
	2) Shapely (1.3+) [2]

Final Project (12/12/14) Update: I followed the steps outlined in M. Bostock's "How To Infer Topology" [3] 
to design a 'PreserveTopology' module that will identify topological elements in a LineString and/or 
MultiLineString shapefile. Combined with two other classes (written by me awhile ago) called GeomSimplify()
and TriangleCalculator(), a user can call my simplify_topology.py library from command line and
create a simplified version of any LineString or MultiLineString shapefile.  

The primary work that I completed includes:

	1) identify junctions (intersection points) in LineString/MultiLineString shapefiles
	2) split geometric 'arcs' at their junction points (note: I decided for MultilineStrings and Linestrings
       the need to de-duplicate geometric 'arcs' was unnecessary. However, it will have to be done 
	   in order to complete the code for Polygon and MultiPolygon shape types). 
	3) complete 10 unittests which tested the functionality of the PreserveTopology() class.


Key points to note:

	- All the code within the GeomSimplify() and TriangleCalculator() classes was undertaken 
	  in a previous code I wrote here: [4] and should NOT be counted as part of my class project.
	- All functions that were drafted as part of this class project have test functions. Test
      functions for code that WASN'T part of the project (i.e. the GeomSimplify() and TriangleCalculator()
      class is included at this repo [4].	  
	- to run from command line: python simplify_topology.py <input file path> <output file path> <threshold> Topology=<True> or <False>
	- the 'sample_lines.shp' included is a test file. When ran through this code with the Topology 
	  flag set to 'True' it created 'sample_lines_TopoTrue':
	  
	  python .\simplify_topology.py .\sample_lines.shp .\sample_lines_TopoTRUE 10000000 True
	  
	  When ran with this code with the flag set to 'False' it created 'sample_lines_TopoFALSE':
	  
	  Python .\simplify_topology.py .\sample_lines.shp .\sample_lines_TopoTRUE 10000000 False

References:

	1: https://pypi.python.org/pypi/Fiona
	2: https://pypi.python.org/pypi/Shapely
	3: http://bost.ocks.org/mike/topology/
	4: https://github.com/ARSimmons/Shapely_Fiona_Visvalingam_Simplify
	
*NOTE: THIS PROJECT IS turned in for code review on 12/12/2014*
 
</body>
</html>