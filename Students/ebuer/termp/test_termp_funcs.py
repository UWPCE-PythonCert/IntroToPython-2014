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

    # assert 'MS' in p_test.qc_samples
    # assert 'LRS' in p_test.qc_samples
    # assert '14051306' not in p_test.qc_samples

