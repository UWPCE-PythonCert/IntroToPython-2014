"""
Testing of my make10 function

Make sure that pytest is installed.
Since the name of this testing script file begins with 'test_'
pytest will find it and run it.

In the directory where this file lives, simply do:
    $ py.test

For more information, see: www.pytest.org
"""
import pytest
from make10 import make10

test_data = [ ( ( 10, 3), True),
              ( ( "a", 10), True),
              ( ( 9, "b"), False),
              ( ( 12, -2), True),
              ( ( 8, 3), False),
              ( ( "a", "b"), False) ]

@pytest.mark.parametrize(("input", "result"), test_data)
def test_make10(input, result):
    assert make10(*input) == result