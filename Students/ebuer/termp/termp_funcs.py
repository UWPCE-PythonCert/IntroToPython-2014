"""termp_funcs
Contains class plotprep which is initialized using a validated data file.

Class  methods include:
  showOptions: method called by class methods to print out list of available values
  selectSample: selects a sample from the data that has been read
  selectMethod: subsets data returned by selectSample using the method value passed
  makePlotobj: creates plotting object from output of selectMethod to be passed to plotting class

"""

import pandas as pd
import pdb


class plotprep(object):
    """Class is initialized with validated data file and used to create plotting object"""

    def __init__(self, dfile):
        self.raw_data = pd.read_excel(dfile, 'tbl_EXPORT')

        """Create new dataframe from existing using selected columns"""
        column_args = ['sample_name',
                       'sample_date_time',
                       'lab_sample_id',
                       'cas_rn',
                       'std_anl_method_name',
                       'chemical_name',
                       'result_value',
                       'result_unit',
                       'lab_flag',
                       'dilution_factor',
                       'sample_matrix_code',
                       'method_detection_limit',
                       'Validation Qualifiers',
                       'Validation Reason',
                       'Interpreted Qualifier']

        # reduced data set for plotting
        self.selected_data = self.raw_data[column_args]

        """Return an array of field samples and a second array of qc_samples"""
        qc_samp_tag = [u'MS', u'LR', u'LCS', u'MB', u'SD']
        temp_array = self.selected_data['sample_name']

        mask = [True for t in temp_array]
        i_mask = [False for f in temp_array]

        # create masks to subset samples and qc
        for q in qc_samp_tag:
            for i, name in enumerate(temp_array):
                # pdb.set_trace()
                if q in name:
                    mask[i] = False
                    i_mask[i] = True

        # samples and qc samples each in their own class attribute
        self.samples = temp_array[mask]
        self.qc_samples = temp_array[i_mask]

        # create a unique list of sample names
        # self.sample_ids = self.samples.unique()
        s_dict = {'name': 'samples', 'o_list': self.samples.unique()}
        self.showOptions(**s_dict)

    def showOptions(self, **arg_dict):
        """Method is called to print out available options"""
        print 'List of available {name}: '.format(**arg_dict)
        o_list = arg_dict.get('o_list')

        for i, sid in enumerate(o_list):
            kwargs = {'i': i, 'sid': sid}
            print '{i: >2}. {sid: >10}'.format(**kwargs)

    def selectSample(self, sample_id='14051202'):
        """Return rows of data for selected sample"""
        sample_mask = self.samples.isin([sample_id])
        sample_rows = self.samples[sample_mask]
        data_index = sample_rows.index

        # test data to makes sure every row has passed sample_id
        if not sample_rows.isin([sample_id]).any(0):
            raise ValueError('A bad sample ID was passed')

        self.sampleData = self.selected_data.loc[data_index]
        self.sampleData = self.sampleData.dropna()

        # self.plotData = self.plotData.reset_index('index')

        temp = self.sampleData['std_anl_method_name']
        m_dict = {'name': 'methods', 'o_list': temp.unique()}
        self.showOptions(**m_dict)

        return self.sampleData

    def selectForPlot(self, methodval='SW7470A'):
        """Present methods for sampleData, subset based on method selection"""

        # filter self.sampleData by method and return to class
        mask = self.sampleData['std_anl_method_name'].isin([methodval])
        # pdb.set_trace()
        self.plotData = self.sampleData[mask]
        # pdb.set_trace()
        # self.plotData = self.plotData.reset_index()

        return self.plotData


    def makePlotobj(self):
        """take method-subsetted data and make a plotting object (dict?)"""

        # take self.selectMethod data as argument
        x_label = [x for x in self.plotData['chemical_name']]
        y_value = [y for y in self.plotData['result_value']]
        flag =    [f for f in self.plotData['lab_flag']]

        self.plot_dict = {'x_label': x_label, 'y_value': y_value, 'flag': flag}

        return (self.plot_dict)

        # make dictionary for plotting that can be read by matplotlib






