
from codingbat import monkey_trouble


def test_true_true():
    assert monkey_trouble(True, True)


def test_false_false():
    assert monkey_trouble(False, False)


def test_true_false():
    assert monkey_trouble(True, False) is False


def test_false_true():
    assert monkey_trouble(False, True) is False
