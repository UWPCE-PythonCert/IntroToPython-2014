"""termp_funcs"""
import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

from termp_funcs_rf import plotprep as pp

def test_select_columns():
    dfile = 'datafiles/test_chemistry.xlsx'
    p_test = pp(dfile)

    assert len(p_test.selected_data.columns) == 15


def test_getsamples():
    dfile = 'datafiles/test_chemistry.xlsx'
    p_test = pp(dfile)

    samples = [s for s in p_test.samples]

    assert 'MS' not in samples
    assert 'LRS' not in samples
    assert '14051306' in samples

    assert len(p_test.samples) + len(p_test.qc_samples) == len(p_test.selected_data['sample_name'])


def test_plotSample():
    dfile = 'datafiles/test_chemistry.xlsx'
    p_test = pp(dfile)

    p_plot = p_test.plotSample('14051306')

    assert p_plot is not None
