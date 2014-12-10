"""termp_funcs"""

import pandas as pd
import pdb


class plotprep(object):

    def __init__(self, dfile):
        self.dfile = dfile
        self.raw_data = pd.read_excel(dfile, 'tbl_EXPORT')


    def select_columns(self, dframe):
        """Creates new dataframe from existing using selected columns"""
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
        dframe = dframe[column_args]
        return dframe

    def get_samples(self, dframe):
        """Returns an array of field samples and a second array of qc_samples"""
        # unames = dframe.sample_name.unique()
        # unames_list = [u for u in unames]
        qc_samp_tag = [u'MS', u'MSD', u'LR', u'LCS', u'MB', u'SD']

        mask = []
        i_mask = []
        for i, d in enumerate(dframe):
            for q in qc_samp_tag:
                if q in d:
                    mask[i] = False
                    i_mask[i] = True
                    print i
                    continue
                else:
                    mask[i] = True
                    i_mask[i] = False
                    print i
                    
        samples = dframe[mask]
        qc_samples = dframe[i_mask]
        return (samples, qc_samples)









        # for q in qc_samp_tag:
        #     for i, u in enumerate(unames_list):
        #         if q in u:
        #             unames_list.pop(i)
        # return unames_list

