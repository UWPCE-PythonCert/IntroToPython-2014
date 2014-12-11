

import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

import termp_funcs
reload(termp_funcs)

from termp_funcs import plotprep

import pdb
import pandas as pd
import matplotlib.pyplot as plt


# create the instance from the data file


def callclass():
    dfile = 'datafiles/test_chemistry.xlsx'
    return plotprep(dfile)

# use the class object and methods to select and prepare data for plotting
chem = callclass()
chem.selectSample('14051202')
chem.selectForPlot('SW8082A')
plot_dict = chem.makePlotobj()


# create a function to make use of the plot_dict


def plotSampdict(**kwargs):
    """Takes plotting dictionary from plotprep and returns figure

       Not sure how to test this function since most of what is
       rendered goes to the screen.
       """

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    # creating the bar graph of results
    ax1.bar(kwargs.get('x_ticks'),
            kwargs.get('y_value'), 0.35)

    # decorate x-axis with ticks and labels
    ax1.set_xticks([n - 0.25 for n in kwargs.get('x_ticks')])
    ax1.set_xlim(0, kwargs.get('x_ticks')[-1]+1)
    ax1.set_xticklabels(kwargs.get('x_label'),
                        rotation=45)
    ax1.set_xlabel('Sample Parameter')

    # decorate y-axis with ticks, label
    ax1.set_ylabel('Concentration in ug/kg', rotation='vertical')

    # in principle visualization is expensive, so we save it for the end
    fig.canvas.draw()
    fig.show()
    return (fig, ax1)

# call function with dict
fig1, ax1 = plotSampdict(**plot_dict)

"""some test ideas, check output of fig1 and ax1 types,
   additional inspection of figure"""