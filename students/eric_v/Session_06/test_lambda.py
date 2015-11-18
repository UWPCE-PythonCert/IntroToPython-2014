"""
some simple tests for the function builder

designed to run with py.test or nose.
"""

from lambda_keyword import function_builder
# uncomment to test second version
# from lambda_keyword import function_builder2 as function_builder


def test_length():
    """
    the function should return a list of the length input
    """
    assert len(function_builder(0)) == 0

    assert len(function_builder(3)) == 3

    assert len(function_builder(5)) == 5


def test_increment():
    """
    the functions in the list should increment the input values
    """
    func_list = function_builder(5)

    assert func_list[0](3) == 3

    assert func_list[1](3) == 4

    assert func_list[2](3) == 5

    assert func_list[3](3) == 6


def test_increment2():
    """
    the functions in the list should increment the input values
    """

    func_list = function_builder(10)

    assert func_list[0](12) == 12

    assert func_list[1](10) == 11

    assert func_list[9](3) == 12
