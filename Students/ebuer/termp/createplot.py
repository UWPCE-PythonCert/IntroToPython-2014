

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
# this could easily be turned into an fx w/dict arg for efficient looping
# with either sys.argv or an additional script to feed values


def makeSampdict(**kwargs):
    chem = callclass()
    chem.selectSample(kwargs['sample'])
    chem.selectForPlot(kwargs['method'])
    plot_dict = chem.makePlotobj()
    return plot_dict

test_samp = {'sample': '14051305', 'method': 'SW8082A'}
plot_dict = makeSampdict(**test_samp)


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
    ax1.set_ylim(plot_dict['y_lims'])
    ax1.set_ylabel('Concentration in {u_units}'.format(**kwargs), rotation='vertical')

    # create annotation
    anno_text = 'Results for Sample: {u_sample}  Analytical Method: {u_method}'.format(**kwargs)
    # ax1.annotate(anno_text, xy=(kwargs['x_ticks'][0]-0.5, kwargs['y_lims'][1]))
    ax1.set_title(anno_text)


    # in principle visualization is expensive, so we save it for the end
    d = {'pad': 2, 'w_pad': 1, 'h_pad': 1}  # keyword dict for padding
    fig.set_tight_layout(d)

    fig.canvas.draw()
    # plt.savefig('test_figure.pdf')
    fig.show() # after many trial runs and tests screen vis not needed
    return (fig, ax1)

# call function with dict
fig1, ax1 = plotSampdict(**plot_dict)
