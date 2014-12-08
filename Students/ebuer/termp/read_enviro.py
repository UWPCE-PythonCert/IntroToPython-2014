"""read_enviro
   File contains seris of steps and functions to read in environmental data from raw xlsx file provided by data validation firm"""

import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

#modules
from termp_funcs import plotprep as pp


# developent requires we reload the module every time to add changes
reload(pp)

# read in the data and pull out columns into a new df
# dfile = sys.argv[1]  
# think about converting up with sys.argv[1] when everything works correctly

dfile = 'datafiles/test_chemistry.xlsx'
p_instance = pp(dfile)

selected_data = pp.select_columns(p_instance.raw_data)
sample_list, qc_list = pp.get_samples(selected_data)



