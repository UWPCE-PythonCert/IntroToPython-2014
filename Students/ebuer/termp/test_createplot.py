
import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

from termp_funcs import plotprep

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import pytest

from createplot import callclass, plotSampdict

def tsetup():
    chem = callclass()
    chem.selectSample('14051202')
    chem.selectForPlot('SW8082A')
    plot_dict = chem.makePlotobj()
    return (chem, plot_dict)


def test_pSd():
    chem, plot_dict = tsetup()
    fig1, ax1 = plotSampdict(**plot_dict)

    with pytest.raises(TypeError):
        plotSampdict('blah') 
    assert type(fig1) is plt.Figure
    assert type(ax1) is mpl.axes.Subplot

def test_ax1():
    chem, plot_dict = tsetup()
    fig1, ax1 = plotSampdict(**plot_dict)

    assert ax1.xaxis.get_label_text() == 'Sample Parameter'
