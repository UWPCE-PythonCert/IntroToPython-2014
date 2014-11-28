
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

I propose to follow the steps outlined in M. Bostock's "How To Infer Topology" [3] to design 
a 'PreserveTopology' module that will identify topological elements in a LineString or 
MultiLineString shapefile (and possibly Polygon/Multipolygons...time allowing).

As described in the article, the primary work that I will undertake will include:

	1) identify junctions (intersection points) in LineString/MultiLineString shapefiles
	2) split (and rotate) geometric 'arcs' at their junction points.
	3) delete duplicate geometric 'arcs' that have no junction points but lie directly
	   on top of an identical geometric feature.


Key points to note:

	- Other work that M. Bostock notes as being necessarary
	 (...namely: "extract - decompose shapes into lines and rings"...) has already been 
	  undertaken in a previous code I wrote here: [4].
	- All functions will include test code.   
	- to run from command line: python simplify_topology.py <input file> 

References:

	1: https://pypi.python.org/pypi/Fiona
	2: https://pypi.python.org/pypi/Shapely
	3: http://bost.ocks.org/mike/topology/
	4: https://github.com/ARSimmons/Shapely_Fiona_Visvalingam_Simplify
	
*NOTE: THIS PROJECT IS STILL in progress as of 11/23/2014*
 
</body>
</html>