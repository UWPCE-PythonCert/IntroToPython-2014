from codingbat import cat_dog


def test_true_string():
    assert cat_dog('catdog')
    assert cat_dog('1cat1cadodog')


def test_false_string():
    assert not cat_dog('catcat')


def test_no_cat_dog():
    assert cat_dog('fishfishfish')



# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True