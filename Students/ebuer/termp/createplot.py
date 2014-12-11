

import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

import termp_funcs
reload(termp_funcs)

from termp_funcs import plotprep as pp
import pdb

import pandas as pd
import matplotlib.pyplot as plt

# create the class from the data file
def callclass():
    dfile = 'datafiles/test_chemistry.xlsx'
    p_test = pp(dfile)
    return p_test

# use the class object and methods to select and prepare data for plotting
chem = callclass()
chem.selectSample('14051202')
chem.selectForPlot('SW8082A')
plot_dict = chem.makePlotobj()

# create a function to make use of the plot_dict
def plotSdict(**kwargs):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(kwargs.get('x_ticks'), kwargs.get('y_value'), 0.35)
    fig.canvas.draw()
    fig.show()

# call function with dict
plotSdict(**plot_dict)

