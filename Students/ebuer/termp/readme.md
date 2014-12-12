##Term Project Readme  
Basic project construct: use newfound python knowledge combined with pandas and matplotlib modules to create a simple data visualization tool for environmental chemistry data.

###plotprep Class Attributes  
All attributes at this time are mutable to allow for tinkering.

_raw_data_  
Raw import of the data used in class initialization

_selected_data_  
Columns selected from raw_data that are processed as part of the plotprep. Original raw_data is left untouched in the event it needs to be examined later.

_samples_  
A list of unique sample identifiers pulled from selected_data.

_qc_samples_  
A llist of unique qc sample identifiers pulled from selected_data

_sampleData_  
Analytical results selected based on the sample id handed to the selectSample method.

_plotData_  
Analytical results for the sample identified using selectSample and the method provided to selectForPlot. Results do not include spiked sample recoveries.

_plot_dict_  
Plotting dictionary created by makePlotobj method, requires that both plotData already have been selected and assigned as an attribute of the class instance


####Class Methods  
_showOptions_  
Automatically called by other methods to display a unique list of options for the user such as sample identifiers or methods used on a specific sample.

_selectSample_  
Returns sampleData attribute to the class instance.  sampleData are the columns of selected_data reduced down to only the selected sample.

Syntax: selectSample(sample_id)  

Note: type(sample_id) must match what is in the raw_data.

_selectForPlot_  
Returns plotData attribute to the class instance.  plotData is the set of analytical results from the selected_data reduced down by sample in _selectSample_ and by the method entered.

Syntax: selectForPlot(analytical_method)

_makePlotobj_  
Returns plotting dictionary attribute to the class instance.  Method takes no arguments, but requires that selectSample and selectForPlot have already been run to be fully populated

###Createplot.py  
Script initializes plotprep object and creates plotting dictionary for sample-method pair passed in as test_samp dictonary using _makeSampdict_.  

_plotSampdict(**kwargs)_  
Takes plotting dictionary created in the plotprep instance of _makeSampdict_ and renders a bar chart of results with labeling and laboratory flags applied to the top of each column.  Returns figure and subplot objects for further tinkering.
