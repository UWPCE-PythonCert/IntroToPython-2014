from codingbat import sleep_in

def test_false_false():
	assert sleep_in(False, False)

def test_true_false():
	assert not (sleep_in(True, False))

def test_false_true():
	assert sleep_in(False, True)

def test_true_true():
	assert sleep_in(True, True)
