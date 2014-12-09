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
                       'sample_type_code',
                       'cas_rn',
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
        self.sample_ids = self.samples.unique()

        print 'List of available samples: '

        for i, sid in enumerate(self.sample_ids):
            kwargs = {'i': i, 'sid': sid}
            print '{i: >2}. {sid: >10}'.format(**kwargs)

    def plotSample(self, sample_id='14051306'):
        sample_mask = self.samples.isin(sample_id)
        sample_rows = self.samples[sample_mask]

        if not sample_rows.all(sample_id):
            raise ValueError('A bad sample ID was passed')

        return self.pS
