from coding_bat import string_splosion, cigar_party, count_evens

# Tests for string_slosion()

def test_x():
    assert string_splosion('x') == 'x'


def test_ab():
    assert string_splosion('ab') == 'aab'


def test_abc():
    assert string_splosion('abc') == 'aababc'


def test_the_word_code():
    assert string_splosion('Code') == 'CCoCodCode'


def test_the_word_kitten():
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'

# Tests for cigar party


def test_30_false():
    assert not cigar_party(30, False)


def test_50_false():
    assert cigar_party(50, False)


def test_70_true():
    assert cigar_party(70, True)


def test_30_true():
    assert not cigar_party(30, True)


def test_60_false():
    assert cigar_party(60, False)


def test_40_false():
    assert cigar_party(40, False)


def test_40_true():
    assert cigar_party(40, True)

# Count evens


def test_all_evens():
    assert count_evens([2, 4, 6, 8, 10]) == 5


def test_all_odds():
    assert count_evens([1, 3, 5, 7, 9]) == 0


def test_evens_and_odds():
    assert count_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4
