"""read_enviro
   File contains seris of steps and functions to read in environmental data from raw xlsx file provided by data validation firm"""

#modules
import pandas as pd
import sys
import termp_funcs as tf

from pandas import DataFrame as df

#developent requires we reload the module every time to add changes
reload(tf)

#read in the data and pull out columns into a new df
# dfile = sys.argv[1]  # think about converting up with sys.argv[1] when everything works correctly

dfile = 'datafiles/test_chemistry.xlsx'
raw_data = tf.get_data(dfile)
selected_data = tf.select_columns(raw_data)



