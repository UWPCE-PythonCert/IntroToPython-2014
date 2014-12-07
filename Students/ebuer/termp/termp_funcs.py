"""termp_funcs"""

import pandas as pd
from pandas import DataFrame as df

def get_data(dfile):
    "Returns dataframe of raw data"
    return pd.read_excel(dfile, 'tbl_EXPORT')


def select_columns(dframe):
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
    return dframe[column_args]

