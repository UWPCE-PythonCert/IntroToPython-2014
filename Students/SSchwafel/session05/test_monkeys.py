#!/usr/bin/python
from codingbat_lab import monkey_trouble

def test_monkey_trouble():
    assert monkey_trouble('True', 'True') == True
    assert monkey_trouble('True', 'False') == False
    assert monkey_trouble('False', 'False') == True
    assert monkey_trouble('False', 'True') == False

