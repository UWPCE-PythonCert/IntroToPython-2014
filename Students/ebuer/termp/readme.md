###Term Project Readme  
Basic project construct: use newfound python knowledge combined with pandas and matplotlib modules to create a simple set of data visualization tools for environmental chemistry and monitoring data.

**Desired Key Elements**  
* Read in environmental data from format delivered
* Visualize detected results on a single image
* Apply estimate flag to qualified results
* Add axis and constituent labeling as appropriate
* Plot multiple sets of data on shared axis graphs or a single image for monitoring/environmental data

####Part 1: Read in data
Environmental chemistry data is delivered in csv or xlsx format.  After validation it is almost always delivered as an xlsx file.  Use pandas module along with other techniques to create a data set for plotting.

Several points to work out:  
* multiple sample names per sheet -- need unique list of samples
* create list (or tuple?) of parameters analyzed in each sample
* take advantage of index feature to pull out flags
* make dict of plotting parameters to pass to chart