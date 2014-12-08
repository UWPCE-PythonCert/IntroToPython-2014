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

        self.selected_data = self.raw_data[column_args]

        """Return an array of field samples and a second array of qc_samples"""
        # unames = dframe.sample_name.unique()
        # unames_list = [u for u in unames]
        qc_samp_tag = ['MS', 'LR', 'LCS', 'MB', 'SD']
        temp_array = self.selected_data['sample_name']

        mask = [True for t in temp_array]
        i_mask = [False for f in temp_array]

        for q in qc_samp_tag:
            for i, name in enumerate(temp_array):
                # pdb.set_trace()
                if q in name:
                    mask[i] = False
                    i_mask[i] = True

        self.samples = temp_array[mask]
        self.qc_samples = temp_array[i_mask]



