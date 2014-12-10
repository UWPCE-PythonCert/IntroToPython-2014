"""termp_funcs"""

import pandas as pd
import pdb


class plotprep(object):

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

        # self.showOptions(({'name':'samples', 'plist':self.samples.unique()})

    def showOptions(self, name='samples', olist=[]):
        print 'List of available {name}: '.format(name)

        for i, sid in enumerate(olist):
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
        self.sampleData = self.plotData.dropna()

        # self.plotData = self.plotData.reset_index('index')

        return self.sampleData

    def selectMethod(self, sampleData):
        """Present methods for sample, subset sampleData based on method selection"""
        temp = self.sampleData.columns('std_anl_method_name')
        # self.showOptions(('methods', temp.unique()))

        # prompt for input

        # filter self.sampleData by method

        # return filtered data


    def makePlotobj(self):
        """take method-subsetted data and make a plotting object to hand over to matplotlib"""

        # take self.selectMethod data as argument

        # make dictionary for plotting that can be read by matplotlib






