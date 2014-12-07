"""termp_funcs"""

import pandas as pd
from pandas import DataFrame as df

import termp_funcs as tf

def test_select_columns():
    dframe = tf.get_data('datafiles/test_chemistry.xlsx')
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

    selected_frame = dframe[column_args]
    assert len(selected_frame.columns) == 15


