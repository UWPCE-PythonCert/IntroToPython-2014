"""test_termp_funcs
    Tests used to guide development of class objects and methods
"""
import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

from termp_funcs import plotprep as pp
import pdb

def callclass():
    dfile = 'datafiles/test_chemistry.xlsx'
    p_test = pp(dfile)
    return p_test


def test_select_columns():
    p_test=callclass()
    assert len(p_test.selected_data.columns) == 15


def test_getsamples():
    p_test=callclass()
    samples = [s for s in p_test.samples]

    assert 'MS' not in samples
    assert 'LRS' not in samples
    assert '14051306' in samples

    assert len(p_test.samples) + len(p_test.qc_samples) == len(p_test.selected_data['sample_name'])


def test_showOptions():
    # this is a sort of lame test but the function only prints to screen
    # so simply failing to run to completion is all that is tested
    p_test = callclass()

    junk_dict = {'name': 'samples', 'o_list': p_test.samples.unique()}
    p_test.showOptions(**junk_dict)

    two_dict = {'name': 'methods', 
                'o_list': ['Method A', 'Method B', 'Method C']}
    p_test.showOptions(**two_dict)
    assert True


def test_selectSample():
    p_test = callclass()
    p_sampled = p_test.selectSample('14051305')

    assert p_sampled is not None
    assert p_sampled['sample_name'].isin(['14051305']).all() == True


def test_selectForPlot():
    p_test = callclass()
    sample_full = p_test.selectSample('14051305')
    sample_plot = p_test.selectForPlot('SW8082A')

    assert len(sample_plot.columns) > 1
    assert sample_plot['std_anl_method_name'].isin(['SW8082A']).all() == True


def test_makePlotobj():
    p_test = callclass()
    p_test.selectSample('14051305')
    p_test.selectForPlot('SW8082A')
    # pdb.set_trace()
    sample_dict = p_test.makePlotobj()

    assert type(sample_dict) is dict
    assert sample_dict['x_label'][0] == 'Aroclor 1016'
    assert sample_dict['y_value'][0] is not None
    assert type(sample_dict['y_value'][0]) is float
    assert sample_dict['u_units'] == 'ug/kg'
