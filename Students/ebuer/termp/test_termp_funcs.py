"""termp_funcs"""
import sys
sys.path.append(r"D:\GitHub\IntroToPython\Students\ebuer\termp")

from termp_funcs import plotprep as pp

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
    p_test=callclass()
    junk_dict = {'name': 'samples', 'plist': p_test.samples.unique()}
    p_test.showOptions(junk_dict)

    two_dict = {'name': 'methods', 'plist': ['Method A', 'Method B', 'Method C']}
    p_test.showOptions(two_dict)


def test_selectSample():
    p_test = callclass()
    p_plot = p_test.selectSample('14051306')

    assert p_plot is not None
    
