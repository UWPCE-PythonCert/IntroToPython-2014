from .codebat import sleep_in, cigar_party


def test_false_false():
    assert sleep_in(False, False)


def test_true_false():
    assert sleep_in(True, False)


def test_false_true():
    assert sleep_in(False, True)


def test_50_false():
    assert cigar_party(50, False)


def test_70_true():
    assert cigar_party(70, True)


def test_50_true():
    assert cigar_party(50, True)


def test_60_false():
    assert cigar_party(60, False)


def test_39_true():
    assert not cigar_party(39, True)
