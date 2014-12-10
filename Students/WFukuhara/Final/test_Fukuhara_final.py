""" 
test harness for Fukuhara_final.py

"""

import sys
from StringIO import StringIO
from Fukuhara_final import highlowresults
from Fukuhara_final import opencloseresults


def test1_avgresults( ):
    assert 'test' in highlowresults('test', 2)    # correct string in results

def test2_avgresults( ):
    assert '44.06' in highlowresults('test', 2)    # correct result for avg High

def test3_avgresults( ):
    assert '50.00' not in highlowresults('test', 2)    # incorrect result for avg High

def test4_avgresults( ):
    assert '39.10' in highlowresults('test', 3)    # corrrect results for avg Low

def test5_avgresults( ):
    assert '40.00' not in highlowresults('test', 3)    # incorrect result for avg Low


def test6_fileoutput( ):
    out = StringIO( )
    opencloseresults( out = out )
    output = out.getvalue( )
    assert '10/1/14' in output   # beginning date

def test7_fileoutput( ):
    out = StringIO( )
    opencloseresults( out = out )
    output = out.getvalue( )
    assert '10/3/94' in output    # ending date

def test8_fileoutput( ):
    out = StringIO( )
    opencloseresults( out = out )
    output = out.getvalue( )
    assert '11/1/14' not in output    # date does not exist

def test9_fileoutput( ):
    out = StringIO( )
    opencloseresults( out = out )
    output = out.getvalue( )
    assert '89.08' in output    # beginning data result in one of the columns

def test10_fileoutput( ):
    out = StringIO( )
    opencloseresults( out = out )
    output = out.getvalue( )
    assert '90.00' not in output    # data result not in any of the columns
